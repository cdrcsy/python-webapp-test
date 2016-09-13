#!/usr/bin/env python
#coding:utf-8

import os
import subprocess
import multiprocessing
import time,random

def fork_process():
    print ('Precess (%s) start .....' % os.getpid())
    pid=os.fork()

    if pid == 0 :
        print ('I am child process (%s) and my parent is %s.'%(os.getpid(),os.getppid()))
    else:
        print ('I (%s) just created a child process (%s).' % (os.getpid(),pid))

def lookup_www():

    print ("$ nslookup www.python.org")
    r=subprocess.call(['nslookup','www.python.org'])
    print ('Exit code:',r)


def subsub_proc():
    print('$ nslookup')
    p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, err = p.communicate(b'set q=mx\npython.org\nexit\n')
    print(output.decode('utf-8'))
    print('Exit code:', p.returncode)


def read(q):
    while True:
        try:
            value=q.get()
            print ("get %s from queue." %value)
            time.sleep(random.random())
        finally:
            q.task_done()

def main():
    q=multiprocessing.JoinableQueue()
    pw1=multiprocessing.Process(target=read,args=(q,))
    pw2=multiprocessing.Process(target=read,args=(q,))
    pw1.daemon=True
    pw2.daemon=True
    pw1.start()
    pw2.start()
    for c in [chr(ord('A')+i) for i in range(26)]:
        q.put(c)
    try:
        q.join()
    except KeyboardInterrupt:
        print ('stopped by hand')

if __name__=="__main__":
    main()
    subsub_proc()

