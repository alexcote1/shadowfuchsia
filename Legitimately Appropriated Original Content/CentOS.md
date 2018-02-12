# Centos

```
https://www.howtoforge.com/tutorial/how-to-install-elastic-stack-on-centos-7/
```

### Password

Change password:
```
#	passwd
```

### Elasticsearch

#### Installation

first install java:

```
#	yum install java-1.8.0-openjdk.x86_64
```

confirm that you have the right version:
```
#	java -version
```

Next install wget
```
#	yum install wget
```

Next we will download the rmp file for elasticsearch (probably is a newer version available):

```
#	wget https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-6.1.3.rpm
```

install the it using rpm:
```
#	rmp -ivh elasticsearch-6.1.3.noarch.rpm
```

then start and enable the service:

```
#	systemctl start elasticsearch.service
#	systemctl enable elasticsearch.service
```

#### Editing Config Files

Next yu will need to edit the file `/etc/elasticsearch/elasticsearch.yml`, and add the following configurations (I did it to the end): 

Specify the name of this node, and the cluster.
```
node.name: "ice"
cluster.name: tundra
```

Specify if this node is a master, or a slave (default master):
```
node.master: true
```
Specify if this node will store data (default true):
```
node.data: true
```

Next specify the number of shards (how many pieces the index will be split into), and the number of replicas (how many copies of the index accross the cluster):
```
index.number_of_shards: 1
index.number_of_replicas: 0
```
Next you can sepcify where the index is stored. The default location is `/var/lib/elasticsearch/tundra/`. For the directory, it must contain the folder `nodes`, and the permission should be 755, and the owner and group should be `elasticsearch`

```
path.data: /cold
```

Next we need to deal with the fact that Elasticsearch doesn't have any built-in security, or authentication. We can deal with that by specfying that it should only bind to localhost.

```
network.bind_host: localhost
```

Next we will need to disable dynamic scripts, which will allow for custom expressions, which opens up an entirely new attack surface.

```
script.disable_dynamic: true
```

#### Using Elasticsearch

To insert data into the `winter` index, with the `warning` type, with the id of `1`.

```
#	curl -X GET 'http://localhost:9200/winter/warning/1' -d '{ "message": "Hello World!"}'
```

To view the data in the the `winter` index, with the `warning` type, with the id of `1`.

```
#	curl -X GET 'http://localhost:9200/winter/warning/1'
```

output will look something like this (this output is from a different select, so the output is different):

```
{"_index":"tutorial","_type":"helloworld","_id":"1","_version":1,"found":true,"_source":{ "message": "Hello World!" }}
```

To edit an existing entry:
```
#	curl -X PUT 'localhpst:9200/winter/warning/1?pretty' -d '
< 	{
> "message": "Hail to the King!"
> }'
```

the output looks like this:
```
{
 "_index" : "winter",
 "_type" : "warning",
 "_id" :  "1",
 "_version"  : 2,
 "created" : false
} 
```

### Kibana & Nginx

#### Installation

First download the Kibana rpm and install Kibana:

```
#	wget https://artifacts.elastic.co/downloads/kibana/kibana-5.1.1-x86_64.rpm
#	rpm -ivh kibana-5.1.1-x86_64.rpm
```

next edit the Kibana config file:
```
#	vim /etc/kibana/kibana.yml
```

add the following configurations to the end:
```
server.port: 5601
server.host: "localhost"
elasticsearch.url: "http://localhost:9200"
```

then start and enable the kibana 

```
#	systemctl start kibana
# systemctl enable kibana
```

Next install epel and Nginx:
```
#	yum -y install epel-release
#	yum -y install nginx httpd-tools
```

next edit the main nginx config file:
```
#	vim /etc/nginx/nginx.conf
```

In that file, you want to edit out the server block (for me it was lines 39-58). Also make sure it says `include /etc/nginx/conf.d/elk.conf`. I also commented out the `include /etc/nginx/conf.d/*.conf`:


next add the following nginx config file:

```
#	vim /etc/nginx/conf.d/elk.conf
```

add the following configuration:

```
server {
    listen 80;
 
    server_name elk-stack.co;
 
    auth_basic "Restricted Access";
    auth_basic_user_file /etc/nginx/.kibana-user;
 
    location / {
        proxy_pass http://localhost:5601;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection 'upgrade';
        proxy_set_header Host $host;
        proxy_cache_bypass $http_upgrade;
    }
}
```

next make a password for that site:
```
#	sudo htpasswd -c /etc/nginx/.kibana-user admin
```

Then finally check the nginx conf, start, and enable the daemon:
```
#	nginx -t
# systemctl enable nginx
# systemctl start nginx
```


### Networking issue

I expereince an issue where Centos would not automatically get a DHCP address. To manually grab an address:
```
#	dhclient -v
```

Then create the following file to have the fix persist through reboots startup named `/etc/init.d/net-autostart`:

```
#!/bin/bash
# Solution for "No Internet Connection from VMware"
#
### BEGIN INIT INFO
# Default-Start: 2 3 4 5
# Default-Stop: 0 1 6
### END INIT INFO
dhclient -v
```

make the file executable
```
#	chmod 755 /etc/init.d/net-autostart
```

add the file to auto-start
```
#	chkconfig --add /etc/init.d/net-autostart
```