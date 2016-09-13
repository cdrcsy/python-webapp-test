#!/usr/bin/env python
# coding:utf-8

import hashlib

def md5():
    md5= hashlib.md5()
    md5.update('how to use md5 in python hashlib?'.encode('utf-8'))
    print(md5.hexdigest())



def mult_md5():

    mod= hashlib.md5()
    mod.update('how to use md5 in'.encode('utf-8'))
    mod.update('python hashlib?'.encode('utf-8'))
    print(mod.hexdigest())

if __name__=="__main__":
    md5()
    mult_md5()
