#这里首先介绍一下，如何使用常规的requests库来自动批量爬取搜狗图片，为之后通过scrapy爬取作铺垫。搜狗图片的爬取有一些难度，主要体现在4方面
#1网页是用Ajax动态请求渲染过的，即通过向向下滚动页面才会刷新内容，且刷新后的网址没有变化，需要通过分析Ajax动态请求找到真正的网址
#2获取的数据是json格式的，提取稍微有些难度
#3在不添加User-Agent(用户代理)的情况下很容易触发反爬机制，尤其是在下载图片时需要加上User-Agent参数
#4搜狗的相关网址都启用来IP反爬机制，如果同一个IP地址爬取次数太多，搜狗就会封锁该IP地址，需要用IP代理来应对IP反爬机制

#分析Ajax动态请求找到正的网址
#打开开发者工具，1切换值"Network"选项卡， 2单击xhr按钮筛选请求条目，3然后向下滚动页面以加载新的内容，可以看到相关的Ajax请求
#4选中某一条Ajax请求  5在右侧"Headers"选选项卡下查看General栏目中的"Request URL"参数，其值就是实际请求的网址(即刷新出来的内容)

#分析3次ajax请求(可以视为3个页面),对应的实际网址如下：
#网址1：https://pic.sogou.com/napi/pc/searchList?mode=13&dm=4&cwidth=1512&cheight=982&start=0&xml_len=48&query=%E5%A3%81%E7%BA%B8
#网址2：https://pic.sogou.com/napi/pc/searchList?mode=13&dm=4&cwidth=1512&cheight=982&start=48&xml_len=48&query=%E5%A3%81%E7%BA%B8
#网址3：https://pic.sogou.com/napi/pc/searchList?mode=13&dm=4&cwidth=1512&cheight=982&start=96&xml_len=48&query=%E5%A3%81%E7%BA%B8

#通过观察可以发现，不同页面的网址的主要区别是star参数不同：第一个star参数为0，第二个star参数为48，第3个为96。由此总结出不同页面对应的
#star参数为(页数-1)*48,其中的48表示每个页面显示48张图片
#此外query参数的值%E5%A3%81%E7%BA%B8是壁纸经过浏览器翻译的结果，可以直接将其改成壁纸，不会影响访问
#其他参数其实都不是必须的，例如cwidth表示图片的宽度，cheight表示图片的高度，如果删去这些参数就没有宽高限制，但是不影响图片爬取
#这里保留相关参数，最终网址规律如下：
#https://pic.sogou.com/napi/pc/searchList?mode=13&dm=4&cwidth=1512&cheight=982&start=((页数-1)*48)&xml_len=48&query=壁纸
#根据上述规律，在编写代码时就可以构造如下网址，这里为了方便拼接字符串，把star参数放在最后
#url = 'https://pic.sogou.com/napi/pc/searchList?mode=13&dm=4&cwidth=1512&cheight=982&xml_len=48&query=壁纸&start=' + str((n-1)*48)

#解析json格式数据
#在浏览器中打开某一个ajax实际请求的网址，显示的内容实际上是json格式的数据。为了更好的查看和分析json格式数据，
#这里需要在谷歌浏览器中安装插件jsonvue，以便对不同层次的数据进行折叠和展开
#json格式数据可以理解为字典和列表的组合，调用方法与字典和列表类似。这里的json格式数据就是一个大字典，其中所有图片信息都存储在data键下
#的items键下。items键所对应的值是一个大列表(items前面的"-"号是jsonvue中用于折叠内容的按钮图标，并不是数据的内容)
#大列表里又用一个个字典存储这一张张图片的信息，每个字典中的title键对应图片名称，picUrl键对应图片网址
import time
import requests
import json

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.0.0 Safari/537.36'}
url = 'https://pic.sogou.com/napi/pc/searchList?mode=13&dm=4&cwidth=1512&cheight=982&start=0&xml_len=48&query=壁纸'
res = requests.get(url, headers=headers)
data = res.text   #通过res.text获取相应res中的文本数据
js = json.loads(data)  #用json库中的loads()函数将文本数据装换为python对象。
# js = res.json()       #等同上面，其实对于requests库获取的响应res，还可以直接用requests库中的json()函数来转换
print(js)   #打印结果，其结构和在浏览器中看到的一致(jsonvue）

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
#js['data']['items']表示提取data键所对应的值中的items键所对应的值，根据前面的分析js['data']['items']提取到的是一个大列表
#那么i就表示这个大列表中的元素，即以字典形式存储的每张图片的信息

