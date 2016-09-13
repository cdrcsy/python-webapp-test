#!/usr/bin/env python
# coding:utf-8

#导入wsgiref模块simple_server
from wsgiref.simple_server import make_server
#导入我们自己写的函数（要与server在同一个目录）
from Hello_dynamic import application

#定义服务，端口
httpd = make_server('',8000,application)

print "Serving HTTP on port 8000 ....."
#监听
httpd.serve_forever()

