from flask import Flask

app = Flask(__name__)

#http://localhost:5000/login
# @app.route("/login")
# def login():
#     return "<h1>欢迎访问登录界面</h1>"

@app.route('/category')
@app.route('/cate')
def show_name_age():
    return "你好"

@app.route("/")
@app.route("/index")
@app.route("/<number>")
@app.route("/index/<number>")
def num(number=1):
    return "页数为%s"%number

if __name__ == "__main__":
    app.run(debug=True)