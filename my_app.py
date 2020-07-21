from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
	return 'Hello IIS from Flask framework.'

@app.route('/Hello')
def hello_world():
	return 'Hello World!'
	
if __name__ == '__main__':
	app.run()
