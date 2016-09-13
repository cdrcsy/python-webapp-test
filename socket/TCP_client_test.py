#!/usr/bin/env python
# coding:utf-8

import socket

conn=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
conn.connect(('192.168.1.165',9000))
print conn.recv(1024)

for data in ['Michael','Tracy','Sarah']:
    conn.send(data)
    print conn.recv(1024)

conn.send('exit')
conn.close()



