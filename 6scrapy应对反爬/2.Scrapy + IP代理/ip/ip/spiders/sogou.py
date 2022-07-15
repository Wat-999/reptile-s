import scrapy
import json
import requests
import time
import urllib3

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.0.0 Safari/537.36'}


class SogouSpider(scrapy.Spider):
    name = 'sogou'
    allowed_domains = ['sogou.com']
    start_urls = ['http://sogou.com/']
    for i in range(1):  # 要爬的页数，可以自定义修改
        start_urls.append('https://pic.sogou.com/napi/pc/searchList?mode=13&dm=4&cwidth=1920&cheight=1080&xml_len=48&query=壁纸&start' + str(i * 48))

    def parse(self, response):
        data = response.text
        js = json.loads(data)

        for i in js['data']['items']:
            title = i['title']
            img_url = i['picUrl']
            title = title.replace(' > ', '')  # 清除标题中的一些特殊字符

            path = 'images/' + str(i+1) + title + '.png'  # 需要在代码所在文件夹新建一个images文件夹

            res = requests.get(img_url, headers=headers)
            file = open(path, 'wb')  # 注意要以二进制的模式写入
            file.write(res.content)
            file.close()

            print(title + "下载完毕")
            time.sleep(1)
