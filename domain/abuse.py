__author__ = 'root'

import sqlite3
import urllib2
from scapy.all import *
import time
import scrapy
import os

def read_db():
    cx = sqlite3.connect('domain.db')
    cu = cx.cursor()
    select_cmd = "SELECT * FROM domains"
    cu.execute(select_cmd)
    res = cu.fetchall()
    return res

def parseip(url):
    try:
        ans,unans = sr(IP(dst=str(url))/ICMP(), timeout=3)
            #ip = ans.res[0][0].dst
        return True
    except Exception,e:
        print url,e
        return e

def at_abuse(url):
    blocked = 100
    try:
        ck_url = "http://www.anti-abuse.org/multi-rbl-check-results/?host=%s"%url
        urllib2.urlopen(ck_url)
        time.sleep(5)
        res_url = "http://www.anti-abuse.org/rbl-results/?host=%s"%url
        response2 = urllib2.urlopen(res_url)
        data = response2.read()
        sel = scrapy.selector.Selector(text=data)
        blocked = len(sel.xpath('//li[@class="blocked rbl"]'))
    except Exception,e:
        print Exception,e
    return blocked


class DbSave():
    def __init__(self):
        self.cx = sqlite3.connect('url.db')
        self.cu = self.cx.cursor()
        self.dbInit()

    def dbInit(self):
        try:
            create_table = "CREATE TABLE IF NOT EXISTS urls (url TEXT UNIQUE , domains TEXT, class TEXT, descs TEXT)"
            self.cu.execute(create_table)
            self.cx.commit()
        except Exception,e:
            print e

    def insert(self, data):
        try:
            insert_cmd = 'INSERT INTO urls(url, domains, class, descs) VALUES ("%s", "%s","%s","%s")'%data
            self.cu.execute(insert_cmd)
            self.cx.commit()
        except Exception,e:
            print e


def main():
    url_list = read_db()
    dbsave = DbSave()
    for data in url_list:
        url, domain, clss = data
        isip = parseip(str(url))
        if isip==True:
            abus = at_abuse(str(url))
            count = 0
            while abus==100:
                time.sleep(15)
                abus = at_abuse(str(url))
                print "please wait..."
                count += 1
                if count>3:
                    break
            desc = str(abus)
        else:
            desc = isip
        dbsave.insert((url, domain,clss, desc))

def whois(url):
    cmd = "whois %s"%url
    t = os.popen(cmd)
    print t.read()

def test():
    url = "baidu.com"
    whois(url)

if __name__ == '__main__':
    test()
    #main()

