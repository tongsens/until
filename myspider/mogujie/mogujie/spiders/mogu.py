# -*- coding: utf-8 -*-
import scrapy
from selenium import webdriver
import os
import time
import urllib2
from mogujie.getimgurl import *

class MoguSpider(scrapy.Spider):
    name = "mogu"
    allowed_domains = ["mogujie.com", "mogucdn.com"]
    start_urls = (
        'http://list.mogujie.com/s?q=%E9%9C%B2%E4%B9%B3&ptp=1.__item_detail.0.0.JPXJZ',
    )

    def parse(self, response):
        driver = webdriver.PhantomJS()
        driver.get(response.url)
        driver.find_element_by_class_name("ts_btn").click()
        driver.find_element_by_class_name("ts_btn").click()
        sel = scrapy.selector.Selector(text=driver.page_source)
        for x in sel.xpath('//div[@class="iwf goods_item"]/a[@class="goods_info_container"]/@href'):
            url = x.extract()
            cimg = CrawlImg(url)
            imglist = cimg.getimglist()
            for x in imglist:
                yield scrapy.Request(x, self.saveimg)

    def saveimg(self, response):
        imgsrc = response.url
        print imgsrc
        filename = imgsrc.split("_")[1]+'.jpg'
        filepath = os.path.join('/mnt/lulu', filename)
        with open(filepath, 'w') as fp:
            fp.write(response.body)






