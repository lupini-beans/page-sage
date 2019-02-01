from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
@app.route('/welcome')
def index():
    return render_template('welcome.html')
