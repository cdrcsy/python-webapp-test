#!/usr/bin/env python
#coding:utf-8

from __future__ import with_statement  
import ConfigParser  
config=ConfigParser.ConfigParser()  
with open("test.cfg","rw") as cfgfile:  
    config.read(cfgfile)  
    name=config.get("info","name")  
    age=config.get("info","age")  
    print name  
    print age  
    config.set("info","sex","girl")  
    config.set("info","age","55")  
    age=config.getint("info","age")
    sex=config.get("info","sex") 
    print name  
    print type(age)
    print age  
    print sex

