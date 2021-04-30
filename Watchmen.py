from flask import Flask,request,render_template

Watchmen = Flask(__name__)

@Watchmen.route('/')
@Watchmen.route('/index')
def index():
	f = open("/home/tge/Watchmen/donne.log")
	file = f.read()
	return file
        #return render_template("patron.html")
@Watchmen.route('/')
@Watchmen.route('test')
def teste():
	a = "alllo sa marche pas"
	return a
