from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import re

# 1.访问网址
#url = "https://weibo.com/"
# browser = webdriver.Chrome()
# browser.get(url)  # 访问微博官网
# browser.maximize_window()  # 需要全屏后才能显示那个登录框
# time.sleep(30)  # 休息30秒，进行手动登录

# 2.访问环球时报官微
url = 'https://weibo.com/u/1974576991'  # 必须登录，直接访问是访问不了的，这里加上参数is_all=1，查看全部微博
browser = webdriver.Chrome()
browser.get(url)  # 访问环球时报官微
browser.maximize_window()  # 需要全屏后才能显示那个登录框
time.sleep(30)  # 休息30秒，进行手动登录



#3分析单个微博页面
data = browser.page_source   #打印源代码
print(data)

p_title = '<div class="detail_wbtext_4CRf9">.*?target="_blank">(.*?)</div>'
title = re.findall(p_title, data, re.S)  # 这里用的是上面汇总的源代码data_all
print(title)
for i in range(len(title)):
    title[i] = title[i].strip()
    title[i] = re.sub('<.*?>', '', title[i])
    title[i] = re.sub('\.*?>', '', title[i])
    print(title[i])


