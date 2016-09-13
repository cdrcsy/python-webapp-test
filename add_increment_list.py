#!/usr/bin/env python
# coding:utf-8

"""
#实现类似这样的序列：
0M-5M=0
5M-10M=1
10M-15M=2
15M-20M=3
20M-25M=4
25M-30M=5
30M-35M=6
35M-40M=7
40M-45M=8
45M-50M=9
50M-55M=10
55M-60M=11
60M-65M=12
65M-70M=13
70M-75M=14
75M-80M=15
80M-85M=16
85M-90M=17
90M-95M=18
95M-100M=19
100M-105M=20
105M-110M=21
110M-115M=22
115M-120M=23    这里结束，下面从0开始。基线
120M-125M=0
125M-130M=1
130M-135M=2
"""

import os

def add_list(start,stop,step,node):
    for i in range(start,stop,step):
        x=i+step
        y=(x/5-1)%node
        print "%sM-%sM=%s" %(i,x,str(y))

if __name__=="__main__":
    add_list(0,2000,5,24)


#for x in range(1, (x/5-1)%24): print "%dM-%dM=%d" % ((x-1)*5, x*5, x % 24)

