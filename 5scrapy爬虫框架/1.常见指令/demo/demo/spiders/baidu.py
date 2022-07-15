import scrapy


class BaiduSpider(scrapy.Spider):
    name = 'baidu'
    allowed_domains = ['baidu.com']
    start_urls = ['http://baidu.com/']

    def parse(self, response):
        print(response.text)
        pass
 #属性和方法                     含义
# name                     爬虫文件名
# allowed_domains         允许爬取的域名区域
# start_urls              爬取的初始网址
# parse                   用于实现爬虫逻辑的函数
#其中name、allowed_domains、start_urls 、parse 属性的内容都市随"scrapy genspider baidu baidu.com"这一指令自动生成的
#name和allowed_domains 属性分别对应爬虫文件"baidu.py"和域名baidu.com。经过尝试后发现，其实scrapy并没有很严格地限制允许爬取的域名
#域名不是baidu.com的网站也能获取，所以这两个属性简单理解即可
#start_urls 属性是初始的默认爬取网址，可以修改成自定义的内容，如百度新闻的相关网址
#pase()函数用于实现爬虫逻辑，是代码编写工作的重点。该函数有两个默认参数self和response：self为在类中定义函数的固定格式，简单了解即可
#response则是scrapy框架获取的网络响应，比较重要
#目前parse()函数中只有pass语句，表示什么也不做。现在为parse()函数添加功能代码，尝试获取百度首页的网络响应，那么response.text就是获取
#网页源代码。添加代码后，parse()函数已经具备具体功能，其实可以把pass语句删除，这里还是先保留着，不影响代码的执行



#scrapy的常用指令
#指令                                           作用
#scrapy startproject xxxx(项目名)             创建爬虫项目
#cd xxx(项目名)                                进入爬虫项目
#scrapy genspider xxxx(爬虫名) xxxx.com(域名)   创建具体的爬虫文件
#scrapy crawl xxx(爬虫名)                       运行爬虫项目

#scrapy爬虫项目是由多个python文件组成的，这里的"baidu.py"其实和其他python文件有关联。如果只运行这一个文件，并不能真正启动爬虫项目。
#在scrapy中，应该使用指令"scrapy crael xxx(项目名)"来执行爬虫项目。这里的爬虫名为"baidu"，那么对应的指令为"scrapy crael baidu"
#有两种方法来执行指令，一中在pycharm的终端中执行(前提是用终端里写命令创建的项目),一种在命令窗口中执行即外面的终端
#还有一种：在pycharm中通过python文件启动爬虫项目
#1在文件夹"spiders"同级文件夹中新建python文件"main.py"
#2然后在文件中输入代码
#from scrapy import cmdline     导入cmdline模块来执行命令行指令
#cmdline.execute("scrapy crawl 爬虫名".split())    用split(）函数根据空格拆分指令字符串，再用execute()函数输入到命令行中执行，
#相当于直接在终端中执行指令"scrapy crawl 爬虫名"


#Robots协议破解
#运行爬虫项目时遇到来提示"DEBUG`````"说明百度的robots协议禁止scrapy框架直接爬取，要破解robots协议，首先得了解什么是robots协议。
#robots协议的全称是"网络爬虫排除标准"，又称为爬虫协议、机器人协议等。网站通过robots协议高速爬虫引擎哪些页面可以爬取，哪些页面不能爬取
#通过在网址后添加"/robots.txt"，可以查看网站的robots协议内容。百度的robots协议里面列出来禁止哪些爬虫引擎爬取哪些页面(Disallow是禁止的意思)

#robots协议的破解方法很简单。1打开爬虫项目的设置文件'setting.py" 2找到第20行左右的变量ROBOTSTXT_OBEY 把原来的True改成False即可
#OBEY意为遵守，将变量ROBOTSTXT_OBEY设置为False就表示不遵守robots。


#user-Agent设置
#在requests库中，user-Agent是在headers参数中设置的。在scrapy框架中，user-Agent则是在设置文件中设置。
#1打开爬虫项目的设置文件'setting.py" 2找到第40行左右选中DEFAULT_REQUEST_HEADERS = {
  # 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
  # 'Accept-Language': 'en',这几行代码，按快捷键"cmd+/"取消注释
  #其中DEFAULT_REQUEST_HEADERS意为"默认请求头"将其激活，也就是给爬虫添加请求头。其设置方法和requests库的headers参数是一样的。
  #我们在里面添加一行user-Agent代码：'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36',

#通常建议在爬虫项目设置文件中把robots协议相关代码设置为false，并添加一个'User-Agent'，这样能绕过一些潜在的反爬手段。
#当然，又很多网站不需要设置这两项也能爬取。