from selenium import webdriver
import os
import time
from selenium.webdriver.common.by import By
# 1.访问网址
browser = webdriver.Chrome()
# url = r'E:\验证码反爬\滑块验证码\index.html'
current_dir = os.path.dirname(os.path.abspath(__file__))  # 获取代码所在的文件夹目录
url = 'file:' + '//' + current_dir + '/index.html'  # 获取HTML文件的文件绝对路径
print('此时的文件路径为：' + url)  # 打印此时的文件路径，所以如果文件位置固定，可以直接写url = r'文件路径'
browser.get(url)  # 访问网址

# 2.获取滑块按钮
huakuai = browser.find_element(By.XPATH, '//*[@id="code-box"]/span')  # 获取滑块按钮

# 3.开始滑动
action = webdriver.ActionChains(browser)  # 启动滑动功能
action.click_and_hold(huakuai).perform()  # 按住滑块
time.sleep(2)  # 休息两秒，来看效果，不然执行太快了
action.move_by_offset(260, 0)  # 移动滑块的距离=width-height  即宽度减去高度
#查看滑轨的尺寸，有两种方法：一种是直接看图上方的"div#code-box.code-box300*40",其中300*40就表示宽为300像素，高为40像素
#这里的像素可以理解为一种长度单位；另一种是在界面右侧的"styles"选项卡中可以看到width(宽)为300像素，height(高)为40像素
action.release().perform()  # 释放滑块


#需要注意的是，现在有一些含有滑块验证码的网页会检测当前浏览器是否为selenium库的webdriver模拟浏览器
#如果是的话，便难以模拟滑动成功。这种反爬机制已经不是验证码反爬，而是webdriver反爬，处理起来比较困难。
#这里说一个讨巧的方法：如果是登录阶段需要进行滑动验证(如淘宝的登录),那么可以在代码中用time.sleep()等待一段时间，在这段时间用其他方式手动登录，
#如手动扫码登录，登录成功后在用selenium库继续爬取。