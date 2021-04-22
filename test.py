from flask import Flask,request,render_template

test = Flask(__name__)

@test.route('/')
@test.route('/index')
def index():
	f = open("/home/tge/test/donne.log")
	file = f.read()
	return file
       # return render_template("patron.html")
