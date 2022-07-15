# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DycjItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    href = scrapy.Field()
    pass

#为实体文件
#声明变量并指定存储变量的区域，
#再通过文件夹spider里的爬虫文件获取的内容都会存储在此处设置的区域里，然后以实体晚间作为中转站，将这些变量传输到其他文件中，
#例如传输到管道文件中进行数据存储等处理，设置完实体文件，就可以在实战中应用刚才创建的变量了