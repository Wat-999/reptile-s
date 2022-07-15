from flask import Flask
from flask import render_template   #导入渲染模版
app = Flask(__name__)


@app.route('/')
def index():
    name = ['华小智', '百度', '阿里巴巴']  #设置变量
    return render_template('hello.html', name=name)


app.run(debug=True)  #激活调试模式
#循环语句
#前面演示的网页比较简单，只有一行内容。如果要显示多行类似的内容，可将html代码复制多次再分别修改，但这样显得很烦琐。
#在html模版文档里通过{% %}符号可以调用for循环语句，从而通过简短的代码显示多条内容。将"hello.html"的内容修改成如下代码：
# {% for i in name %}
#     <h1>Hello {{ i }}</h1>
# {% endfor %}
#可以看到这里的for循环语句和python的for循环语句类似，主要区别是在HTML模版文档中需要用{% %}包围if、for等控制语句，
#用{{ }}包围要显示的变量，并且还需要用endfor结束循环
#修改完前端的HTML模版文档，接着修改后端的python文件
#和之前代码唯一的区别是第7行name不是一个简单的字符串，而是一个列表。把这个列表传入html模版文档中后，flask就会通过HTML代码中的for循环语句
#批量调取列表的元素；运行代码后得到的网页内容可以看到for循环语句依次调取来列表的所有元素并渲染在页面中。
