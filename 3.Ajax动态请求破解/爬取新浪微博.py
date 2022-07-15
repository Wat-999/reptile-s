from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import re

# 1.访问网址
url = "https://weibo.com/"
browser = webdriver.Chrome()
browser.get(url)  # 访问微博官网
browser.maximize_window()  # 需要全屏后才能显示那个登录框
time.sleep(30)  # 休息30秒，进行手动登录

# 2.访问环球时报官微
url = 'https://weibo.com/huanqiushibaoguanwei?is_all=1'  # 必须登录，直接访问是访问不了的，这里加上参数is_all=1，查看全部微博
browser.get(url)



# 3.定义模拟翻页的函数
def fanye():
    for i in range(5):
        browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
        time.sleep(10)

    # try:
    #     browser.find_element(By.XPATH, '//*[@id="Pl_Official_MyProfileFeed__27"]/div/div[47]/div/a[2]').click()
    # except:
    #     try:
    #         browser.find_element(By.XPATH, '//*[@id="Pl_Official_MyProfileFeed__27"]/div/div[48]/div/a[2]').click()
    #     except:
    #         try:
    #             browser.find_element(By.XPATH, '//*[@id="Pl_Official_MyProfileFeed__27"]/div/div[47]/div/a').click()
    #         except:
    #             browser.find_element(By.XPATH, '//*[@id="Pl_Official_MyProfileFeed__27"]/div/div[48]/div/a').click()
    #

# 4.进行模拟翻页
data_all = ''
for i in range(3):  # 这里作为演示，只翻页3次
    fanye()
    data = browser.page_source
    data_all = data_all + data

# 5.正则表达式提取所需内容
p_title = '<div class="detail_wbtext_4CRf9">.*?target="_blank">(.*?)</div>'
title = re.findall(p_title, data_all, re.S)  # 这里用的是上面汇总的源代码data_all

# 6.打印结果
for i in range(len(title)):
    title[i] = title[i].strip()
    title[i] = re.sub('<.*?>', '', title[i])
    title[i] = re.sub('\.*?>', '', title[i])
    print(title[i])

