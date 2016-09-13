#! /usr/bin/env python
#coding:utf-8

num=int(raw_input('please input your guess number(1-100):'))

if 0<= num < 88:
    print "your number:%d "%num
    print "number less than XX"
elif num == 88:
    print "your number:%d "%num
    print "yes,your guess right,it's 88."
elif 88 < num <=100:
    print "your number:%d "%num
    print "number more than XX "
else:
    print " Are you a human?"
