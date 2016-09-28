__author__ = 'root'

import os
import zipfile
import time

def readconf():
    fpath = file('config','r').read().split('\n')
    return fpath[0], fpath[1]

def isempty(filepath):
    if not os.listdir(filepath):
        return True
    else:
        return False

def upzip(filename, savepath):
    with zipfile.ZipFile(filename, "r") as fp:
        try:
            fp.extractall(path=savepath)
        except:
            print "extract %s faile"%filename

def mainloop(zippath, savapath):
    for i in range(0,780):
        while True:
            if isempty(savepath):
                break
            else:
                print "directory not empty"
            time.sleep(30)
        filename = 'trojan%d.zip'%i
        filepath = os.path.join(zippath, filename)
        try:
            upzip(filepath, savepath)
        except:
            with open('log.txt', "a") as fp:
                fp.write(filename)


if __name__ == '__main__':
    zippath, savepath = readconf()
    mainloop(zippath, savepath)
