from selenium import webdriver
import time
brower = webdriver.Chrome()
url = 'https://login.taobao.com/member/login.jhtml'
brower.get(url)
# browser.find_element_by_xpath('//*[@id="login"]/div[1]/i').click()  # 通过这行代码可以自动切换成二维码模式，其实手动点也可以
time.sleep(20)  #等待20秒用来扫码登录，推荐扫码登录
cookies = brower.get_cookies()  #获取cookie
print(cookies)    #打印cookie值
#获得的cookie时效通常是一天左右。打印输出，可以看到获得的是一个列表，列表的元素是一个个字典，字典里包含各个cookie
#其实就是用开发者工具看到的东西，我们并不需要cookie中的所有内容，只需其中的name和value值，因而还需要对获取的cookie处理

#修改cookie的数据格式：修改成requests库使用的格式
cookie_dict = {}
for item in cookies:
    cookie_dict[item['name']] = item['value']
    #第14行和第15行用来遍历上面获取的cookie，从中提取name和value，添加到创建的字典
    #从打印结果得知是列表嵌字典，因此item是一个字典结构，那么item['name']和item['value']就是根据字典的键提取对应的值。
    #列入，第一条cookie的name为"1"，value为"ebg·····"。而cookie_dict[item['name']] = item['value']则是在字典中添加键值对
    #例如cookie_dict['a'] = 'b' 表示在字典cookie_dict中添加一个键为'a'、值为'b'的键值对


#3通过requests库使用cookie
import requests
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.0.0 Safari/537.36'}
url = 'https://s.taobao.com/search?q=王宇韬'
res = requests.get(url1, headers=headers, cookies=cookie_dict).text
#print(res)   #在打印的源代码网页中寻找规律

# 验证是否登录成功
if 'fgwyt94' in res:
    print('登录成功')

# 4.正则表达式提取信息
import re
title = re.findall('"raw_title":"(.*?)"', res)
price = re.findall('"view_price":"(.*?)"', res)
sale = re.findall('"view_sales":"(.*?)人付款"', res)

for i in range(len(title)):
    print(title[i] + '，价格为：' + price[i] + '，销量为：' + sale[i])



#补充知识点：淘宝网多页数据爬取
#为了爬取多页数据，在浏览器中翻页，会发现网址有如下规律
#原网址：https://s.taobao.com/search?ie=utf8&initiative_id=staobaoz_20220604&stats_click=search_radio_all%3A1&js=1&imgfile=&q=%E7%8E%8B%E5%AE%87%E9%9F%AC&suggest=history_2&_input_charset=utf-8&wq=&suggest_query=&source=suggest&bcoffset=4&ntoffset=4&p4ppushleft=2%2C48&s=0
#第一页网址(把网址中一些没有变化的参数删除):https://s.taobao.com/search?ie=王宇韬&s=0
#第二页网址：https://s.taobao.com/search?ie=王宇韬&s=44
#第三页网址：https://s.taobao.com/search?ie=王宇韬&s=88
#可以看到，在翻页的过程中，主要变化的是一个名为s的参数，而且可以推测第n页的参数s的值为44*(n-1)
#第n页的网址：https://s.taobao.com/search?ie=王宇韬&s=44*(n-1)
#得到网址规律后，便可以通过for循环语句来爬取多页数据了，在获取到cookie并修改数据格式后，通过如下代码来爬取多页数据
# res_all = []  # 构造一个空字符串, 用于汇总每一页的网页源代码
# for i in range(3):  # 这里演示爬取3页
#     page = i * 44  # i是从0开始的
#     url = 'https://s.taobao.com/search?ie=王宇韬&s=' + str(page)  # 拼接页码上去
#     res = requests.get(url, headers=headers, cookies=cookie_dict).text
#     res_all = res_all + res  # 拼接每一页的网页源代码
#
# title = re.findall('"raw_title":"(.*?)"', res_all)
# price = re.findall('"view_price":"(.*?)"', res_all)
# sale = re.findall('"view_sales":"(.*?)人付款"', res_all)
#
# for i in range(len(title)):
#     print(title[i] + '，价格为：' + price[i] + '，销量为：' + sale[i])
#
