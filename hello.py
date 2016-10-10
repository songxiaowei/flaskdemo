from flask import Flask
from flask_script import Manager
app = Flask(__name__)
@app.route('/')
def index():
	return '<h1>hello flask</h1>'
if __name__ == '__main__':
	app.run()
	
	
'''
* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
原因是默认启动侦听的ip是127.0.0.1,只能是在本地服务器上的浏览器能正常打开，怎么解决?
'''
