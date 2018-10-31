from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def hello_world():
    return 'Hello World!'


@app.route("/01-static")
def tatic_views():
    url = url_for("static", filename='images/wxy.jpeg')
    print(url)
    return render_template("01-static.html")

#访问路径。。。02-parent
@app.route('/02-parent')
def parent_views():
    return render_template("02-parent.html")

@app.route("/03-child")
def child_views():
    return render_template("03-child.html")

@app.route("/04-request")
def request_views():
    # print(dir(request))
    #获取请求方案（协议）
    scheme = request.scheme
    #获取请求方式
    method = request.method
    #获取get请求方式的请求数据
    args = request.args
    #获取post请求的方式的请求数据
    form = request.form
    #获取cookies中的信息
    cookies = request.cookies
    #获取请求路径（不带参数）

    path = request.path

    full_path = request.full_path

    url = request.url

    headers = request.headers

    return render_template("04-request.html", params = locals())


@app.route("/05-form-get")
def form_get():
    return render_template('05-form-get.html')

@app.route("/06-get")
def get_views():
    print(request.args)
    uname = request.args['uname']
    upwd = request.args['upwd']
    print(uname, upwd)
    return "06get"

# @app.route('/07-form-post')
# def form_post():
#     return render_template("07-form-post.html")
#
# @app.route("/07-post",methods=["POST"])
# def post_views():
#     print(request.form)
#     return 'get-post'



@app.route("/07-post",methods=["POST"])
@app.route('/07-form-post', methods=["GET", "POST"])
def form_post():
    if request.method == "GET":
        return render_template("07-form-post.html")
    else:
        print(request.form)
        return 'get-post'

if __name__ == "__main__":
    app.run(debug=True)