#!/usr/bin/env python
# coding:utf-8

import hashlib

sha1=hashlib.sha1()
sha1.update('how to use sha1 in'.encode('utf-8'))
sha1.update('python hashlib?')
print(sha1.hexdigest)