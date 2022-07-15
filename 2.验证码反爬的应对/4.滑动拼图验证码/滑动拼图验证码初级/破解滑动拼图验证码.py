from selenium import webdriver
import time
import re
import os
from selenium.webdriver.common.by import By

#1访问网址
browser = webdriver.Chrome()

current_dir = os.path.dirname(os.path.abspath(__file__))  # 获取代码所在的文件夹目录
url = 'file:' + '//' + current_dir + '/index.html' # 获取HTML文件的文件绝对路径
print(url)  # 打印此时的文件路径，所以如果文件位置固定，可以直接写url = r'文件路径'
browser.get(url)

#2 定位滑块并模拟单击， 让缺口显示出来
slider = browser.find_element(By.XPATH, '//*[@id="slideBtn"]')  #定位滑块
slider.click()  #模拟单击滑块，让缺口显示出来
time.sleep(3)   #等待3秒
#初级版滑动拼图验证码是在普通滑块验证码的基础上增加另随机的滑动距离，用户需要根据拼图的缺口位置来决定滑块的滑动距离
#现在的滑动拼图验证码的初始状态，都是未显示拼图和缺口。单击滑块后就会出现拼图和缺口，之后才可以利用这一特性来找到拼图和缺口的位置
#出现拼图和缺口后，我们需要将其滑块拖动到合适的位置，使得拼图正好落入缺口。松开鼠标将自动验证结果，如果拼图填充正确，则通过验证；
#否则，验证失败，滑块回到起始位置，需要重新拖动滑块
#由上述机制可知，网页中初级版滑动拼图验证码处理的基本思路如下：
#1用selenium库打开网页
#2用selenium库定位滑块并模拟单击滑块，让缺口显现出来
#3找到拼图和缺口的位置，初级版可以直接在网页源代码中找到
#4计算滑动的距离
#5用selenium库模拟移动滑块，完成验证


#3获取缺口位置
data = browser.page_source  #获取网页源代码
p_qk = '<div class="slide-box-shadow".*?left: (.*?)px'  #对缺口属性编写正则
qk_left = re.findall(p_qk, data, re.S)   #提取缺口的left属性值
#left属性值，即缺口的左边界到整张图片左边界的距离，这里为131像素
print(qk_left)

#4计算滑块需要滑动的距离
distance = float(qk_left[0]) - float(2)  #减去拼图左侧的2像素，获得滑动距离
print(distance)
#这里用float()函数将数据都转换为浮点数(即带小数点的数)
#float(2)中间的2是与查看缺口的left属性值的方法一样来查看拼图的left属性值，即拼图的左边界到整张图片的左边界的距离，这里为2像素


# 开始滑动~！偶尔会因为移动太快导致验证失败，可以重新运行程序进行尝试
action = webdriver.ActionChains(browser)  #启动动作链
action.click_and_hold(slider).perform()   #按住滑块
action.move_by_offset(distance, 0) #移动滑块
time.sleep(2)  #休息2秒
action.release().perform()  #释放滑块

#补充知识点：模拟慢慢滑动
#如果不希望滑太快，可以将滑动距离分为3段，让滑块分3次滑动，每次滑动后等待一定时间，代码如下
# x1 = distance / 3
# x2 = x1
# x3 = distance - x1 - x2
# action.move_by_offset(x1, 0)
# time.sleep(1)
# action.move_by_offset(x2, 0)
# time.sleep(1)
# action.move_by_offset(x3, 0)
# time.sleep(1)
# action.release().perform()  #释放滑块