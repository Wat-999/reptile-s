import scrapy
import re


class TbSpider(scrapy.Spider):
    name = 'tb'
    allowed_domains = ['taobao.com']
    start_urls = ['https://s.taobao.com/search?q=王宇韬']  # 如果想爬取多页，可以参考14.4节或者15.2节通过for循环和append函数添加网页
    for i in range(3):
        page = i * 33
        start_urls.append('https://s.taobao.com/search?q=王宇韬&s=' + str(page))  #爬取多页

    # keywords = ['金融', 'Python', '科技']  # 将这些代码取消注释，就是爬取多家的代码
    # for i in keywords:
    #     start_urls.append('https://s.taobao.com/search?q=' + keywords)

    def parse(self, response):
        res = response.text
        title = re.findall('"raw_title":"(.*?)"', res)
        price = re.findall('"view_price":"(.*?)"', res)
        sale = re.findall('"view_sales":"(.*?)人付款"', res)

        for i in range(len(title)):
            print(title[i] + '，价格为：' + price[i] + '，销量为：' + sale[i])
