from flask import Flask, render_template
import pymysql
app = Flask(__name__)


def database(keyword):  #定义一个函数，方便之后从数据库中批量获取不同公司的数据
    db = pymysql.connect(host='localhost', port=3306, user='root', password='123456', database='sys', charset='utf8')
    cur = db.cursor()  # 获取会话指针，用来调用SQL语句
    sql = 'select * from article where company = %s' #%s表示占位符号
    cur.execute(sql, keyword)  # 执行SQL语句  keyworld赋值给占位符号
    data = cur.fetchall()  # 提取数据
    cur.close()  # 关闭会话指针
    db.close()  # 关闭数据库链接
    return data  #设置函数的返回值，即指定公司的所有新闻数据


data_all = {}   #创建一个空字典，然后用for循环语句循环遍历companys中公司的名称
companys = ['华能信托', '阿里巴巴', '百度']
for i in companys:
    data_all[i] = database(i)  #调用database()函数获取指定公司的数据
    #data_all[i] 表示以公司名称i作为键，指定公司的新闻数据database(i)作为值，存入字典data_all


@app.route('/')
def index():
    return render_template('index.html', data_all=data_all)  #将字典data_all传入HTML模版文档


app.run(debug=True)
