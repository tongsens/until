__author__ = 'root'

import urllib2
import json


class CrawlImg():
    def __init__(self, url):
        self.url=url
        self.itemid = self.getitemid()
        self.imglist = []
        self.buildPageUrl()

    def getitemid(self):
        return self.url.split('?')[0].split('/')[-1]

    def buildPageUrl(self):
        model = "http://shop.mogujie.com/ajax/pc.rate.ratelist/v1?pageSize=20&sort=1&isNewDetail=1&itemId=%s&type=1&isImg=1&page="%self.itemid
        for i in range(1,200):
            url = model+str(i)
            data = urllib2.urlopen(url).read()
            dejson = json.loads(data)
            if dejson['data']["total"]==0:
                break
            self.getimgurl(dejson)

    def getimgurl(self, data):
        comlist = data["data"]["list"]
        for x in comlist:
            try:
                self.imglist.extend(x["append"]["images"])
            except:
                try:
                    self.imglist.extend(x["images"])
                except:
                    print x

    def getimglist(self):
        return self.imglist

if __name__ == '__main__':
    url = "shop.mogujie.com/detail/17uifu2?acm=3.ms.1_4_17uifu2.0.13850.Rkkq08x0rRL.t_0&ptp=1.eW5XD._b_24d26a5beabd83bd_wall_docs.1.MCUTe&f=baidusem_15iolsgmgz"
    cimg =CrawlImg(url)
    imglist = cimg.getimglist()
    for x in imglist:
        print x
