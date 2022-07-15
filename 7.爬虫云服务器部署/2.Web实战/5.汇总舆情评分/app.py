from flask import Flask, render_template
import pymysql
app = Flask(__name__)


def database(keyword):
    db = pymysql.connect(host='localhost', port=3306, user='root', password='123456', database='sys', charset='utf8')
    cur = db.cursor()  # 获取会话指针，用来调用SQL语句
    sql = 'select * from article where company = %s'
    cur.execute(sql, keyword)  # 执行SQL语句
    data = cur.fetchall()  # 提取数据
    cur.close()  # 关闭会话指针
    db.close()  # 关闭数据库链接
    return data


# 汇总新闻
data_all = {}
companys = ['华能信托', '阿里巴巴', '百度']
for i in companys:
    data_all[i] = database(i)  #调用database()函数获取指定公司的数据
    # data_all[i] 表示以公司名称i作为键，指定公司的新闻数据database(i)作为值，存入字典data_all

# print(data_all)

# 汇总评分
score_all = {}
for key, value in data_all.items():
    score = 0
    # print(value)
    for i in value:
        score += i[5]  # 也可以写成score = score + i[5]
    try:  # 通过try except语句防止相关公司没有新闻，导致len(value)=0，然后产生X/0，但是0不能为除数的报错
        score = int(score/len(value))
    except:
        score = 100
    score_all[key] = score  #用key或value结果都一样， 只是赋值

print(score_all)



@app.route('/')
def index():
    return render_template('index.html', data_all=data_all, score_all=score_all)


app.run(debug=True)
