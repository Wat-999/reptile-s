#Ajax简介：Ajax动态请求在本质上就是把常规的翻页操作做成了动态刷新的效果。最典型的例子就是开源中国博客频道和新浪微博等博客类网站，
#大家在浏览页面时会发现，用鼠标滚轮向下滚动页面的过程中会自动加载新的内容，但是地址栏中网址没有发生变化，这就是ajax动态请求实现的。

#Ajax的基本概念与工作原理
#Ajax工作过程：1触发条件：用户在网页中触发某些条件，如将页面滚动到底部；2请求数据：前端代码使用Ajax向后端口发送请求，要求服务器提供一些新数据
#3获取数据：前端代码获得服务器的响应后，对接收到的数据进行处理并呈现在页面上。
#根据Ajax的工作原理，有两种破解方法
#方法1：以请求数据为突破口，用requests库破解
#触发条件后，Ajax会向服务器发送请求，以获取新的数据，为通过requests库获取数据，就需要知道发往服务器接口的真正网址及携带的参数(主要是翻页参数)
#方法2：以触发条件为突破口，用selenium库破解
#通过selenium库破解Ajax的核心是模拟滚动页面的操作，其核心代码如下
#browser.execute_scripe('window.scrollTo(0, document.body.scroll-Height)')
#这行代码利用selenium库的execute_script()函数模拟执行JavaScript代码(JavaScript可在网页中执行动态操作，读者简单了解）。
#这里执行的JavaScript代码是window.scrollTo(0, document.body.scroll-Height)。其中window.scrollTo()函数用于把页面滚动到指定的像素点
#该函数的第一个参数为x轴像素坐标，这里设置为0；第二个参数为y轴像素坐标，这里设置为document.body.scroll-Height，表示目前高度。
#实现的效果就是把页面滚动到已展示区域的最底端。通过不停地向下滚动，就能加载新的内容了。
#方法1不需要打开模拟浏览器，所以爬取速度稍快，但是需要分析真正的请求的网址，得多动一些脑筋。而方法2不需要做额外的分析，实现起来相对比较简单，
#只是爬取速度稍慢。

import requests
import re

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}

def kaiyuan(page):
    url = 'https://www.oschina.net/blog/widgets/_blog_index_recommend_list?p=' + str(page)
    res = requests.get(url, headers=headers).text

    p_title = '<a class="header" href=".*?" target="_blank".*?title="(.*?)">'   # 这里唯一的注意点就是target="_blank"后的.*?（换行）是F12中看不出来的，要在Python获取的源代码res中看
    title = re.findall(p_title, res, re.S)  # 因为有换行，所以要加re.S

    p_href = '<a class="header" href="(.*?)" target="_blank".*?title=".*?">'
    href = re.findall(p_href, res, re.S)

    for i in range(len(title)):
        print(str(i+1) + '.' + title[i])
        print(href[i])

for j in range(1, 10):
    kaiyuan(j)

#补充知识点
#Ajax请求中不同页面网址的规律为
#第一页：https://www.oschina.net/blog/widgets/_blog_index_recommend_list?classification=15&p=1&type=ajax
#第二页：https://www.oschina.net/blog/widgets/_blog_index_recommend_list?classification=15&p=2&type=ajax
#第三页：https://www.oschina.net/blog/widgets/_blog_index_recommend_list?classification=15&p=3&type=ajax
#第n页：https://www.oschina.net/blog/widgets/_blog_index_recommend_list?classification=15&p=n&type=ajax
#网址中第有些参数不是必须第。经过试验，发现网址中只保留p参数也可以访问，因此上面第网址可以简写如下形式
#第n页：https://www.oschina.net/blog/widgets/_blog_index_recommend_list?p=n
#在浏览器中打开简化后第网址，如https://www.oschina.net/blog/widgets/_blog_index_recommend_list?p=1，
#会发现页面第排版和首页一样，但只有20条博客，页面滚动到底部后也不会加载出新到内容。这说明可以用简化后到网址来爬取数据，当然，用完整网址也是没有问题的。
