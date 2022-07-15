import scrapy
from demo.items import SinanewsItem
from bs4 import BeautifulSoup
from datetime import datetime

class BaiduSpider(scrapy.Spider):
    name = 'xinlang'
    allowed_domains = ['xina.com']  # 这个其实不太重要，哪怕不是该域名的好像也可以访问
    start_urls = ['https://news.sina.com.cn/o/2020-09-27/doc-iivhvpwy9145593.shtml']

    def parse(self, response):
        item = SinanewsItem()
        soup = BeautifulSoup(response.text, 'html.parser')
        item['title'] = soup.select('.main-title')[0].text
        item['source'] = soup.select('.source')[0].text
        item['time'] = datetime.strptime(soup.select('.date')[0].text.strip(), '%Y年%m月%d日 %H:%M')

        yield item
