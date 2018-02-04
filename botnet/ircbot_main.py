import json
import subprocess
import socket
import ssl
import sys
import time
import random

class IRCController(object):
    def __init__(self, **kwargs):
        self.server = kwargs['server']
        self.port = kwargs['port']

        self.username = kwargs['username']
        self.channel = kwargs['channel']
        
        self.nickname = self.username
        self.name = self.username

        self.hostname = "fakeaf"
        self.master = kwargs['master']
        
        if 'parser' in kwargs and kwargs['parser'] is not None:
            self.commandParser = kwargs['parser']
        else:
            self.commandParser = self

        self.sentGreeting = False
        self.joinedChannel = False
        self.sendReady = False
        self.loop = True

    """
        Call this method to connect, authenticate, and start the read/eval loop
        As the name implies, this runs the bot.
    """
    def run(self):
        self.openSocket()
        self.login()
        # self.joinChannel(self.channel)
        self.message_loop()

    """
        This will stop the loop from running.
    """
    def stop():
        self.loop = False

    """
        Opens a socket, and wraps it with SSL
    """
    def openSocket(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((self.server, self.port))
        self.irc_socket = ssl.wrap_socket(self.socket)

    """
        Authenticates the bot to the server
        For a handy protocol reference, check out http://stackoverflow.com/a/2969441
    """
    def login(self, **kwargs):
        self.irc_socket.send("USER "+ self.nickname + " " + self.hostname + " " + self.server + " : " + self.name + "\n")
        self.irc_socket.send("NICK "+ self.nickname +"\n")

    """
        Sends the given message text to the current channel.
    """
    def sendMessage(self, message):
        self.irc_socket.send("PRIVMSG "+ self.channel +" :"+ message +"\n")

    """
        Send a message, but prefix it with the @username of the bot owner, so
        that they're notified.
    """
    def tellMaster(self, message):
        self.sendMessage('@' + self.master +': '+ message)

    """
        Joins the specified channel.
    """
    def joinChannel(self, channel):
        self.irc_socket.send("JOIN "+ channel +"\n")
        self.joinedChannel = True

    """
        As per the RFC, we need to respond with a PONG every time
        the server PINGs us.
    """
    def sendPong(self, str):
        ping, nonce = str.split(':')
        self.irc_socket.send("PONG :" + nonce + "\n")

    """
        The main loop, which retrieves any new messages and passes them to the parser.
        We only pass messages if they're not a PING or authentication error message.
        If no parser is supplied, then we print all messages recieved to stdout.
    """
    def message_loop(self):
        while self.loop is True:
          message = self.irc_socket.recv(2048)
          message = message.strip('\n\r')

          # Every time the server sends a PING, respond with a PONG (per the RFC)
          if message.find("PING") == 0:
            self.sendReady = True
            self.sendPong(message)
          
          if self.sendReady is True and self.joinedChannel is False:
            self.joinChannel(self.channel)

          # If we haven't sent the greeting yet, but we're ready to begin sending messages
          # Then we'll announce our presence to the current channel.
          if self.sentGreeting is False and self.sendReady is True:
              self.tellMaster(self.nickname +' has connected.')
              self.sentGreeting = True

          # Attempt to evaluate input, and catch any errors
          # If there's an error, we'll notify the channel instead of crashing.
          try:
              output = self.commandParser.parse(message) if self.sendReady is True else None
              if output is not None:
                  self.tellMaster(output)
          except Exception,e:
              self.tellMaster('Encountered an error while processing: `'+ message +'` _(got `'+ repr(e) +'`)_.')

    """
        If no parser is supplied, the controller will simply print every message it recieves.
    """
    def parse(self, message):
        print message

class MessageParser(object):
    def __init__(self, **kwargs):
        if 'config' in kwargs:
            if isinstance(kwargs['config'], dict):
                self.config = kwargs['config']
            else:
                with open(kwargs['config'], 'r') as cfg:
                    self.config = json.load(cfg)

        self.command_map = CommandMap(self.config)

        if 'nickname' in kwargs:
            self.nickname = kwargs['nickname']
        else:
            self.nickname = self.config['irc']['username']

    """
        The parse method, which is called by the message read/eval loop
        in the SlackIRCController class.
    """
    def parse(self, item):
        # Strip metadata from the message
        message = self.getMessage(item)
        meta = self.getMeta(item)

        # If we find our nickame in the message (e.g. we're being summoned)
        if self.checkForNick(message) and self.checkAuthorization(meta, message):
            # Strip our nickname from the message
            message = self.stripNick(message)
            # Strip any illegal characters from the message
            message = self.stripCharacters(message)
            # Compare the command sent against the configured list
            command = self.findCommand(message)
            if command is not None:
                # If we found it, then figure out what method to call
                method = self.findMethod(command)
                # Remove the command name from the message, leaving only the arguments
                args = self.stripCommand(command, message)
                # Call the appropriate method in the CommandMap class, and return
                # the response text it generates.
                return getattr(self.command_map, method)(args)
            else:
                return 'Couldn\'t find a command: `'+ message +'`'

    """
        Checks for either @nickname or nickname in the current message text.
    """
    def checkForNick(self, message):
        message = message.split(' ')
        return '@'+self.nickname in message or self.nickname in message

    """
        Checks message sender against authorized users
    """
    def checkAuthorization(self, meta, message):
        meta = self.getMeta(meta)
        authorized_users = self.config['authorized_users']
        authorized_users.append(self.config['master'])
        return meta[:meta.find('!')] in authorized_users

    """
        Strips the metadata from the latest message.

        Converts this:
            :nickname!nickname@<server> PRIVMSG <channel> : <message>
        to this:
            <message>
    """
    def getMessage(self, message):
        if message.find('!') < 0:
            return ""

        return message[message.find('PRIVMSG #cnc :')+14:]
        
    """
        Returns the metadata from the latest message.

        Converts this:
            :nickname!nickname@<server> PRIVMSG <channel> : <message>
        to this:
	        nickname!nickname@<server>
    """
    def getMeta(self, message):
        return message[message.find(':')+1:message.find(' ')] # Return everything between first and second colons

    """
        Removes any blacklisted characters from the message.
    """
    def stripCharacters(self, message):
        for char in self.config['character_blacklist']:
            message = message.replace(char, '')
        return message

    """
        All commands are prefixed with the bot's nickname, so we need to remove that
        so that we're left with only the command itself and the arguments to pass.
    """
    def stripNick(self, message):
        nick = '@'+self.nickname if '@'+self.nickname in message else self.nickname
        message = message[message.find(nick)+len(nick):] # Strip first occurrence of nick
        return message

    """
        Strips the command name from the message, which leaves us with the arguments to pass.
    """
    def stripCommand(self, command, message):
        message = message[message.find(command)+len(command)+1:] # Strip first occurrence of command name
        return message

    """
        The first string after our bot's nick in a message is the name of the command.
        So, we'll take that string and compare it against the configured list of valid
        commands.
    """
    def findCommand(self, message):
        message = message.split(' ')
        for word in message:
            if word in self.config['commands']:
                return word
        return None

    """
        If a command was found, then we'll need to know what method to call
        in the CommandMap class. Thankfully, this is defined in the config,
        so it's easy to look up.
    """
    def findMethod(self, message):
        message = message.split(' ')
        for word in message:
            if word in self.config['commands']:
                return self.config['commands'][word]['method']
        return None



class CommandMap(object):
    def __init__(self, config):
        self.config = config

    def sayHello(self, args):
        return 'Hello! ' + args

    def domainLookup(self, args):
        if any(c.isalpha() for c in args):
            ip = str(subprocess.check_output(["dig", "+short", args.replace(' ', '')])).strip('\n')
            return ip if any(c.isdigit() for c in ip) else 'No DNS records found for ' + args
        else:
            return '*dig:* No domain specified.'

    def getHostname(self, args):
        return str(subprocess.check_output(["hostname"])).strip('\n')

    def diskStatus(self, args):
        stat = str(subprocess.check_output(["df", "-h", "/"])).split('\n')
        return 'Disk Usage _[fs size used avail % mounted]_:  ' + stat[1]

    def getUptime(self, args):
        return str(subprocess.check_output(["uptime"])).strip('\n')

    def doReboot(self, args):
        msg = str(subprocess.check_output(["shutdown", "-r", "+2"])).strip('\n')
        return 'Reboot scheduled in 2 minutes. ' + msg

    def undoReboot(self, args):
        msg = str(subprocess.check_output(["shutdown", "-c"])).strip('\n')
        return 'Reboot cancelled! ' + msg

    def listCommands(self, args):
        commands = list()
        for key in self.config['commands']:
            commands.append(key)
        return 'Available commands are: ' + ', '.join(commands)

    def killClient(self, args):
        exit(0)


# -----------  MAIN -----------

with open('config.json', 'r') as cfg:
    config = json.load(cfg)

botname = config['irc']['username'] + str(random.randint(6,66)*100)

bot = IRCController(server=config['irc']['host'],
                           port=config['irc']['port'],
                           channel=config['irc']['channel'],
                           master=config['master'],
                           parser=MessageParser(config=config, nickname=botname),
                           username=botname)

# Runs the bot and handles/retries on connection errors,
# implementing an exponential backoff up to 256 seconds.
def retryLoop(func, sec):
    try:
        func()
    except socket.error:
        sec = sec+1 if sec < 8 else 1
        print 'Connection error, retrying in '+ str(2**sec) +' seconds...'
        time.sleep(2**sec)
        retryLoop(func, sec)

retryLoop(bot.run, 0)
