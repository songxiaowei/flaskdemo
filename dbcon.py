from flask import Flask
import MySQLdb
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:root@localhost/flask'
db = SQLAlchemy(app)

class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(80), unique=True)
	email = db.Column(db.String(320), unique=True)
	phone = db.Column(db.String(32), nullable=False)
	
	def __init__(self, username ,email, phone):
		self.username = username
		self.email = email
		self.phone = phone

if __name__ == '__main__':
	db.create_all()
