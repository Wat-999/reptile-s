import time
import requests
import json

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.0.0 Safari/537.36'}
url = 'https://pic.sogou.com/napi/pc/searchList?mode=13&dm=4&cwidth=1512&cheight=982&start=0&xml_len=48&query=壁纸'
res = requests.get(url, headers=headers)
data = res.text   #通过res.text获取相应res中的文本数据
js = json.loads(data)  #用json库中的loads()函数将文本数据装换为python对象。
# js = res.json()       #等同上面，其实对于requests库获取的响应res，还可以直接用requests库中的json()函数来转换
#print(js)   #打印结果，其结构和在浏览器中看到的一致(jsonvue）

#用for循环语句从上述json格式数据中提取每一张图片的名称和网址
for i in js['data']['items']:
    title = i['title']
    img_url = i['picUrl']
    title = title.replace(' > ', '')  #清除图片名称中的特殊符号
    path = '/Users/macbookair/Desktop/简历/images' + title + '.png'   #需要提前创建文件夹"images"
    res = requests.get(img_url, headers=headers)  #打开图片网址
    file = open(path, 'wb')   #注意要以二进制模式打开
    file.write(res.content)  #写入
    file.close()  #关闭文件
    print(title + '下载完毕')
    time.sleep(1)  #用上述代码爬取一定数量的图片后就会报错ConnectionError: ('Connection aborted.', ConnectionResetError
    #原因是爬取过于频繁导致ip地址被封

#知识点补充：用urlretrieve()函数下载图片时如何添加headers
#此方法添加headers参数的方法比requests库略微复杂
import urllib3.request
opener = urllib3.request.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.0.0 Safari/537.36')]
urllib3.request.install_opener(opener)
urllib3.request.urlretrieve(图片网址, 图片保存路径)