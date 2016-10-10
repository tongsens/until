__author__ = 'root'

import scrapy
from downformweb.malspider.malspider.db.database import *
from downformweb.upzip.uzip import *

class MalSpider(scrapy.Spider):
    name = 'mal'
    allowed_domains = ["malekal.com"]
    start_urls = [
        "http://malwaredb.malekal.com/index.php?page=1",
    ]

    def parse(self, response):
        for href in response.xpath('//table/tr/td/a/@href'):
            if 'files' in href.extract():
                url = response.urljoin(href.extract())
                md5 = url.split('=')[1]
                db = DataBase('md5.db')
                if not db.isExit(md5=md5):
                    yield scrapy.Request(url, callback=self.download)

        nextlink = response.xpath('//p/a/@href').extract()[1]
        if nextlink:
            nexturl = response.urljoin(nextlink)
            print nexturl
            yield scrapy.Request(nexturl, callback=self.parse)

    def download(self, response):
        db = DataBase('md5.db')
        filename = response.url.split('/')[4]
        md5 = filename.split('.')[0]
        filepath = os.path.join('/root/data', filename)
        try:
            with open(filepath, 'wb') as fp:
                fp.write(response.body)
            db.insertMd5(md5=md5)
            extract_zip(filepath, '/root/data')
        except Exception as e:
            print 'Error: %s'%e