from flask import Flask,render_template,request
from flask.ext.wtf import Form
from wtforms import StringField,SubmitField,PasswordField
from wtforms.validators import Required
app = Flask(__name__)
app.config['SECRET_KEY']='www.itmin.cn'

class NameForm(Form):
	name = StringField('user:',validators=[Required()])
	passwd = PasswordField('password:', validators=[Required()])
	submit = SubmitField('submit')
	
@app.route('/')
def index():
	return render_template('index.html')
@app.route('/<user>')
def add(user):
	return render_template('add.html',name=user)
	
@app.route('/submit')
def submit_form():
	name = None
	form = NameForm()
	if form.validate_on_submit():
		name = form.name.data
		form.name.data = ''
	return render_template('submit.html',form=form,name=name)
	
@app.route('/submit',methods=['GET','POST'])
def submit():
	return request.form['name']+'</br>'+request.form['passwd']
	
if __name__ == '__main__':
	app.run(host='0.0.0.0',port=5000,debug=True)
