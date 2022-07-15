import scrapy
from xinlang.items import XinlangItem  # 引入刚刚创建的Item内容
from bs4 import BeautifulSoup

class XinaSpider(scrapy.Spider):
    name = 'xina'  #爬虫文件名
    allowed_domains = ['xina.com']   #域名
    start_urls = ['https://news.sina.com.cn/gov/2020-09-28/doc-iivhuipp6876829.shtml']  #要爬取的网址

    def parse(self, response):
        item = XinlangItem()  # 激活Item（专业的说法叫实例化对象，了解即可）即就是前面导入的类
        #XinlangItem为实体文件中定义的类，在编写其他爬虫项目时，需要根据实际的项目名和类名修改这行代码
        soup = BeautifulSoup(response.text, 'html.parser')  # BS提取内容
        item['title'] = soup.select('.main-title')[0].text  # 提取标题
        item['source'] = soup.select('.source')[0].text  # 提取来源
        item['time'] = soup.select('.date')[0].text  # 提取日期
        yield item  # 如果这个函数之后没有内容的话，其实用return也可以，可自行尝试下
#用BeautifulSoup库解析网页源代码，根据class属性值选取网页元素

#首先要注意，response.text才是网页源代码，所以第13行代码中为BeautifulSoup()传入response.text，第14～16行代码先用select()函数
#根据class属性值选取网页元素，例如soup.select('.main-title')[0].text 表示选取class属性值为"main-title"的网页元素，这里因为只有
#一条新闻，所以接着通过[0]提取列表中第一个也是唯一一个网页元素，再通过text属性提取网页元素的文本。
#提取文本后，需要通过赋值给item['title']的方式把提取结果传入实体文件，其中title、source、time都是在实体文件中创建的变量，
#最后一行代码通过yield item返回获取的内容：
#学到这里，读者可能会产生两个疑问：
#1为什么要把提取结果传入实体文件？这是因为实体文件类似一个数据中转站，要通过实体文件和其他文件进行交互，例如之后会和管道文件进行交互，
#在管道文件中进行数据存储等操作

#2为什么最后设置函数返回值用的是yield item 而不是return item？这个问题将在补充知识点中回答
#运行结果总，可以成功看到爬取了新闻的来源、日期、和标题，还可以看到item是一个字典，之前编写的source、title、time作为字典的键，爬取结果作为字典的值
#这里至爬取了一条新闻，所以字典的值是一个字符串；如果又多个爬取结果，那么字典的值会是由多个结果组成的列表

#补充知识点
#对于yield和return的区别，我们无序了解太深，值需要知道函数在执行过程中如果遇到return xxx语句，就会返回相应内容，并且不再执行函数内该语句之后的代码
#而如果遇到yield xxx语句，则会在返回相应内容后继续执行函数内该语句之后的代码

#假设定义了两个函数y(x)和z(x)，其中y(x)使用return x，z(x)使用yield x,代码如下
# def y(x):
#     x = x +1
#     return x
#     print('这里使用是return')
#
# def z(x):
#     x = x - 1
#     yield x
#     print('这里使用的是yield')
#
# #通过如下代码来调用函数：
# a = y(1)
# print(a)
#
# b = z(1)
# for i in b:    #yield会产生一个生成器，需要用for循环语句遍历内容
#     print(i)
#

#可以看到，y(x)函数执行完return x后，不再执行后面的print(),而z(x)函数执行完后yield x后，还会继续执行后面的print().
#不过需要注意，yield会产生一个迭代器(一种可迭代对象，类似于range()函数产生的对象)，需要通过for循环语句遍历其内容
#scrapy框架中之所以要用yield item，是因为在一些复杂的爬虫项目中，需要在parse()函数中写很多代码，用yield item可以不间断地执行代码，
#在循环获取数据时比价有效。本章的爬虫项目并不复杂，用return item也是可以的