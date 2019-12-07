from flask import render_template
from flask import Flask
from app import app

app = Flask(__name__)

@app.route('/')
@app.route('/index')

def index():
	user = {'name': 'Antonio'}
	return render_template('index.html', title = 'Home', user = user)
