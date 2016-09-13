#!/usr/bin/env python
# coding:utf-8

import socket

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
for data in ['Michael','Tracy','Sarah']:
    s.sendto(data,('192.168.1.165',9009))
    print s.recv(1024)
s.close()


