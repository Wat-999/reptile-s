from selenium import webdriver
import time
from chaojiying import Chaojiying_Client  # 引入破解图片验证码所用到的库
from selenium.webdriver.common.by import By
import requests
import re
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'}

# 1.模拟访问网址
url = "https://weibo.com/"
browser = webdriver.Chrome()
browser.get(url)  # 访问微博官网
browser.maximize_window()  # 需要全屏后才能显示那个登录框
time.sleep(5)  # 休息5秒

# 2.自动模拟输入账号密码，也可以把上面休息时间设置为30秒后手动登录

browser.find_element(By.XPATH, '//*[@id="__sidebar"]/div/div[1]/div[1]/div/button').click()  # 点击立即登录按钮
time.sleep(3)
browser.find_element(By.XPATH, '//*[@id="app"]/div[4]/div[1]/div/div[2]/div/div/div[5]/a[1]').click()  # 点击账号登录按钮
time.sleep(3)
browser.find_element(By.XPATH, '//*[@id="loginname"]').send_keys('15700717177')  # 输入账号
browser.find_element(By.XPATH, '//*[@id="pl_login_form"]/div/div[3]/div[2]/div/input').send_keys('hjl5406558')  # 输入密码
time.sleep(1)

# 3.破解验证码，详细讲解请参考本书第10章
try:
    browser.find_element(By.XPATH, '//*[@id="pl_login_form"]/div/div[3]/div[3]/a/img').screenshot('weibo.png')  # 获取验证码截图
    chaojiying = Chaojiying_Client('hjl990505', 'hjl5406558', '934599')  # 连接超级鹰远程服务
    im = open('weibo.png', 'rb').read()  # 打开刚刚保存的图片验证码
    code = chaojiying.PostPic(im, 1902)['pic_str']  # 识别图片验证码
    print(code)  # 打印破解结果
    browser.find_element(By.XPATH, '//*[@id="pl_login_form"]/div/div[3]/div[3]/div/input').send_keys(code)  # 在验证码输入框中输入破解的验证码
except:
    print('无验证码')  # 偶尔会没有验证码，所以写个try except以防万一

# 4.点击登录按钮
time.sleep(1)
browser.find_element(By.XPATH, '//*[@id="pl_login_form"]/div/div[3]/div[6]/a').click()  # 点击登录按钮

# 5.获取Cookie
cookies = browser.get_cookies()

# 6.Cookie数据处理
cookie_dict = {}
for item in cookies:
    cookie_dict[item['name']] = item['value']

# 7.访问微博热搜
url = 'http://s.weibo.com/top/summary?cate=realtimehot'
res = requests.get(url, headers=headers, cookies=cookie_dict).text

if '会游泳的图图' in res:  # 通过判断账号名是否在访问的网页中判断登录是否成功
    print('登录成功')

# 8.编写正则，提取数据
p_title = '<td class="td-02">.*?>(.*?)</a>'
p_hot = '<td class="td-02">.*?<span>(.*?)</span>'
title = re.findall(p_title, res, re.S)
hot = re.findall(p_hot, res, re.S)

title = title[1:]  # 从第二条标题开始提取
for i in range(len(title)):
    print(title[i], hot[i])  # 通过逗号可以同时打印多个变量

