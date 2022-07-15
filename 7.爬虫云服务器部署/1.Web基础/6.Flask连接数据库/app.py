from flask import Flask, render_template
import pymysql
app = Flask(__name__)

db = pymysql.connect(host='localhost', port=3306, user='root', password='', database='pachong', charset='utf8')
cur = db.cursor()  # 获取会话指针，用来调用SQL语句
sql = 'select * from test where company = "阿里巴巴"'
cur.execute(sql)  # 执行SQL语句
data = cur.fetchall()  # 提取数据
cur.close()  # 关闭会话指针
db.close()  # 关闭数据库链接
print(data)


@app.route('/')
def index():
    return render_template('index.html', data=data)


app.run(debug=True)
