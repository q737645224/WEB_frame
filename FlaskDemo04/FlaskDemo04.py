import os

import datetime
from flask import Flask, render_template, request, make_response, redirect

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/01-js')
def js_views():
    return render_template('01-js.html')

@app.route('/02-get')
def get_views():
    name = request.args['name']
    age = request.args['age']
    return "姓名:%s,年龄:%s" % (name,age)

@app.route('/03-response')
def response_views():
    # resp = make_response('这是使用响应对象创建出来的响应内容')
    resp = make_response(render_template('01-js.html'))
    return resp

@app.route('/04-redirect')
def redirect_views():
    #直接通过重定向的方式，将请求发送给03-response
    return redirect('/03-response')

@app.route('/05-file',methods=['GET','POST'])
def file_views():
    if request.method == 'GET':
        return render_template('05-file.html')
    else:
        # 获取上传的文件
        f = request.files['uimg']
        # 将上传的文件保存至指定的目录处
        # 获取上传的文件的文件名
        # 将文件名修改为当前时间作为名称，再上传
        ftime=datetime.datetime.now().strftime('%Y%m%d%H%M%S%f')
        # 获取文件的扩展名
        ext=f.filename.split('.')[1]
        filename = ftime + '.' + ext


        # 将上传的文件保存至指定目录处[绝对路径]
        basedir = os.path.dirname(__file__)
        upload_path=os.path.join(basedir,'static/upload',filename)
        print('upload_path:'+upload_path)
        f.save(upload_path)

        return "Upload OK"

if __name__ == '__main__':
    app.run(debug=True,port='5001')
