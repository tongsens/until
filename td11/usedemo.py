__author__ = 'root'

import urllib2
import cookielib

def proxytest():
    url = 'http://www.freebuf.com'
    proxy = urllib2.ProxyHandler({'http':'127.0.0.1:8080'})
    opener = urllib2.build_opener()
    opener.add_handler(proxy)
    opener.addheaders = [('User-agent', 'Mozilla/5.0 (X11; Linux i686; rv:31.0) Gecko/20100101 Firefox/31.0 Iceweasel/31.8.0'),('Accept','*/*'),\
                         ('Accept-Language','en-US,en;q=0.5'),('Accept-Encoding','gzip, deflate'),('Referer','http://www.freebuf.com/'),\
                         ('Cookie','aliyungf_tc=AQAAAN98lnN0ZgQAGSZWbvsMe9y9PfJv; 3cb185a485c81b23211eb80b75a406fd=1480643370; Hm_lvt_cc53db168808048541c6735ce30421f5=1480643331; Hm_lpvt_cc53db168808048541c6735ce30421f5=1480647117'),\
                         ('Connection','keep-alive')]
    #cookie = cookielib.CookieJar()
    #opener.add_handler(urllib2.HTTPCookieProcessor(cookie))
    response = opener.open(url)
    print response.info()


def test():
    handler = urllib2.FTPHandler()


if __name__ == '__main__':
    proxytest()