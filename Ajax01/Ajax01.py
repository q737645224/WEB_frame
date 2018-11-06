from flask import Flask, render_template, request

import pymysql
from flask_sqlalchemy import SQLAlchemy

pymysql.install_as_MySQLdb()

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']="mysql://root:123456@localhost:3306/ajax"
db = SQLAlchemy(app)

class Users(db.Model):
  id = db.Column(db.Integer,primary_key=True)
  loginname = db.Column(db.String(30))
  loginpwd = db.Column(db.String(30))
  username = db.Column(db.String(30))

db.create_all()

@app.route('/01-xhr')
def xhr():
    return render_template('01-xhr.html')

@app.route('/02-ajax-get')
def ajax_get():
    return render_template('02-ajax-get.html')

@app.route('/02-server')
def server02():
    return "这是我的第一个ajax请求"

@app.route('/03-get-params')
def get_params():
  return render_template('03-get-params.html')

@app.route('/03-server')
def server03():
  uname = request.args.get('uname')
  return "欢迎:%s" % uname

@app.route('/04-post')
def post():
  return render_template('04-post.html')

@app.route('/04-server',methods=['POST'])
def server04():
  uname = request.form['uname']
  age = request.form['age']
  return "姓名:%s,年龄:%s" % (uname,age)

@app.route('/05-form')
def form():
  return render_template('05-form.html')

@app.route('/06-register')
def register():
  return render_template('06-register.html')

@app.route('/06-server')
def server06():
  # 接收前端传递过来的参数 - lname
  lname=request.args.get('lname')
  # 以lname作为条件，通过Users实体类查询数据
  user=Users.query.filter_by(loginname=lname).first()
  # 如果查询出来了数据的话则说明登录名称已存在，否则通过
  if user:
    return "用户名称已存在"
  else:
    return "通过"

if __name__ == '__main__':
    app.run(debug=True)
