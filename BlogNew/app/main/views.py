import datetime
import os

from flask import render_template, request, session, redirect
#导入蓝图程序-main,用于构建路由
from . import main
#导入db以及models下的类
from .. import db
from ..models import *
#首页的访问路由


@main.route('/')
@main.route('/index')
def index():
    categories = Category.query.all()
    topics = Topic.query.all()
    #获取登录信息
    if 'uid' in session and 'uname' in session:
        user= User.query.filter_by(id=session.get('uid')).first()
    return render_template('index.html',params = locals())

@main.route('/login',methods=['get','post'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        #接受前段传递过来的数据
        loginname = request.form['username']
        upwd = request.form['password']
        #使用接受的数据去数据库验证,查询
        user = User.query.filter_by(loginname=loginname,upwd=upwd).first()
        #如果用户存在,则将数据保存至session
        if user:
            #登录成功
            session['uid'] = user.id
            session['uname'] = user.uname
            return redirect('/')
        else:
            #登录失败
            errMsg = '用户名或密码不正确'
            return render_template('login.html',errMsg=errMsg)

@main.route('/logout')
def logout():
    #获取源地址,有源地址的话返回到源地址

    url = request.headers.get('referer','/')
    print("源地址:"+url)
    #判断登录信息是否在session中
    if 'uid' in session and 'uname' in session:
        session.clear()
    return redirect('/')

@main.route('/release',methods=['GET','POST'])
def release():
    if request.method == 'GET':
        #实现权限的验证(是否登录,是否为作者)

        #判断用户是否在登录状态上,如果登录了,则继续向下判断,否则去往登录页
        if 'uid' in session and 'uname' in session:
            #继续判断是否为作者
            user = User.query.filter_by(id = session.get('uid')).first()
            if user.is_author !=1:
                return redirect('/')
            else:
                categories = Category.query.all()
                blogtypes = Blogtype.query.all()
                return render_template('release.html',params=locals())
        else:
            #去往登录页
            return redirect('/login')
    else:
        #讲发表的博客信息保存进数据库
        topic = Topic()
        topic.title = request.form.get('author')
        topic.blogtype_id = request.form.get('list')
        topic.category_id= request.form.get('category')
        topic.user_id = session.get('uid')
        topic.content = request.form.get('content')
        topic.pub_date = datetime.datetime.now().strftime("%Y%m%d")
        if request.files:
            print('有文件上传')
            f = request.files['picture']
            ftime = datetime.datetime.now().strftime('%Y%m%d%H%M%S%f')
            ext = f.filename.split('.')[1]
            filename = ftime+'.'+ext
            topic.images = "upload/"+filename
            #将文件保存至服务器
            basedir = os.path.dirname(os.path.dirname(__file__))
            print(basedir)
            upload_path = os.path.join(basedir,'static/upload',filename)
            print(upload_path)
            f.save(upload_path)
        db.session.add(topic)
        return "OK"

@main.route('/info')
def info():
    #接受前端传递过来的id
    id = request.args.get('id')
    #再根据id的值查询一个博客
    topic = Topic.query.filter_by(id=id).first()

    return render_template('info.html',params = locals())














@main.route('/about')
def about():
    return render_template('about.html')

@main.route('/footer')
def footer():
    return render_template('footer.html')

@main.route('/gbook')
def gbook():
    return render_template('gbook.html')

@main.route('/header')
def header():
    return render_template('header.html')


@main.route('/list')
def list():
    return render_template('list.html')

@main.route('/photo')
def photo():
    return render_template('photo.html')

@main.route('/register',methods=['get','post'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    else:
        return 'Success'



@main.route('/time')
def time():
    return render_template('time.html')

