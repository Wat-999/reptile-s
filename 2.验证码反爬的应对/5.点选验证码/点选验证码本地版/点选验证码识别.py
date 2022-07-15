import os
from chaojiying import Chaojiying_Client
from selenium import webdriver
import time
from selenium.webdriver.common.by import By

def cjy():  # 定义超级鹰识别函数
    chaojiying = Chaojiying_Client('hjl990505', 'hjl5406558', '934599')  # 账号、密码、项目号（这个不用改）
    im = open('a.png', 'rb').read()  # 本地图片文件路径
    code = chaojiying.PostPic(im, 9004)['pic_str']  # 9004用来识别各个点的坐标
    return code  # 返回识别的结果，这里返回的是各个点选文字的坐标，如：282,54|472,59|513,144|342,157，第一个点坐标就是（282, 54）


# 1.访问网址
browser = webdriver.Chrome()

# url = r'E:\验证码反爬\点选验证码\index.html'  # 自己用的话可以直接写这样的固定路径
current_dir = os.path.dirname(os.path.abspath(__file__))  # 获取代码所在的文件夹目录
url = 'file:' + '//' + current_dir + '/index.html' # 通过拼接获取HTML文件的文件绝对路径，/相当于\\，所以拼接的时候也可以写'\\index.html'
print('此时的文件路径为：' + url)  # 打印此时的文件路径，所以如果文件位置固定，可以直接写url = r'文件路径'
browser.get(url)  # 访问网址
time.sleep(5)  # 让那个验证码稍微加载会

# 2.捕捉并截取图片
canvas = browser.find_element(By.XPATH, '//*[@id="verify"]')  # 定位点选验证码,即捕捉图片  选取时注意需要涵盖上方的图片和下方的操作说明
canvas.screenshot('a.png')  # 用selenium库的screenshot()函数截取图片
#关于25，26行代码有两点说明：第一这里没有直接写成canvas = browser.find_element(By.XPATH, '//*[@id="verify"]').screenshot('a.png')
#而是先定位点选验证码并赋给变量canvas('画布'的意思),再用screenshot()函数街区图片，这是因为在后面一次模拟单击文字时需要用到变量canvas
#第二，因为cjy()函数中打开的本地图片文件是"a.png"，所以在截取图片时也要保存为"a.png"

# 3.使用超级鹰识别，获得各点的位置坐标
result = cjy()
print(result)  # 此时获得各点的坐标，但是各点坐标格式不太规范

# 4.对获取的坐标数据进行一些处理
all_location = []  # 创建一个空列表，用来规范各点坐标
list_temp = result.split('|')  # 利用“|”将各个点的坐标提取出来，list_temp是个临时列表
print(list_temp)  # 打印临时列表，方便大家理解

for i in list_temp:  # 遍历上面的临时列表
    list_i = []  # 用来存储每点的坐标
    x = int(i.split(',')[0])  # 第一个元素为横坐标，并将字符串转为整数
    y = int(i.split(',')[1])  # 第二个元素为纵坐标，并将字符串转为整数
    list_i.append(x)  # 添加横坐标
    list_i.append(y)  # 添加纵坐标
    all_location.append(list_i)  # 汇总每一点的坐标
print(all_location)  # 此时转换成立规范的坐标

# 5.依次模拟点击文字
for i in all_location:
    x = i[0]  # 提取x坐标
    y = i[1]  # 提取y坐标
    action = webdriver.ActionChains(browser)  # 启动Selenium的动作链
    action.move_to_element_with_offset(canvas, x, y).click().perform()  # 模拟点击
    #其中需要传入前面的获取的变量即画布，这样才知道在哪个网页元素上单击
    time.sleep(1)  # 休息1秒
