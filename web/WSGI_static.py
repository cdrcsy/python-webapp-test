#!/usr/bin/env python
# coding:utf-8

def application(environ,start_response):
    start_response('200 OK',[('Content_type','text/html')])
    return '<h1>Hello,web!</h1>'

