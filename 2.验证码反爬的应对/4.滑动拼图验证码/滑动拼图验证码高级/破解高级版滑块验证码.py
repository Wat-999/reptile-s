from selenium import webdriver
import os
import time
from PIL import Image, ImageChops
from selenium.webdriver.common.by import By

# 1.访问网址
browser = webdriver.Chrome()
# url = r'E:\验证码反爬\高级滑动拼图验证码\index.html'  # 自己用的话可以直接写这样的固定路径
current_dir = os.path.dirname(os.path.abspath(__file__))  # 获取代码所在的文件夹目录
url = 'file:' + '//' + current_dir + '/index.html' # 获取HTML文件的文件绝对路径
print('此时的文件路径为：' + url)  # 打印此时的文件路径，所以如果文件位置固定，可以直接写url = r'文件路径'
browser.get(url)  # 访问网址
time.sleep(2)

# 2.获取原始图片
browser.find_element(By.XPATH, '//*[@id="jigsawCanvas"]').screenshot('origin.png')  # 获取原始图片

# 3.获取有缺口的图片
slider = browser.find_element(By.XPATH, '//*[@id="jigsawCircle"]')  # 获取滑动按钮
slider.click()  # 先模拟点击下，方便下面获取到有缺口的图片
browser.find_element(By.XPATH, '//*[@id="jigsawCanvas"]').screenshot('after.png')  # 获取有缺口的图片

# 4.比较两幅图片的区别，获取需要移动的距离
image_a = Image.open('origin.png')  # 打开原始图片
image_b = Image.open('after.png')  # 打开有缺口的图片
x = ImageChops.difference(image_a, image_b).getbbox()  # 比较两个图片的差别
print(x)  # 举个例子：倘若x为：(226, 103, 277, 154)；返回缺口对应的左边横坐标（由左往右看），上边纵坐标（由上往下看），右边横坐标，下边纵坐标
distance = x[0]  # 第一个元素x[0]表示的就是缺口左边横坐标，也就是滑块需要移动的距离
print(distance)  # 如果例子为：(226, 103, 277, 154)，那么需要移动的距离为226

# 5.开始滑动！
action = webdriver.ActionChains(browser)  # 启动Selenium的动作链
action.click_and_hold(slider).perform()  # 按住滑动按钮不松开
action.move_by_offset(distance-10, 0)  # 开始滑动！这里-10，是把初始圆角矩形左侧left属性值给减去了，这样更准确
action.release().perform()  # 释放滑块
