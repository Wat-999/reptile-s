import scrapy
from xinlang.items import XinlangItem
from bs4 import BeautifulSoup


class Xina2Spider(scrapy.Spider):  # 新浪网，暂时不需要设置Robot协议和User-Agent
    name = 'xina2'
    allowed_domains = ['xina.com']
    start_urls = ['https://news.sina.com.cn/world/']  # 目的是提取这一页里多个新闻

    def parse(self, response):  # 得在settings中激活pipeline，不然不会生成txt文件
        item = XinlangItem()
        print(response.text)
        soup = BeautifulSoup(response.text, 'html.parser')
        title = soup.select('.news-item') #+ soup.select('.news-2 li a')
        title_list = []  # 用来存储多个新闻标题
        for i in range(len(title)):
            title_list.append(title[i].get_text())

        item['title'] = title_list
        yield item  # 如果这个函数之后没有内容的话，其实用return item也可以，可自行尝试下
#网页源代码没获取到