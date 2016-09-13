#!/usr/bin/env python
# coding:utf-8

from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random


def RandChar():
    return chr(random.randint(65, 90))

def RandColor():
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))

def RandColor2():
    return (random.randint(32,127),random.randint(32,127), random.randint(32,127))

width=60*4
height=60

image=Image.new('RGB',(width,height),(255,255,255))

font=ImageFont.truetype('/usr/share/fonts/default',36)

draw=ImageDraw.Draw(image)

for w in range(width):
    for h in range(height):
        draw.point((w,h),fill=RandColor())

for t in range(4):
    draw.text((60*t+10,10),RandChar(),font=font,fill=RandColor2())

image=image.filter(ImageFilter.BLUR)
image.save('./db/code.jpg','jpeg')

