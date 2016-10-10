from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def index():
	return render_template('index.html')
@app.route('/<user>')
def add(user):
	return render_template('add.html',name=user)
def add(one):
	return render_template('one.html',name=one)
def add(two):
	return render_template('two.html',name=two)
def add(three):
	return render_template('three.html',name=three)
if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000, debug = True)
	
	
	
'''
实现flask与Jinja2模板的结合
'''
