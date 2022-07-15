import scrapy
import re

class BaiduSpider(scrapy.Spider):
    name = 'baidu'
    allowed_domains = ['baidu.com']
    start_urls = ['https://www.baidu.com/s?rtt=1&bsst=1&cl=2&tn=news&word=阿里巴巴']

    def parse(self, response):
        res = response.text  # 注意用response.text获取到文本内容
        p_title = '<div class="result-op c-container xpath-log new-pmd".*?<div><!--s-data:{"title":"(.*?)"'
        title = re.findall(p_title, res, re.S)

        for i in range(len(title)):  # range(len(title)),这里因为知道len(title) = 10，所以也可以写成for i in range(10)
            title[i] = re.sub('<.*?>', '', title[i])  # 核心，用re.sub()函数来替换不重要的内容
            print(str(i + 1) + '.' + title[i])
