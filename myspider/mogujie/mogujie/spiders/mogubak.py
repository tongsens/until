# -*- coding: utf-8 -*-
import scrapy
from selenium import webdriver
import os
import time
import urllib2

class MoguSpider(scrapy.Spider):
    name = "mogus"
    allowed_domains = ["mogujie.com", "mogucdn.com"]
    start_urls = (
        'http://xiuseqingqu.mogujie.com/index?shopwebtag=1',
    )

    def parse(self, response):
        for href in response.xpath('//li[@class="z-nav-list"]/a/@href'):
            newulr = href.extract()
            yield scrapy.Request(newulr, callback=self.getitemlist)

    def getitemlist(self, response):
        for href in response.xpath('//div[@class="item i_w_f youdian"]/a/@href'):
            newulr = href.extract()
            self.getimg(newulr)

    def getimg(self, url):
        driver = webdriver.PhantomJS()
        driver.get(url)
        driver.find_element_by_xpath('//li[@data-panels="rates"]').click()
        driver.find_element_by_xpath('//div[@class="nav clearfix"]/a[@data-type="img"]').click()
        sel = scrapy.selector.Selector(text=driver.page_source)
        for url in sel.xpath('//img[@width="40"]/@src').extract():
            imgsrc = url.replace("100x100","468x468")
            filename = imgsrc.split("_")[1]+'.jpg'
            filepath = os.path.join('/mnt/img', filename)
            with open(filepath, 'w') as fp:
                res = urllib2.urlopen(imgsrc).read()
                fp.write(res)
            print imgsrc
