from chaojiying import Chaojiying_Client
from selenium import webdriver
import os
from selenium.webdriver.common.by import By


def cjy():  # 使用超级鹰识别
    chaojiying = Chaojiying_Client('hjl990505', 'hjl5406558', '934599')  # 账号、密码、项目号（这个不用改）
    im = open('a.png', 'rb').read()  # 本地图片文件路径，需要为a.png名字
    code = chaojiying.PostPic(im, 1902)['pic_str']  # 4-6位英文数字用1902
    return code


# 1.访问网址
browser = webdriver.Chrome()
# url = r'E:\验证码反爬\英文图像验证码\index.html'
current_dir = os.path.dirname(os.path.abspath(__file__))  # 获取代码所在的文件夹目录，照抄这行代码即可
url = 'file:' + '//' + current_dir + '/index.html'  # 获取HTML文件的文件绝对路径，/相当于\\，所以拼接的时候也可以写'\\index.html'
print('此时的文件路径为：' + url)  # 所以如果文件位置固定，可以直接写url = r'文件路径'
browser.get(url)  # 访问网址

# 2.截取验证码图片
browser.find_element(By.XPATH, '//*[@id="verifyCanvas"]').screenshot('a.png')  # 截取验证码图片

# 3.通过超级鹰识别
result = cjy()  # 使用超级鹰OCR识别内容
print(result)

# 4.模拟键盘输入内容，并模拟点击确认按钮
browser.find_element(By.XPATH, '//*[@id="code_input"]').send_keys(result)  # 输入答案
browser.find_element(By.XPATH, '//*[@id="my_button"]').click()  # 模拟点击确认按钮
