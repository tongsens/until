__author__ = 'root'

import sys,PIL.Image as Image
import os


def issex(filename):
    img = Image.open(filename).convert('YCbCr')
    w,h = img.size
    data = img.getdata()
    cnt = 0
    for i, ycbcr in enumerate(data):
        y,cb,cr = ycbcr
        if 86<= cb <= 117 and 140<= cr<=168:
            cnt+=1
    if cnt>w*h*0.3:
        return True
    else:
        return False

def dirimg(filepath):
    imglist = os.listdir(filepath)
    for img in imglist:
        filename = os.path.join(filepath, img)
        if issex(filename):
            cmd = "mv %s /mnt/result"%filename
            print cmd
            os.system(cmd)


if __name__ == '__main__':
    path = '/mnt/qingqu'
    dirimg(path)