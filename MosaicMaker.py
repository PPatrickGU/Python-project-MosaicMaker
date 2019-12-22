#!/usr/bin/env python
# -*- coding:utf-8 -*-

from PIL import Image
from PIL import ImageDraw   #调用PIL库里的Image和ImageDraw函数来对图片处理
import os

scale = 10
image = Image.open('F://MM.jpg')   #打开需要进行填充的图片

#把图片变为原来的8倍大，为了方面进行切分
w = 8*image.width    #/scale
h = 8*image.height   #/scale
image = image.resize((w, h), Image.ANTIALIAS)
mywidth = w                   #设定长宽高
myheight = h

#做一张rgb画布
ib = Image.new('RGB', (w, h))
colors = []
i = j = 0
imgdraw = ImageDraw.Draw(ib)

while ( i < w ):
    j = 0
    while( j < h ):
        c = image.getpixel((i, j))
        colors.append(c)
        imgdraw.rectangle(((i, j), (i+scale, j+scale)), fill=c)  #20个像素为基本单位，进行颜色分析
        j += scale
    i += scale
#把原图的颜色信息分块存入color数组内

allimages = []
allimagespath = []
smallscale = scale  #小图尺寸

#在图库里，对图片进行大小调整
for file in os.listdir('F://image1'): #图库
    im = Image.open('F://image1/' + file)
    im = im.resize((smallscale, smallscale), Image.ANTIALIAS)  #图库里的图片修改尺寸
    allimages.append(im)
    allimagespath.append('F://image1/'+file)

allcolors = []

#在图库里，求得每一张修改完大小的图片的平均rgb信息
for f in allimages:
    w = f.width
    h = f.height
    i = 0
    ar = ab = ag = 0
    c = 0
    while (i < w):
        j = 0
        while (j < h):
            r, g, b = f.getpixel((i, j))
            ar += r
            ab += b
            ag += g
            j += 1
        i += 1
    ar /= (w*h)
    ab /= (w*h)
    ag /= (w*h)
    x = (ar, ag, ab)
    allcolors.append(x)    #得到每张图片的平均rgb信息

mypixel = []
counter = 0

for i in colors:
    r, g, b=i
    mind = 1000
    mini = 0 #符合条件的图的序号
    innercounter = 0
    for j in allcolors:
        r1, g1, b1=j
        x = abs(r-r1)
        y = abs(g-g1)
        z = abs(b-b1)
        x = (x+y+z)/3
        if ( x < mind ):
            mind = x
            mini = innercounter
        innercounter += 1
    mypixel.append(mini)
    z += 1
    counter += 1

k = 0
i = 0

while (i < my width):
    j = 0
    while (j < myheight):
        image.paste(allimages[mypixel[k]], (i, j))
        k += 1
        j += scale
        #print(allimages[mypixel[k]])
    i += scale

image

image.save('F://BB.jpg')


