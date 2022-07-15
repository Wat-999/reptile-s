from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route('/')
def index():
    name = '华小智1'
    return render_template('hello.html', name=name)


app.run(debug=True)

#2传入参数：前后端进行交互
#前面初步演示了render_template()函数的用法，下面对"hello.html"中对前端html代码稍加修改，代码如下：<h1>hello {{name}}</h1>
#这段代码很像原来对html代码，但它其实是一段html模版代码。其中但name位于双层大括号中，不再是一个固定值，而是一个变量，render_template()函数
#会在渲染页面时根据变量name但值(如后端但python代码传来的值)显示不同但内容
#注意：此时如果直接在浏览器中打开hello.html，页面中国显示但会是"Hello {{name}}"，关于html模版文档但语法，只需记住两种特殊符号
#{{}}：作用可以在中间填写变量，      {% %}:作用可以在中间填写if、for等控制语句
#运行代码后，打开网址，可以看到把python文件中定义但变量值传入了html模版文档
#这个例子虽然简单，却蕴含着数据前后端交互但核心原理，之后从数据库获取但舆情数据都会以类似但方式展示在前端页面
#这里但代码和之前但代码但主要区别是在第8行定义里一个变量name，然后在第9行但render_template()函数传入name=name。注意这两个name但含义不同
#等号前面但name对应html模版文档中但变量name，等号后面但name则对应python文件中定义的变量name
#假设将第8行的变量名改为hhh，则第9行也要相应改为name=hhh
#同理，如果在html模版文档中更改里变量名，则在python代码中也要做相应更改
#如果相传递多个参数，例如，"hello.html"的内容为<h1>Hello {{name}},{{age}}</h1>,
#那么在render_template()函数中传入两个参数name和age即可，代码如下：
# name = '华小智'
# age = '28'
# return render_template('hello.html', name=name, age=age)

#此外，可以通过在app.run()中传入参数debug=true来激活调试模式，这样每次修改代码后无须重新启动项目，直接刷新网页就可以看到更新结果。
#例如，读者可以把"华小智"改成自己的名字，然后无须重新运行代码，直接刷新网页，就能看到内容已自动更新
#如果页面中的中文显示为乱码，可以在html模版文档中添加<head>标签并设置编码格式，代码如下：

# <!DOCTYPE html>
# <html>   #36、37行以及最后的一行<html>是一种固定的标准写法，用于声明这是一个html文档
# <head>  #头部信息，用<head>标签定义，主要用来设置编码格式等内容
#     <meta charset="utf-8">  #设置编码格式   如果出现乱码，则将utf-8改为gbk c
# </head>     #html代码里的注释格式为：<!-- 在这里面可以添加注释 -->
# <body>  #用<body> 标签定义，主要是网页的具体内容
#     <h1>Hello {{ name }}</h1>
# </body>
# </html>