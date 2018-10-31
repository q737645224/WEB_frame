from flask import Flask

#将当前运行的主程序构建成Flask应用，以便接收用户的请求（request）并给出响应（response）
app =Flask(__name__)

# @app.route() Flask中的路由定义，主要定义用户的访问路径、'/表示的是整个网站的根路径
#def index(),表示的是匹配上@app.route()路径后的处理程序，视图函数。
#所有的视图函数必须要有return, return后面可以是一个字符串也可以是一个独立的响应对象
# @app.route("/")
# def index():
#     return "<h1>what is you name, where you are?<h1>"

@app.route('/login')
def login():
    return '欢迎访问登录页面'
@app.route('/register')
def register():
    return '欢迎访问注册页面' 

if __name__ =="__main__":
    #运行flask应用（启动flask服务），默认在本机开启的端口是5000
    #debug=True,将启动模式更改为调试模式(开发环境中推荐些True， 生产环境中必须写Flase)
    app.run(debug=True)