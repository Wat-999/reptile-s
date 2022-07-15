from flask import Flask
from flask import render_template  #render是"渲染"的意思，render_template就是渲染模板的意思
app = Flask(__name__)   #创建web应用的flask类的实例


@app.route('/')
def index():
    return render_template('hello.html')  #表示用render_template()函数调用文件夹"templates"中的html文档"hello.html"进行渲染
#有些读者可能会不明白这样做的意义。简单来说，之前制作的html文档的内容都是在代码中写死的，写什么内容就展示什么内容，无法进行动态更新
#二用render_template()函数渲染页面主要就是为了通过前后端交互实现内容的动态更新。


app.run(debug=True)

#1用render_template()函数渲染页面

#上一小节把HTML直接写在主代码文件"flask入门.py"中，但在实战中往往不会这样做，因为实战中通常强调"前后端分离"，也就是不能把HTML等前端代码和
#python后端代码混淆在一起。虽然把前后端代码写在一起并不影响代码运行，但是不利于项目维护，同时也增加了代码等阅读难度
#实战中等做法是创建一个html文档，然后在python代码中调用这个html文档，这样代码既简洁，又方便调试

#1.调用html文档
#要在flask中调用外部等html文档，必须先在代码所在等文件夹下创建一个名为"templates"的文件夹，用来存放html模版文档的，。
#templates是"模板"的意思，表示这个文件夹是用来存放html模版文档的，这个名称是flask框架规定的，不可更改
#然后在文件夹"templates"下新建一个名为"hello.html"的HTML文档(可以先新建一个扩展名为".txt"的文本文件，然后将扩展名改为".html")，
#再用pycharm打开这个html文档，输入如下代码：<h1>Hello wrold</h1>
#这里为了简化演示只写了一行HTML代码，严格来说是不规范的，但并不会影响页面的显示效果。
#如果想写得更加规范，可以加上<!DOCTYPEhtml>、<html>、</html>等标签
#双击这个html文档可以看到网页中显示'Hello World",下面就可以在flask项目的python代码中调用这个HTML文档。