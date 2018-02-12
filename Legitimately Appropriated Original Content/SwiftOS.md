# SwiftOS 

### Password

To change the password:
```
$	sudo passwd
```

To elevate to root:

```
$	sudo su
```

to

### Sources

I needed to configure the sources list located at `/etc/apt/sources.list`. I edited this with the gui editor `geany`. I used the sources.list from `https://gist.github.com/SimonPe/1034723`, and only used the sources related to `wheezy`, since that is what Swift is based off of. These are the sources I used (rest is commented out):

```
deb http://ftp.nl.debian.org/debian/ wheezy main contrib non-free
deb http://ftp.be.debian.org/debian/ wheezy main contrib non-free
deb-src http://ftp.nl.debian.org/debian/ wheezy main contrib non-free
deb-src http://ftp.be.debian.org/debian/ wheezy main contrib non-free

deb http://www.debian-multimedia.org wheezy main non-free
deb-src http://www.debian-multimedia.org wheezy main non-free
```

after that, we can install vim and update:

```
$	sudo apt-get update
$	sudo apt-get install vim
```


### Installing Jenkins

Install this dependency

```
$	sudo apt-get install default-jre-headless
```

