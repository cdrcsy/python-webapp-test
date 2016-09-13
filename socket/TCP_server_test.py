#!/usr/bin/env python
# coding:utf-8

import socket
import threading
import datetime,time

conn=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
conn.bind(('0.0.0.0',9000))
conn.listen(5)
print ('waiting for connection...')

def tcplink(sock,addr):
    now=datetime.datetime.now()
    print ('%s')%now+(' Accept new connection from %s:%s')%addr
    sock.send('Welcome!')
    while True:
        data=sock.recv(1024)
        time.sleep(1)
        if data == 'exit' or not data:
            break
        else:
            sock.send('Hello,%s !'%data)
    sock.close()
    now=datetime.datetime.now()
    print ('%s')%now+(' Connection from %s:%s closed')%addr

while True:
    sock,addr=conn.accept()
    t=threading.Thread(target=tcplink,args=(sock,addr))
    t.start()



