from flask import Flask
#将SQLAlchmey模块导入进来
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
#为app指定数据库的配置信息
app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:123456@localhost:3306/flask'
#创建SQLAlchemy的实例，并将app指定给实例
#db是SQLAlchemy的实例，表示的是程序正在使用的数据库，同时db也具备SQLAlchemy中的所有功能
db = SQLAlchemy(app)

@app.route('/')
def index():
    return "Hello World"

if __name__ == "__main__":
    app.run(debug=True,port=5001)