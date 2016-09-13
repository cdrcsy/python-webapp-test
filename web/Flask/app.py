#!/usr/bin/env python
# coding:utf-8

from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/',methods = ['GET','POST'])
def home():
    return '<h1>Home</h1>'

@app.route('/signin',methods = ['GET'])
def signin_from():
    return '''<form action="/signin" method="post"
            <p><input name="username"></p>
            <p><input name="password"></p>
            <p><button type="submit">Signin</button></p>
            </from>'''

@app.route('/signin',methods=['POST'])
def signin():
    if request.form['username'] == 'admin' and request.form['password'] == 'password':
        return '<h3>Hello,admin!</h3>'
    return '<h3>Bad username or password.</h3>'

if __name__ == "__main__":
    app.run('0.0.0.0',5000)


'''
注意：<form action="/signin" 这里，是form否则下面
request.form['username']则匹配不到。无法返回。
'''