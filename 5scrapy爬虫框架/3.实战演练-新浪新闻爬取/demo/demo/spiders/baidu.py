import scrapy
import re
from bs4 import BeautifulSoup


class BaiduSpider(scrapy.Spider):
    name = 'baidu'
    allowed_domains = ['baidu.com']  # 这个其实不太重要，哪怕不是该域名的好像也可以访问
    start_urls = ['https://news.sina.com.cn/o/2020-09-27/doc-iivhvpwy9145593.shtml']

    def parse(self, response):
        res = response.text  # 注意用response.text获取到文本内容
        soup = BeautifulSoup(res, 'html.parser')
        title = soup.select('.main-title')[0].text
        print(title)
