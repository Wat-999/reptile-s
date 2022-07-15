import scrapy
import re
from dycj.items import DycjItem  #导入实体文件，其中dycj为爬虫项目名，items为实体文件，DycjItem为实体文件中定义的类

class YicaiSpider(scrapy.Spider):
    name = 'yicai'
    allowed_domains = ['yicai.com']
    start_urls = ['https://www.yicai.com/search?keys=阿里巴巴']  # 修改下start_urls为我们的目标网址

    def parse(self, response):
        item = DycjItem()  #激活实体文件
        data = response.text
        # print(data)  # 代码调试完毕后可以将这行代码注释掉

        p_title = '<div class="m-list">.*?<h2>(.*?)</h2>'
        p_href = '<a href="(.*?)" class="f-db" target="_blank">'
        title = re.findall(p_title, data)
        href = re.findall(p_href, data)

        title = title[:-1]  # 因为最后一条匹配的内容不是新闻，就给删掉了
        href = href[:-1]  # 因为最后一条匹配的内容不是新闻，就给删掉了
        href_list = []
        for i in range(len(title)):
            href[i] = href[i].split('<a href="')[-1]  # 如果不加这行代码，第一条新闻匹配的网址会夹杂一些不需要的内容
            href[i] = 'https://www.yicai.com' + href[i]
            href_list.append(href[i])
            # print(str(i+1) + '.' + title[i])
            # print(href[i])
        item['title'] = title
        item['href'] = href_list
        yield item   #将提取结果传回到实体文件