#补充知识点
#json的全称是javaScript Object Notation(javaScript对象标记)，它是一种轻量级的数据交换格式，构造简洁，结构化程度高
#1对象和数组
#json支持的数据类型有字符串、数字、对象、数组等，其中对象和数组是比较特殊且常用的两种类型
#对象是由{}定义的键值对结构，如{key1:value1,key2:value2,~~~~,keyn:valuen},key为属性，value为属性对应的值。key可以为整数或字符串，value可以是json支持的任意类型
#数组是由[]定义的索引结构，如['java','vb', ~~~~~~],数组中的值可以是json支持的任意类型

#一个json格式数据示例如下，可以看出，它是一个包含两个对象的数组
# [{
#     '名称': '百度',
#     '网址': 'www.baidu.com',
#     '类型': '搜索引擎'
# },{
#     '名称': '百度',
#     '网址': 'www.baidu.com',
#     '类型': '搜索引擎'
#
# }]
#爬虫中遇到的json格式数据常常是像上面的例子那样由对象和数组嵌套组合而成，我们可以将数组理解为python的列表，将对象理解为python的字典，那么上面的例子
#就可以视为一个含有两个字典的大列表。我们可以使用python内置的json库对json格式数据进行操作。常用的函数有两个：
#loads()函数，用于解析json格式的字符串并转换成python对象(如字典、列表等)
#dumps()函数，用于解析python对象(如字典、列表等)并转换为json格式的字符串
#json格式字符串的读取
# import json
# a = '''
# [{
#     "名称": "百度",
#     "网址": "www.baidu.com",
#     "类型": "搜索引擎"
# }, {
#     "名称": "新浪微博",
#     "网址": "www.weibo.com",
#     "类型": "社交平台"
# }]
# '''
# print(type(a))  #打印数据类型
# result = json.loads(a)  #将json格式的a装换为python对象
# print(result)
# print(type(result))
#可以看到，装换得到的python对象是一个列表，其中嵌套着两个字典，它和原字符串在形式上一致，但是在数据类型上已经不同。对于装换得到的python对象，
#我们可以用python的语法来提取其中的内容。例如，要提取列表中第一个字典的"类型"键对应的值，可以使用如下两种方法：
# result[0]['类型']
# result[0].get('类型')
#两种方法都是先用[0]提取第一个字典，区别在于指定键名的方式：第1种方法通过"[]"指定键名来提取对应的值；
#第二种方法则是用get()函数指定键名来提取对应的值。建议使用第2中方法，因为如果传入的键名不存在，那么第1种方法会报错，而第二种方法不会报错，而是返回None
#此外，get()函数还可以传入第2个参数，用于在指定键对应的值不存在时返回一个默认值，演示代码如下
# result[0].get('成立时间')
# result[0].get('成立时间', '2000年')
#对于第98行代码，因为数据中没有名为'成立时间'的键，所以会返回None。对于第二99行代码，加入第2个参数后，如果传入的键名不存在，则会返回默认值'2000年'

#json格式字符串的输出
#下面使用json库中的dumps()函数将前面的变量result重新转换为json格式字符串
# str2 = json.dumps(result, indent=2, ensure_ascii=False)
#dumps()函数的参数indent代表缩尽量的大小(字符个数),可以通过指定indent=2来保留json格式。
#此外，因为例子中的数据包含中文字符，所以还需要指定参数ensure_ascii=False
# print(type(str2))
# print(str2)