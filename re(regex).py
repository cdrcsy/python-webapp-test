#!/usr/bin/env python
# coding:utf-8

"""
regex正则表达式常用练习，re模块练习。
"""

import re

# 判断用户输入是否全是数字？
# test = raw_input("please input your number:")

def match_num(test):
    if re.match(r'^[0-9][0-9]$', test):
        """
        if re.match(r'^[0-9]+[0-9]$', test):也可以的
        """
        print True
    else:
        print False

# 判断用户输入是否全是字母？
def match_str(test):
    if re.match(r'^[a-zA-Z]+[a-zA-Z]$', test):
        """
        if re.match(r'^[a-zA-Z][a-zA-Z]$', test):是不可以的,中间需要使用+连接
        """
        print True
    else:
        print False

# 判断用户输入是否有除数字，字母和下划线的特殊字符？

def match_num_str(test):
    if re.match(r'^[0-9a-zA-Z\_]+[0-9a-zA-Z\_]$', test):
        print True
    else:
        print False

#[a-zA-Z]|[0-9]|[\_]等价于上面




if __name__=="__main__":
    s=match_num("abc123_09")
    #ff=match_str("124abcd_")
    #gg=match_num_str("123THn_=@")
