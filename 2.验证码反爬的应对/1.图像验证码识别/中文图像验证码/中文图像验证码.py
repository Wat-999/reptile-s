from chaojiying import Chaojiying_Client
from selenium import webdriver
import os
from selenium.webdriver.common.by import By


def cjy():  # 使用超级鹰识别
    chaojiying = Chaojiying_Client('hjl990505', 'hjl5406558', '934599')  # 账号、密码、项目号（这个不用改）
    im = open('a.png', 'rb').read()  # 本地图片文件路径，需要为a.png名字
    code = chaojiying.PostPic(im, 2004)['pic_str']  # 1-4位纯中文用2004，参考网址：https://www.chaojiying.com/price.html
    return code


# 1.访问网址
browser = webdriver.Chrome()
url = 'file:///Users/macbookair/Desktop/%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90/%E4%B9%A6%E6%9C%AC%E9%85%8D%E5%A5%97%E8%B5%84%E6%96%99%E5%8F%8A%E7%94%B5%E5%AD%90%E4%B9%A6/python/python%E7%88%AC%E8%99%AB/%E3%80%8APython%E7%88%AC%E8%99%AB%EF%BC%88%E8%BF%9B%E9%98%B6%E4%B8%8E%E8%BF%9B%E9%80%9A%EF%BC%89%E3%80%8B%E4%BB%A3%E7%A0%81%E6%B1%87%E6%80%BB/2.%E9%AA%8C%E8%AF%81%E7%A0%81%E5%8F%8D%E7%88%AC/1.%E5%9B%BE%E5%83%8F%E9%AA%8C%E8%AF%81%E7%A0%81%E8%AF%86%E5%88%AB/%E4%B8%AD%E6%96%87%E5%9B%BE%E5%83%8F%E9%AA%8C%E8%AF%81%E7%A0%81/index.html'
# current_dir = os.path.dirname(os.path.abspath(__file__))  # 获取代码所在的文件夹目录，照抄这行代码即可
# url = current_dir + '/index.html'  # 获取HTML文件的文件绝对路径，/相当于\\，所以拼接的时候也可以写'\\index.html'
# print('此时的文件路径为：' + url)  # 所以如果文件位置固定，可以直接写url = r'文件路径'
browser.get(url)  # 访问网址

# 2.截取验证码图片
browser.find_element(By.XPATH, '//*[@id="verifyCanvas"]').screenshot('a.png')  # 截取验证码图片

# 3.通过超级鹰识别
result = cjy()  # 使用超级鹰OCR识别内容
print(result)

# 4.模拟键盘输入内容，并模拟点击确认按钮
browser.find_element(By.XPATH, '//*[@id="code_input"]').send_keys(result)  # 输入答案
browser.find_element(By.XPATH, '//*[@id="my_button"]').click()  # 模拟点击确认按钮
