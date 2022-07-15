# 1.连接微信APP
from appium import webdriver
import time

desired_caps = {
    'newCommandTimeout': 3600,
    'platformName': 'Android',
    'deviceName': '127.0.0.1:62001',
    'platformVersion': '5.1.1',
    'udid': '127.0.0.1:62001',
    'appPackage': 'com.tencent.mm',
    'appActivity':'.plugin.account.ui.LoginPasswordUI'
}

browser = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

# 2.手动登录微信，然后选择一个好友，进入其朋友圈页面

# 3.获取微信朋友圈源代码+解析微信朋友圈
data_all = ''
text_all = []  # 1.构造一个空列表，存储页面元素的文本信息
for i in range(20):
    data_old = browser.page_source
    data_all = data_all + data_old
    a = browser.find_elements_by_id('com.tencent.mm:id/gbx')
    for i in a:
        text_all.append(i.text)  # 2.通过append()函数

    browser.swipe(50, 1000, 50, 200)
    time.sleep(2)

    data_new = browser.page_source

    if data_new == data_old:
        break
    else:
        pass

text_all = set(text_all)  # 3.通过set()函数进行去重
for i in text_all:  # 4.打印去重后的内容
    print(i)
