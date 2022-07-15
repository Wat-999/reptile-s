from selenium import webdriver
import time
import re
import os
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()

current_dir = os.path.dirname(os.path.abspath(__file__))  # 获取代码所在的文件夹目录
url = 'file:' + '//' + current_dir + '/index.html' # 获取HTML文件的文件绝对路径
print(url)  # 打印此时的文件路径，所以如果文件位置固定，可以直接写url = r'文件路径'
browser.get(url)

# 定位滑块
slider = browser.find_element(By.XPATH, '//*[@id="slideBtn"]')#定位滑块

action = webdriver.ActionChains(browser)  #启动动作链
action.click_and_hold(slider).perform()   #按住滑块
time.sleep(2)
data = browser.page_source  #打印网页源代码

p_tbk = '<div class="slide-box-shadow".*?left: (.*?)px'  #编写left属性值正则
tbk_left = re.findall(p_tbk, data, re.S)     #提取left属性值
print(tbk_left)
distance = float(tbk_left[0]) - float(2)
#float(2)中间的2是与查看缺口的left属性值的方法一样来查看拼图的left属性值，即拼图的左边界到整张图片的左边界的距离，这里为2像素
print(distance)

# 开始滑动~！偶尔会因为移动太快导致验证失败，可以重新运行程序进行尝试
action.move_by_offset(distance, 0)    #移动滑块
time.sleep(2)
action.release().perform()   #释放滑块
