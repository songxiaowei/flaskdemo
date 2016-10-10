from flask import Flask,render_template
app = Flask(__name__)
@app.route('/')
def index():
	return render_template('luyou.html')
if __name__ == '__main__':
	app.run(host='0.0.0.0',port=5000,debug = True)
	
'''
静态路由的功能实现
实际意义：寻找文件，路由的意思就是迷茫中寻找出路
'''
