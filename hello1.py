from flask import Flask
from flask_script import Manager
app = Flask(__name__)
@app.route('/')
def index():
        return '&lt;h1&gt;hello flask&lt;/h1&gt;'
if __name__ == '__main__':
	app.run(<span style="color:#ff0000;">host='0.0.0.0',
port=5000,debug = True</span>)




'''
localhost:5000访问
对hello.py的改进
'''
