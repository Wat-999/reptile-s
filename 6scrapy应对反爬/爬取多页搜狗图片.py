import requests
import json
import time
import urllib3
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.0.0 Safari/537.36'}
pages = 3   # 要爬的页数，可以自定义修改
for i in range(pages):
    url = 'https://pic.sogou.com/napi/pc/searchList?mode=13&dm=4&cwidth=1920&cheight=1080&xml_len=48&query=壁纸&start' + str(i*48)  # 因为i是从0开始的序号，所以这里不需要再-1，直接*48即可
    urllib3.disable_warnings()  #为了不烦人，直接移除警告：disable_warnings()
    res = requests.get(url, headers=headers, verify=False)#在请求头中加verify=Fals忽略ssl认证
    data = res.text
    js = json.loads(data)
    for i in js['data']['items']:
        title = i['title']
        img_url = i['picUrl']
        title = title.replace(' > ', '')  # 清除标题中的一些特殊字符

        # 添加IP代理应对IP反爬
        proxy = requests.get('http://api.xdaili.cn/xdaili-api//greatRecharge/getGreatIp?spiderId=890fff42d97343ecbb39c346691044d9&orderno=YZ2022637960aBQrQI&returnType=1&count=1').text
        proxy = proxy.strip() #这一步非常重要，因为要把你看不见的换行符等空格给清除掉
        proxies = {"http": "http://"+proxy, "https": "https://"+proxy}

        # 爬取图片，如果不想加IP代理，把proxies=proxies删掉就行
        path = '/Users/macbookair/Desktop/简历/images/' + title + '.png'  # 需要在代码所在文件夹新建一个images文件夹
        res = requests.get(img_url, headers=headers, proxies=proxies)
        file = open(path, 'wb')  # 注意要以二进制的模式写入
        file.write(res.content)
        file.close()

        print(title + "下载完毕")
        time.sleep(5)  # 这里将休息时间变为5秒是防止提取IP过快，超过频率限制