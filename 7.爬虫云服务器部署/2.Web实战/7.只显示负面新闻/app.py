from flask import Flask, render_template
import pymysql
import datetime
app = Flask(__name__)

today = datetime.datetime.now()
today = today.strftime('%Y-%m-%d')
# today = '2020-11-06'


def database(keyword):
    db = pymysql.connect(host='localhost', port=3306, user='root', password='123456', database='sys', charset='utf8')
    cur = db.cursor()  # 获取会话指针，用来调用SQL语句
    sql = 'select * from article where company = %s and date = %s and score < 100'
    cur.execute(sql, (keyword, today))  # 执行SQL语句
    data = cur.fetchall()  # 提取数据
    cur.close()  # 关闭会话指针
    db.close()  # 关闭数据库链接
    return data


# 汇总新闻
data_all = {}
companys = ['华能信托', '阿里巴巴', '百度']
for i in companys:
    data_all[i] = database(i)

print(data_all)

# 汇总评分
score_all = {}
for key, value in data_all.items():
    score = 0
    # print(value)
    for i in value:
        score += i[5]
    try:  # 防止有的len(value)为0，也就是当日没有新闻
        score = int(score/len(value))
    except:
        score = 0
    score_all[key] = score

print(score_all)


@app.route('/')
def index():
    return render_template('index.html', data_all=data_all, score_all=score_all)


app.run(debug=True)
