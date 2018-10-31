from flask import Flask, render_template


app = Flask(__name__)

@app.route('/template')
def template():
    # html = render_template('01-template.html')
    # print(html)
    # return html

    #渲染01-template.html，并传递变量
    # dic = {"name":'绿光', "zuoqu":"宝强", "zuoci":"乃亮", "geshou":"羽凡"}

    name = '绿光'
    zuoqu = "宝强"
    zuoci = "乃亮"
    geshou= "羽凡"

    # locals() 将当前函数的局部变量封装为一个字典

    return render_template('01-template.html', params=locals())


class Person(object):
    name = None

    def say(self):
        return 'hell im a person'


#目的：能够传递到模板中作为变量的数据类型都有
@app.route("/02-var")
def var():
    bookName = "钢铁是怎样炼成的"
    author = "奥斯特罗夫斯基"
    price = 32.5
    list = ['漩涡鸣人', '卡卡西', '自来也', '佐助']
    tup = ('水浒传', '三国演义', '红楼梦', '西游记')
    dic = {
        'wmz' : '老魏',
        'wwc' : '隔壁老王',
        'Lz' :'卢泽',
        'MM' : '蒙蒙'
    }
    person = Person()
    # print(locals())
    person.name = '狮王.金毛'
    person.song = "鲁光"
    return render_template('02-var.html', params=locals())


@app.route('/03-if')
def Myif():
    return render_template('03-if.html')

@app.route("/user/login")
def login():
    return "模拟登陆"

@app.route('/for')
def for_view():
    list = ('你的名字', "心之声", "天空之城", "龙猫")
    dict = {"天空之城":'宫崎骏', '龙猫' : '宫崎骏' }
    return render_template("04-for.html", params = locals())

if __name__ == "__main__":
    app.run(debug=True)