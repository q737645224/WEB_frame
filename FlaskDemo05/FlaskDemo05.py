from flask import Flask, request, render_template, redirect
from flask_sqlalchemy import SQLAlchemy

import pymysql
from sqlalchemy import or_, func

pymysql.install_as_MySQLdb()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:123456@localhost:3306/flask'
#指定执行完操作后自动提交
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN']=True
db = SQLAlchemy(app)

#创建模型类-Models
#创建Users类,映射到数据库中叫users表
#创建字段:id,主键和自增
#创建字段:username,长度为80的字符串,不允许为空,值必须唯一
#创建字段:age,整数,允许为空
#创建字段:email,长度为120的字符串,必须唯一
class Users(db.Model):
    __tablename__ = "users"
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(80),nullable=False,unique=True)
    age=db.Column(db.Integer,nullable=True)
    email=db.Column(db.String(120),unique=True)

    def __init__(self,username,age,email):
        self.username = username
        self.age = age
        self.email = email

    def __repr__(self):
        return "<Users:%r>" % self.username

class Student(db.Model):
    __tablename__ = 'student'
    id = db.Column(db.Integer,primary_key=True)
    sname = db.Column(db.String(30))
    sage = db.Column(db.Integer)

class Teacher(db.Model):
    __tablename__ = 'teacher'
    id = db.Column(db.Integer,primary_key=True)
    tname = db.Column(db.String(30))
    tage = db.Column(db.Integer)

class Course(db.Model):
    __tablename__ = 'course'
    id = db.Column(db.Integer,primary_key=True)
    cname=db.Column(db.String(30))

#删除已创建的表结构
# db.drop_all()
#将创建好的实体类映射回数据库
db.create_all()


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/01-insert')
def insert_views():
    #创建Users对象并赋值
    # users = Users('王老师',32,'wangwc@163.com')
    #将对象通过db.session.add() 插入到数据库
    # db.session.add(users)
    #提交插入操作
    # db.session.commit()

    #创建Users对象并赋值
    users = Users('魏老师',40,'laowei@163.com')
    db.session.add(users)
    return "Insert Success"

@app.route('/02-register',methods=['GET','POST'])
def register_views():
    if request.method == 'GET' :
        return render_template('02-register.html')
    else:
        #接收前端传递过来的数据
        username=request.form.get('username')
        age = request.form.get('age')
        email = request.form.get('email')
        #构建Users的对象
        users = Users(username,age,email)
        #通过db.session.add将对象插入到数据库中
        db.session.add(users)
        return "Register OK"

@app.route('/03-query')
def query_views():
    #　测试query()函数
    # print(db.session.query(Users))
    # print(db.session.query(Users,Course))
    # print(db.session.query(Users.username,Users.email))

    # 查询执行函数 - all()
    # users = db.session.query(Users).all()
    # for user in users:
    #     print("姓名:%s,年龄:%d,邮箱:%s" % (user.username,user.age,user.email))

    #查询执行函数 - first() , count()
    # query = db.session.query(Users)
    # user = query.first()
    # print(user)
    # count = query.count()
    # print("共有%d条数据" % count)

    # 查询过滤器函数 - filter()
    # 查询年龄大于30的Users的信息
    # result = db.session.query(Users).filter(Users.age>30).all()

    # 查询年龄大于30并且id大于1的Users的信息
    # result = db.session.query(Users).filter(Users.age>30,Users.id>1).all()

    # 查询年龄大于30或id大于1的Users的信息
    # result=db.session.query(Users).filter(or_(Users.age>30,Users.id>1)).all()

    # 查询email中包含'w'的Users的信息 - 模糊查询like()
    # result = db.session.query(Users).filter(Users.email.like('%w%')).all()

    # 查询Users中所有的age的总和 - 聚合函数
    # result=db.session.query(func.avg(Users.age)).all()

    # 查询id在2,3之间的Users的信息
    # result = db.session.query(Users).filter(Users.id.in_([2,3])).all()

    #　使用filter_by　查询　id=2　的Users的信息
    # result = db.session.query(Users).filter_by(id=2).first()

    # 使用　limit 和　offset 查询限制行数据
    # result = db.session.query(Users).limit(2).all()
    # result = db.session.query(Users).limit(2).offset(1).all()

    # 使用　order_by　排序，先按照年龄升序排序，再按照id降序排序
    result = db.session.query(Users).order_by("age asc,id desc").all()
    print(result)
    return "Query OK"

@app.route('/03-queryall')
def queryall_views():
    users = db.session.query(Users).all()
    return render_template('03-queryall.html',users = users)

@app.route('/04-update',methods=['GET','POST'])
def update_views():
    if request.method == 'GET':
        # 接收前端传递过来的用户id
        id = request.args.get('id','')
        # 根据id将对应的用户的信息读取出来
        # user = db.session.query(Users).filter(Users.id==id).first()
        user = db.session.query(Users).filter_by(id=id).first()
        # 将读取出来的实体对象发送到04-update.html上显示
        return render_template('04-update.html',user=user)
    else:
        # 接收前端传递过来的四个值(id,username,age,email)
        id = request.form.get('id')
        username = request.form.get('username')
        age = request.form.get('age')
        email = request.form.get('email')
        # 根据id查询出对应的user的信息
        user=Users.query.filter_by(id=id).first()
        # 将username,age,email的值分别再赋值给user对应的属性
        user.username = username
        user.age = age
        user.email = email
        # 将user的信息保存回数据库
        db.session.add(user)
        # 响应：重定向回/03-queryall
        return redirect('/03-queryall')

@app.route('/05-query')
def query05_views():
    #使用 Models 查询数据
    # user=Users.query.filter(Users.id==1).first()
    user = Users.query.filter_by(id=3).first()
    print(user)
    return "Query OK"

@app.route('/06-delete')
def delete_views():
    id = request.args.get('id')
    user=Users.query.filter_by(id=id).first()
    db.session.delete(user)
    return redirect('/03-queryall')


if __name__ == '__main__':
    app.run(debug=True)
