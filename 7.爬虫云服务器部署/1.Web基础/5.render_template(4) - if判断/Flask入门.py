from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route('/')
def index():
    name = '华小智'
    return render_template('hello.html', name=name)  #用render_template调用html文件，调用变量name参数


app.run(debug=True)  #debug=True激活调试模式
#4判断语句
#python中的if判断语句的主要区别是要用{% %}包围语句，并且要用endif结束判断
# {% if name == '华小智' %}
#     <h1>Hello, 主人</h1>
# {% else %}
#     <h1>Hello {{ name }}</h1>
# {% endif %}
#上述代码的逻辑是，如果在python文件中传入的值是'华小智'，那么网页上显示的是"Hello，主人"，否则，显示"Hello传入值"