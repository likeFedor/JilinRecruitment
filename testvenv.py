from flask import Flask,make_response

app =Flask(__name__)
@app.route('/user/<name>')
def index(name):
	reponse = make_response('hello %s' % name)
	return reponse
if __name__=='__main__':
	app.run()
