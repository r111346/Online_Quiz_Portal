from flask import Flask, render_template, redirect, url_for, request, make_response
from ums import ums
import requests as rq
app = Flask(__name__)

@app.route('/',methods=['POST','GET'])
def login():
    resp = make_response(render_template('login.html', error=error))
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
