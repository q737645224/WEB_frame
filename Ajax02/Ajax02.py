import json

from flask import Flask, render_template, request
import pymysql
from flask_sqlalchemy import SQLAlchemy

pymysql.install_as_MySQLdb()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:123456@localhost:3306/ajax'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN']=True

db = SQLAlchemy(app)

class Users(db.Model):
  __tablename__ = "users"
  id = db.Column(db.Integer,primary_key=True)
  loginname = db.Column(db.String(30))
  loginpwd = db.Column(db.String(30))
  username = db.Column(db.String(30))

  def to_dict(self):
    dic = {
      'id' : self.id,
      'loginname' : self.loginname,
      'loginpwd' : self.loginpwd,
      'username' : self.username,
    }
    return dic


@app.route('/')
def hello_world():
  return 'Hello World!'

@app.route('/01-allusers')
def allusers():
  return render_template('01-allusers.html')

@app.route('/01-server')
def server01():
  users = Users.query.all()
  str = ""
  for user in users:
    str += user.loginname+user.loginpwd+user.username
  return str

@app.route('/02-json')
def json_views():
  list = ["Fan Bing bing","范冰冰","Li Chen"]

  dic = {
    'name':'Fan Bingbing',
    'age' : 37,
    'gender' : 'female',
  }

  uList = [
    {
      'name':'Mr Wang',
      'age' : 37,
      'gender' : 'male',
    },
    {
      'name' : 'Mrs Wang',
      'age' : 15,
      'gender' : 'female',
    }
  ]

  jsonStr = json.dumps(uList)
  return jsonStr

@app.route('/02-html')
def html_views():
  return render_template('02-json.html')

@app.route('/03-users')
def users():
  return render_template('03-users.html')

@app.route('/03-server')
def server03():
  # 读取users表中id=1的用户的信息
  user=Users.query.filter_by(id=1).first()

  #读取users表中所有的用户信息
  users=Users.query.all()
  list = []
  for u in users:
    list.append(u.to_dict())
  # return json.dumps(user.to_dict())
  return json.dumps(list)

@app.route('/04-users')
def users04():
  return render_template('04-users.html')

@app.route('/04-server')
def server04():
  users=Users.query.all();
  list=[]
  for u in users:
    list.append(u.to_dict())
  return json.dumps(list)

@app.route('/04-delete')
def delete():
  #先获取前端传递过来的id值
  id=request.args.get('id')
  user=Users.query.filter_by(id=id).first()
  try:
    db.session.delete(user)
    dic = {
      'status':1,
      'msg':'删除成功',
    }
  except Exception as e:
    print(e)
    dic = {
      'status':0,
      'msg':'删除失败,请联系管理员'
    }
  return json.dumps(dic)

if __name__ == '__main__':
  app.run(debug=True)
