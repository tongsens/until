__author__ = 'root'

import sqlite3
from scapy.all import *
from collections import Counter

def count():
    cx = sqlite3.connect('domain.db')
    cu = cx.cursor()
    select_cmd = "SELECT domains FROM domains"
    cu.execute(select_cmd)
    res = cu.fetchall()
    cu.close()
    cx.close()
    count_dict = {}
    for data in res:
        if data[0] in count_dict.keys():
            count_dict[data[0]] += 1
        else:
            count_dict[data[0]] = 1
    result = sorted(count_dict.iteritems(), key=lambda dd:dd[1], reverse=True)
    for data in result:
        print data

class Search():
    def __init__(self):
        self.cx = sqlite3.connect('domain.db')
        self.cu = self.cx.cursor()

    def sel_url(self, dname):
        cmd = 'SELECT url FROM domains WHERE domains="%s"'%dname
        self.cu.execute(cmd)
        res = self.cu.fetchall()
        return [data[0] for data in res]

    def __del__(self):
        self.cu.close()
        self.cx.close()

def pingtest(iplist):
    count_s = 0
    count_f = 0
    s_list = []
    for ip in ip_list:
        try:
            ans,unans = sr(IP(dst=str(ip))/ICMP(), timeout=5)
            if len(ans)>0:
                count_s += 1
                s_list.append(str(ip))
            else:
                count_f += 1
        except Exception,e:
            count_f += 1
            print Exception,e
    rate = float(count_s)/float(count_s+count_f)
    print  rate
    return s_list

def dnstest(iplist):
    count_s = 0
    count_f = 0
    for ip in ip_list:
        try:
            sr(IP(dst=str(ip))/ICMP(), timeout=3)
            count_s += 1
        except Exception,e:
            print Exception,e
            count_f += 1
    rate = float(count_s)/float(count_f+count_s)
    print rate

def subdomain(iplist, dom):
    sub_list = []
    fat_list = []
    for ip in ip_list:
        src =  str(ip).split(dom)
        sub_list.append(src[0])
        fat_list.append(src[1])
    return sub_list,fat_list

class DomEntry():
    def __init__(self, dom):
        sel = Search()
        self.ip_list = sel.sel_url(dom)
        sub = '.'+ dom + '.'
        self.sublist, self.fatlist = self.subdomain(self.ip_list, sub)

    def subdomain(self, iplist, dom):
        sub_list = []
        fat_list = []
        for ip in iplist:
            src =  str(ip).split(dom)
            try:
                if len(src)==1:
                    fat_list.append(src[0])
                else:
                    sub_list.append(src[0])
                    fat_list.append(src[1])
            except Exception,e:
                print Exception,e
        return sub_list,fat_list

    def getfat(self):
        print set(self.fatlist)

    def entroy(self):
        ent_list = []
        for data in self.sublist:
            p, lns = Counter(data), float(len(data))
            ent_value =  -sum(count/lns*math.log(count/lns, 2) for count in p.values())
            #print data, ent_value
            ent_list.append(ent_value)
        print sum(val for val in ent_list)/len(ent_list)

    def entroy2(self):
        strs = ""
        for data in self.sublist:
            strs += data
        p, lns = Counter(strs), float(len(strs))
        ent_value =  -sum(count/lns*math.log(count/lns, 2) for count in p.values())
        return ent_value

    def printsub(self):
        for data in self.sublist:
            print data

if __name__ == '__main__':
    doment = DomEntry('360')
    doment.printsub()