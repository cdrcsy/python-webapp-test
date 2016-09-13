#!/usr/bin/env python
# coding:utf-8

import socket
import threading
import datetime,time

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(('0.0.0.0',9009))
print 'Bind UDP on 9009...'

"""
while True:
    data, addr = s.recvfrom(1024)
    print ("Received from %s:%s" %addr)
    s.sendto('hello,%s !' % data, addr)
"""


def tcplink(sock,addr):
    now=datetime.datetime.now()
    print ('%s')%now+(" Received from %s:%s" %addr)
    sock.sendto('Welcome!')
    while True:
        data=sock.recvfrom(1024)
        time.sleep(1)
        if data == 'exit' or not data:
            break
        else:
            sock.sendto('Hello,%s !'%data)
    sock.close()
    now=datetime.datetime.now()
    print ('%s')%now+(' transfer data with %s:%s over')%addr

while True:
    sock,addr=s.recvfrom(1024)
    t=threading.Thread(target=tcplink,args=(sock,addr))
    t.start()
