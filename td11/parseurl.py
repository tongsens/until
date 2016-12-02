__author__ = 'root'
import urllib2

'''
GET /LoadData/Chatroom.ashx?type=guid&accounts=RC63069 HTTP/1.1
Host: td111.net
User-Agent: Mozilla/5.0 (X11; Linux i686; rv:31.0) Gecko/20100101 Firefox/31.0 Iceweasel/31.8.0
Accept: text/plain, */*; q=0.01
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
X-Requested-With: XMLHttpRequest
Referer: http://td111.net/Chatroom/ChatroomList.aspx
Cookie: Hm_lvt_9521d64fb73c01325f264686ceb4dcbb=1480562401,1480646748; say=gewq2110.86.38.25; ASP.NET_SessionId=ye3a5sbcgaee3focpveuhch5; userlanguage111=no; Hm_lpvt_9521d64fb73c01325f264686ceb4dcbb=1480647617; icwN2=0; StarLevel=0; xxx=0c68fc6b-d8f2-475d-b0c6-4686cd7a0d0c; yyy=86b9b9e55165d9792b86ae13f8d2c66b; samepc=0
Connection: keep-alive

http://www.kimo22.com/newnew/client.php?osite=C2@8dgo&roomid=7676&fmode=1&uid=kimooo@8dgo&pwd=3b0ebe405ac1495365291ace9236b0c5&nick=davic&loc=cn&cip=MTEwLjg2LjM4LjI1LDhkZ29jbixDMg==&custxml=http%3A%2F%2Fwww.kimo22.com%2Fskin%2F&lgu=http%3A%2F%2Fwww.kimo22.com%2F&jmu=http%3A%2F%2Fwww.kimo22.com%2Fregister.php&bpu=http%3A%2F%2Fwww.kimo22.com%2Fbuy_point_kind.php
'''




def getpwd(uid):
    url = 'http://td111.net/LoadData/Chatroom.ashx?type=guid&accounts=%s'%uid
    proxy = urllib2.ProxyHandler({'http':'127.0.0.1:8080'})
    opener = urllib2.build_opener()
    opener.add_handler(proxy)
    opener.addheaders = [('User-Agent','Mozilla/5.0 (X11; Linux i686; rv:31.0) Gecko/20100101 Firefox/31.0 Iceweasel/31.8.0'),\
                         ('Accept','text/plain, */*; q=0.01'),\
                         ('Accept-Language','en-US,en;q=0.5'),\
                         ('Accept-Encoding', 'gzip, deflate'),\
                         ('X-Requested-With','XMLHttpRequest'),\
                         ('Referer','http://td111.net/Chatroom/ChatroomList.aspx'),\
                         ('Cookie', 'Hm_lvt_9521d64fb73c01325f264686ceb4dcbb=1480562401,1480646748; say=gewq2110.86.38.25; ASP.NET_SessionId=ye3a5sbcgaee3focpveuhch5; userlanguage111=no; Hm_lpvt_9521d64fb73c01325f264686ceb4dcbb=1480647617; icwN2=0; StarLevel=0; xxx=0c68fc6b-d8f2-475d-b0c6-4686cd7a0d0c; yyy=86b9b9e55165d9792b86ae13f8d2c66b; samepc=0'),\
                         ('Connection','keep-alive')]
    response = opener.open(url)
    return response.read()

def geturl(rooid, uid, pwd):
    url = 'http://www.kimo22.com/newnew/client.php?osite=C2@8dgo&roomid=%s&fmode=0&uid=%s-26@cq11&pwd=%s&nick=davic&loc=cn&cip=MTEwLjg2LjM4LjI1LDhkZ29jbixDMg=='%(rooid,uid,pwd)
    print url



if __name__ == '__main__':
    while True:
        uid = raw_input('uid:')
        pwd = getpwd(uid)
        rooid = raw_input('roomid:')
        geturl(rooid,uid,pwd)