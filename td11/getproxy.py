__author__ = 'root'
import urllib2

def getiplist():
    url = 'http://api.xicidaili.com/free2016.txt'
    buf = urllib2.urlopen(url).read()
    return buf.split('\r\n')

def proxytest(proxylist):
    url = 'http://pv.sohu.com/cityjson'
    for ip in proxylist:
        proxy = urllib2.ProxyHandler({'http':ip})
        opener = urllib2.build_opener(proxy)
        try:
            response = opener.open(url, timeout=5)
            print response.read()
            print ip
        except:
            print 'err',ip


if __name__ == '__main__':
    proxylist = getiplist()
    proxytest(proxylist)