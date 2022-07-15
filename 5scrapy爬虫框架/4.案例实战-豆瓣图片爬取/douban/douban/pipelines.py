# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from urllib.request import urlretrieve


class DoubanPipeline:
    def process_item(self, item, spider):
        for i in range(len(item['name'])):
            print(str(i+1) + '.' + item['name'][i])
            urlretrieve(item['url'][i], 'images/' + item['name'][i] + '.png')  # 得新建好images文件夹，注意在images文件夹是在douban文件夹下面，也即pipelines.py所在的文件夹
        return item
 #管道文件编写爬取后的处理