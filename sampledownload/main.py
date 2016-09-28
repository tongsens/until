__author__ = 'root'

import urllib2
import ssl
import os
import time

def readconf():
    fpath = file('samplepath.conf','r').read().split('\n')
    return fpath[0], fpath[1]

def download(i, savepath):
    url_pat = "https://110.86.5.93:8443/laboratory/downloadZip.html?trojanType=72&remark=virus&currentPage=%d"
    url = url_pat%i
    print url
    filename = 'trojan%d.zip'%i
    targetpath = os.path.join(savepath, filename)
    try:
        f = urllib2.urlopen(url)
        data = f.read()
        with open(targetpath, "wb") as fp:
            fp.write(data)
    except:
        print "get file %d failed"%i
        with open('log.txt', "a") as fp:
            buf = str(i) + '\n'
            fp.write(buf)

def downloop(downpath):
    for i in range(0, 800):
        download(i, downapth)
        time.sleep(5)

if __name__ == '__main__':
    if hasattr(ssl, '_create_unverified_context'):
        ssl._create_default_https_context = ssl._create_unverified_context
    downapth, samplepaht = readconf()
    downloop(downapth)
