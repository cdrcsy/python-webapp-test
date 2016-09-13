#!/usr/bin/env python
# coding:utf-8

def application(environ,start_response):
    start_response('200 OK',[('Content_type','text/html')])
    return '<h1>Hello,%s!</h1>' % (environ['PATH_INFO'][1:] or 'web')

#http://192.168.1.165:8000/maycn    会获取到maycn，返回：Hello,maycn!
#http://192.168.1.165:8000          没有内容供获取，返回：Hello，web!