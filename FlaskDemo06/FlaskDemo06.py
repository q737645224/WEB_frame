from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

import pymysql
pymysql.install_as_MySQLdb()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']="mysql://root:123456@localhost:3306/flask"
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN']=True
db = SQLAlchemy(app)
# db.init_app(app)


class Course(db.Model):
    __tablename__ = "course"
    id = db.Column(db.Integer,primary_key=True)
    cname = db.Column(db.String(30))
    #增加关联属性和反向引用关系
    #关联属性：在course对象中通过哪个属性能够得到对应的所有的teacher
    #反向引用关系：在teacher对象中通过哪个属性能找到它对应的course
    teachers = db.relationship('Teacher',backref='course',lazy="dynamic")

    def __init__(self,cname):
        self.cname = cname

    def __repr__(self):
        return "<Course:%r>" % self.cname

class Teacher(db.Model):
    __tablename__ = 'teacher'
    id = db.Column(db.Integer,primary_key=True)
    tname = db.Column(db.String(30))
    tage = db.Column(db.Integer)
    #增加一列:course_id,外键列,引用自主键表(course)的主键列(id)
    course_id = db.Column(db.Integer,db.ForeignKey('course.id'))
    #增加关联属性以及反响引用属性
    wife = db.relationship('Wife',backref='teacher',uselist=False)

    def __repr__(self):
        return "<Teacher:%r>" % self.tname

class Wife(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    wname=db.Column(db.String(30))
    wage=db.Column(db.Integer)
    #增加一个列(外键):表示引用自Teacher表的主键
    teacher_id = db.Column(db.Integer,db.ForeignKey('teacher.id'))

    def __init__(self,wname,wage):
        self.wname = wname
        self.wage = wage

    def __repr__(self):
        return "<Wife:%r>" % self.wname



# 同步回数据库
db.create_all()

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/01-addcourse')
def add_course():
    course1 = Course('Python基础')
    course2 = Course('Python高级')
    course3 = Course('数据库基础')
    db.session.add(course1)
    db.session.add(course2)
    db.session.add(course3)
    return "Add Course OK"

@app.route('/02-register-teacher')
def register_teacher():
    teacher = Teacher()
    teacher.tname = '吕老师'
    teacher.tage = 25
    # 通过关联属性赋值
    #先获取一个course对象
    # course=Course.query.filter_by(id=3).first()
    #再将course对象赋值给teacher
    # teacher.course = course
    #最后将teacher保存回数据库

    # 通过已定义的外键course_id赋值
    teacher.course_id = 1
    db.session.add(teacher)
    return "Register Teacher Success!!!"

@app.route('/03-query-teacher')
def query_teacher():
    # 通过course查找对应的所有的老师们
    # 查找course_id为1的course对象
    # course = Course.query.filter_by(id=1).first()
    # print('课程名称:'+course.cname)
    # 查找course对应的所有的teacher们
    # teachers = course.teachers.all()
    # for tea in teachers:
    #     print('教师姓名:'+tea.tname)


    # 通过teacher查找对应的course
    teacher=Teacher.query.filter_by(id=1).first()
    print("教师姓名:"+teacher.tname)
    # 通过teacher的course属性查找对应的course
    course = teacher.course
    print("教授课程:"+course.cname)
    return "Query OK"

@app.route('/04-regTeacher',methods=['GET','POST'])
def regTeacher():
    if request.method == 'GET':
        #查询所有的课程
        courses = Course.query.all()
        #将课程列表发送到04-regTeacher.html上
        return render_template('04-regTeacher.html',courses = courses)
    else:
        #接收前端传递过来的数据
        tname = request.form.get('tname')
        tage = request.form.get('tage')
        course_id = request.form.get('course')
        #将三个数据构建成Teacher对象,再保存回数据库
        teacher = Teacher()
        teacher.tname = tname
        teacher.tage = tage
        teacher.course_id = course_id
        db.session.add(teacher)
        return redirect('/05-showTea')

@app.route('/05-showTea')
def showTea():
    teachers=Teacher.query.all()
    return render_template('05-showTea.html',teachers=teachers)

@app.route('/06-regWife')
def regWife():
    # 通过id赋值
    # wife = Wife('王夫人',18)
    # wife.teacher_id = 1
    # db.session.add(wife)

    # 通过对象赋值
    wife = Wife('魏夫人',15)
    teacher=Teacher.query.filter_by(tname='魏老师').first()
    wife.teacher = teacher
    db.session.add(wife)
    return "Register Wife OK"

@app.route('/07-querywife')
def querywife():
    # 通过teacher找wife
    # teacher = Teacher.query.filter_by(id=1).first()
    # wife = teacher.wife

    # 通过wife找teacher
    wife = Wife.query.filter_by(id=2).first()
    teacher = wife.teacher
    return "老师:%s,夫人:%s" % (teacher.tname,wife.wname)

if __name__ == '__main__':
    app.run(debug=True)
