from wsgiref.handlers import read_environ
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/aboutme')
def aboutme():
    return render_template('aboutme.html')

@app.route('/work')
def work():
    return render_template('work.html')

if __name__ == '__main__':
    app.run(debug=True)