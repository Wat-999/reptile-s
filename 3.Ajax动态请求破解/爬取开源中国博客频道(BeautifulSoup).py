import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}


def kaiyuan(url):
    res = requests.get(url, headers=headers).text
    # print(res)

    soup = BeautifulSoup(res, 'html.parser')  # 文档对象  html.parser参数表示的是解析器
    title = soup.select('.blog-item.content.header')
    #title = soup.select('.header')  两者等同
    #用开发者工具观察网页源代码中标签的嵌套关系(圈选整个大块)，发现标题和网址都在"class属性值为blog-item的<div>标签-class属性值为content的
    #<div>标签-class属性值为header的<a>标签"这个嵌套结构中，由此编写出第13行代码(最好写得严格一些，否则容易匹配到不需要的内容）

    for i in range(len(title)):
        print(str(i + 1) + '.' + title[i].get_text().strip().replace('原', '').replace('荐', '').replace('转',
                                                                                                       '').strip())  # 也可以拆开写
        #用get_text()函数获取文本内容，此时的文本内容中含有多余的"原""荐"等字符(有时还会有字符"转"),因此连续用replace()函数把
        #这些字符串替换为空字符串。再用strip()函数删除字符串首尾的空格和换行。
        print(title[i]['href'])


for i in range(1, 10):
    url = 'https://www.oschina.net/blog/widgets/_blog_index_recommend_list?classification=0&type=ajax&p=' + str(i)
    kaiyuan(url)