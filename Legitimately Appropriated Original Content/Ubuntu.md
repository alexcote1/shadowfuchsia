# Ubuntu 16.04

### Jenkins

#### Installation

First add the repository key to the system:
```
$	wget -q -O - https://pkg.jenkins.io/debian/jenkins-ci.org.key | sudo apt-key add -
```

append the Debina package repository to `sources.list`:

```
$	echo deb https://pkg.jenkins.io/debian-stable binary/ | sudo tee /etc/apt/sources.list.d/jenkins.list
```

next just update, then you can install Jenkins:
```
$	sudo apt-get update
$	sudo apt-get install jenkins
```

Next we can start and enable the service:
```
$	sudo systemctl start jenkins
$	sudo systemctl enable jenkins
```

Next you should be able to access the Jenkins server using a web server to go to (assuming the server's ip is 192.168.1.50) `192.168.1.50:8080`. To verify that you are the apporces sysadmin, it will ask you for an inital password stored here:

```
#	cat /var/lib/jenkins/secrets/initialAdminPassword 
```

after that the process is pretty much all GUI.

#### Administration

To change passwords, and user settings for the user `guyinatuxedo`:
```
People>guyinatuxedo>Configure>
```

To configure the security settings, such as the security realm (LDAP, local authentication, it's own users) and the permissions for it's user (what anonymous/authenticated users can do). Also make sure `Prevent Cross Site Request Forgery exploits` is checked:
```
Manage Jenkins>Configure Global Security>
```

### Firewall

for IPv4
```
$	sudo iptables -A INPUT -p tcp --dport 8080 -j ACCEPT
$	sudo iptables -A INPUT -p tcp --dport 22 -j ACCEPT
$	sudo iptables -A INPUT -p icmp -j ACCEPT
$	sudo iptables -A OUTPUT -p tcp --sport 8080 -j ACCEPT
$	sudo iptables -A OUTPUT -p tcp --sport 22 -j ACCEPT
$	sudo iptables -A OUTPUT -p icmp -j ACCEPT
$	sudo iptables -P INPUT DROP
$	sudo iptables -P OUTPUT DROP
$	sudo iptables -P FORWARD DROP
```

for IPv6:
```
$	sudo ip6tables -F
$	sudo ip6tables -P INPUT DROP
$	sudo ip6tables -P OUTPUT DROP
$	sudo ip6tables -P FORWARD DROP
```

and to save the rules:
```
$	sudo iptables-save > /etc/iptables/rules.v4 
$	sudo ip6tables-save > /etc/iptables/rules.v6 
```

