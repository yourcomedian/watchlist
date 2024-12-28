from flask import Flask
from markupsafe import escape

# 创建一个程序对象app
app = Flask(__name__)

# 使用装饰器将视图函数与URL绑定
@app.route('/')
def hello():
    return '<h1>欢迎来到我的观看列表！</h1><img src="http://helloflask.com/totoro.gif">'


@app.route('/user/<name>')
def user_page(name):
    return f'User: {escape(name)}<img src="http://helloflask.com/totoro.gif">'