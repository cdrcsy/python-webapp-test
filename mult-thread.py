#!/usr/bin/env python
# coding:utf-8

import time, threading


#验证，多线程修改共享变量，锁的作用。
balance = 0
lock=threading.Lock()

def change_it(n):
    # 先存后取，结果应该为0:
    global balance
    balance = balance + n
    balance = balance - n

def run_thread(n):
    for i in range(100000):
        #计算前，先必须获取锁。
        lock.acquire()
        try:
            change_it(n)
        finally:
            #修改完毕之后，确保锁释放。
            lock.release()

t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)


def loop():
    print ('thread %s is running . . .'% threading.current_thread().name)
    n=0
    while n<5:
        n+=1
        print ('thread %s >>>> %s' % (threading.current_thread().name,n))
        time.sleep(1)
    print('thread %s is running . . .' % threading.current_thread().name)

print ('thread %s is running . . .' % threading.current_thread().name)
#t=threading.Thread(target=loop,name='loopthread')
t=threading.Thread(target=loop)
t.start()
t.join()
print('thread %s ended.' % threading.current_thread().name)

#
local_school=threading.local()

def process_student():
    std=local_school.student
    print('hello,%s(in %s)'%(std,threading.current_thread().name))

def process_thread(name):
    local_school.student=name
    process_student()

t5=threading.Thread(target=process_thread,args=('Alice'),name='Thread-A')
t6=threading.Thread(target=process_thread,args=('Bob'),name='Thread-B')

t5.start()
t6.start()
t5.join()
t6.join()

