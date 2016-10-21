__author__ = 'root'

from selenium import webdriver
from scrapy.http import HtmlResponse
import time

class ImgMiddleware(object):

    def process_request(self, request, spider):
        if spider.name == "mogu":
            driver = webdriver.PhantomJS()
            driver.get(request.url)
            time.sleep(3)
            body = driver.page_source
            return HtmlResponse(driver.current_url, body=body, encoding='utf-8', request=request)
        else:
            return