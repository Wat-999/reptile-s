# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class XinlangItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()  #对应爬取的新闻标题
    time = scrapy.Field()   #对应爬取的时间
    source = scrapy.Field() #对应爬取的来源
    pass
#实体文件设置
#在pycharm中打开爬虫项目
#然后打开实体文件"items.py"
#在XinlangItem类下添加几行代码
#title = scrapy.Field()  #对应爬取的新闻标题
#time = scrapy.Field()   #对应爬取的时间
#source = scrapy.Field() #对应爬取的来源
#scrapy.Field()可以理解为一个存储变量的区域，通过文件夹"spiders"里的爬虫文件获取的内容都会存储在此处设置的区域里，然后以实体文件作为中转站
#将这些变量传输到其他文件中，例如，传输到管道文件中进行数据存储等处理。