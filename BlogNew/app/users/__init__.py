from flask import Blueprint
users = Blueprint('users',__name__)  #相当于 app = Flask(__name__)
from . import views
