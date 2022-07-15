import scrapy
import re
from douban.items import DoubanItem  # 引入Items文件


class DbSpider(scrapy.Spider):
    name = 'db'
    allowed_domains = ['douban.com']
    start_urls = ['https://movie.douban.com/top250']
    for i in range(1, 10):  # 这里新增除了首页之外要爬的网站（也就是第2-10页）
        start_urls.append('https://movie.douban.com/top250?start=' + str(i*25))
    print(start_urls)

    def parse(self, response):
        res = response.text  # 获取网页源代码
        item = DoubanItem()  # 激活Items文件

        # 获取图片网址img和名称title
        p_title = '<img width="100" alt="(.*?)"'
        title = re.findall(p_title, res)
        p_img = '<img width="100" alt=".*?" src="(.*?)"'
        img = re.findall(p_img, res)

        item['url'] = img  # 图片网址
        item['name'] = title  # 图片名称
        yield item  # 如果这个函数之后没有内容的话，其实用return item也可以
     #编写核心爬虫代码