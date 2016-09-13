#!/usr/bin/env python
# coding:utf-8

import socket

conn=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
conn.connect(('www.baidu.com',80))
conn.send('GET / HTTP/1.1\r\nHost:www.baidu.com\r\nConnection:close\r\n\r\n')

buffer=[]
while True:
    d=conn.recv(1024)
    if d:
        buffer.append(d)
    else:
        break


data=''.join(buffer)
conn.close()

header,html=data.split('\r\n\r\n',1)
print header

with open(r"C:\Users\Administrator\Desktop\baidu.html",'wb') as f:
    f.write(html)




