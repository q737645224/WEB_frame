from flask import render_template
#导入蓝图程序-main,用于构建路由
from . import main
#导入db 以及 models们
from .. import db
from ..models import *

#首页的访问路由
@main.route('/')
def index_views():

    return render_template('index.html')

