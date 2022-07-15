from selenium import webdriver
from chaojiying import Chaojiying_Client
import time
from selenium.webdriver.common.by import By

# 1.访问网址
browser = webdriver.Chrome()
url = 'https://passport.bilibili.com/login'
browser.get(url)  # 打开网页

# 2.输入账号密码，并点击登录按钮
user = '18810623690'  # 账号
password = 'lzhqwer4321'  # 密码
browser.find_element(By.XPATH, 'login-username').send_keys(user)  # 输入账号
browser.find_element(By.XPATH, 'login-passwd').send_keys(password)  # 输入密码
browser.find_element(By.XPATH, '//*[@id="geetest-wrap"]/div/div[5]/a[1]').click()  # 点击登录按钮

time.sleep(2)

# 3.获取点选验证码的图片
canvas = browser.find_element(By.XPATH, '/html/body/div[2]/div[2]')
canvas.screenshot('bilibili.png')

# 4.使用超级鹰识别
chaojiying = Chaojiying_Client('hjl990505', 'hjl5406558', '934599')  # 账号、密码、项目号（这个不用改）
im = open('bilibili.png', 'rb').read()  # 本地图片文件路径
result = chaojiying.PostPic(im, 9004)['pic_str']
print(result)

# 5.对获取的坐标数据进行一些处理
all_location = []  # 下面开始规范各点坐标
list_temp = result.split('|')  # 利用“|”将各个点的坐标提取出来，list_temp是个临时列表
print(list_temp)

for i in list_temp:  # 遍历上面的临时列表
    list_i = []  # 用来存储每点的坐标
    x = int(i.split(',')[0])  # 第一个元素为横坐标，并将字符串转为整数
    y = int(i.split(',')[1])  # 第二个元素为纵坐标，并将字符串转为整数
    list_i.append(x)  # 添加横坐标
    list_i.append(y)  # 添加纵坐标
    all_location.append(list_i)  # 汇总每一点的坐标
print(all_location)  # 此时转换成立规范的坐标

# 6.依次模拟点击文字
for i in all_location:
    x = i[0]
    y = i[1]
    action = webdriver.ActionChains(browser)  # 启动Selenium的动作链
    action.move_to_element_with_offset(canvas, x, y).click().perform()  # 根据坐标点击
    time.sleep(1)

# 7.点击确定按钮，登录成功
time.sleep(3)
browser.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[6]/div/div/div[3]/a/div').click()  # 点击确定按钮，登录成功
