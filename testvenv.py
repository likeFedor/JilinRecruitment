'''from flask import Flask,make_response
app =Flask(__name__)
@app.route('/user/<name>')
def index(name):
	reponse = make_response('hello %s' % name)
	return reponse
if __name__=='__main__':
	app.run()'''
from flask import Flask
from flask.ext.script import Manager
app =Flask(__name__)
manager=Manager(app)
if __name__=='__main__':
	manager.run()
from flask.ext.wtf import Form