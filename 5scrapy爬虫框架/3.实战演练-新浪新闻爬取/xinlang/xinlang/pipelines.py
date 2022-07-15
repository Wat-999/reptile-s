# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class XinlangPipeline:  # 得在settings中激活pipeline，不然不会生成txt文件
    def process_item(self, item, spider):
        file = open('xina.txt', 'w', encoding='utf-8')  # w表示清空后写入
        title = item['title']  # 提取Item中的标题信息
        for i in range(len(title)):  # 遍历标题，写入到txt中
            file.write(str(i+1) + '.' + title[i] + '\n')  # \n表示换行
        file.close()  # 关闭文件
        return item  # 返回item，这样在控制台中会打印出来结果，记着写即可
    #此文件为管道文件，其功能是将爬取的新闻标题写入文本文件
