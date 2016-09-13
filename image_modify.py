#!/usr/bin/env python
# coding:utf-8

from __future__ import print_function
from PIL import Image,ImageFilter
import os,sys

#图片缩放函数
"""
学习模式
def image_size_modify():
    im=Image.open("C:\Users\Administrator\Desktop/icat.jpg")
    print (im.format,im.size,im.mode)   #打印图片属性
    im.show()   #打开图片（window使用图片查看其，linux使用xv)
    w,h=im.size
    im.thumbnail((w//3,h//3))
    im.save("C:\Users\Administrator\Desktop/scat.jpg",'jpeg')
"""
#自动将用户上传图片格式化到指定大小，方法一。
def image_size_modify():
    for infile in sys.argv[1:]:
        im=Image.open(infile)
        print (im.format,im.size,im.mode)
        w,h=im.size
        if w!=300 or h!=200:
            try:
                im.thumbnail((300,200))
                im.save(infile)     #会将原图片覆盖。
            except IOError,e:
                print(e)

#自动将用户上传图片格式化到指定大小，方法二。
def image_size_change():
    size=(300,200)
    for infile in sys.argv[1:]:
        outfile=os.path.splitext(infile)[0]+".thumbnail"
        if outfile != infile:
            try:
                im=Image.open(infile)
                im.thumbnail(size)
                im.save(outfile,"JPEG")
            except IOError:
                print("cannot create thumbnail for",infile)
"""
注意：
im.save(infile)直接会覆盖原图片，如果需要保留原图并重命名,使用方法2，

linux下，使用方法：
python image_modify.py ./db/icat.jpg ./db/icat.png
或者：
python image_modify.py ./db/*.jpg
"""


#将图片格式转换为png格式。
def image_change_format():
    for infile in sys.argv[1:]:
        f,e=os.path.splitext(infile)
        outfile=f+".png"
        if infile != outfile:
            try:
                Image.open(infile).save(outfile)
            except IOError,e:
                print(e)
"""
linux下，使用方法：
python image_modify.py ./db/icat.jpg ./db/icat.png
或者：
python image_modify.py ./db/*.jpg

"""


if __name__=="__main__":
    image_change_format()
    #image_size_modify()


