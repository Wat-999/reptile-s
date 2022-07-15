from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import requests
import re

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.0.0 Safari/537.36'}

#1用selenium库获取cookie
brower = webdriver.Chrome()
url = 'https://login.taobao.com/member/login.jhtml'
brower.get(url)
browser.browser.find_element(By.XPATH, '//*[@id="login"]/div[1]/i').click()  # 通过这行代码可以自动切换成二维码模式，其实手动点也可以
time.sleep(20)  #等待20秒用来扫码登录，推荐扫码登录
cookies = brower.get_cookies()  #获取cookie
#print(cookies)    #打印cookie值


#2修改cookie的数据格式：修改成requests库使用的格式
cookie_dict = {}
for item in cookies:
    cookie_dict[item['name']] = item['value']


#3通过requests库使用cookie
url = 'https://s.taobao.com/search?q=王宇韬'
res = requests.get(url, headers=headers, cookies=cookie_dict).text
#print(res)   （在打印的源代码网页中寻找规律）
if 'fgwyt94' in res:   # 验证是否登录成功
    print('登录成功')


# 4.正则表达式提取信息
res_all = ''  # 构造一个空字符串, 用于汇总每一页的网页源代码
for i in range(3):  # 这里演示爬取3页
    page = i * 44  # i是从0开始的
    url = 'https://s.taobao.com/search?ie=王宇韬&s=' + str(page)      # 拼接页码上去
    res = requests.get(url, headers=headers, cookies=cookie_dict).text
    res_all = res_all + res           # 拼接每一页的网页源代码

title = re.findall('"raw_title":"(.*?)"', res_all)
price = re.findall('"view_price":"(.*?)"', res_all)
sale = re.findall('"view_sales":"(.*?)人付款"', res_all)

#5打印输出数据
for i in range(len(title)):
    print(title[i] + '，价格为：' + price[i] + '，销量为：' + sale[i])