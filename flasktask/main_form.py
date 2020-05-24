from flask import Flask, render_template, request, flash
from flask_mail import Mail
import json

with open('config.json', 'r') as c:
	params=json.load(c)["parameter"]
app=Flask(__name__)
app.secret_key="secret form"

app.config.update(
	MAIL_SERVER='smtp.gmail.com',
	MAIL_PORT='465',
	MAIL_USE_SSL=True,
	MAIL_USERNAME=params['gmail-user'],
	MAIL_PASSWORD=params['gmail-password']
)

mail=Mail(app)

@app.route("/",methods=['GET','POST'])
def home():
	if(request.method=='POST'):
		name=request.form.get('name')
		email=request.form.get('email')
		password=request.form.get('password')
		mail.send_message('New Sign Up', 
			sender= email, 
			recipients = [params['gmail-user']], body='Name = ' + name + ' \n' +  'Email = ' + email)
		if(mail.send_message):
			flash("Successfully Account Created", name)
			return render_template('message.html')
		else:
			flash("Oops Something Went Wrong :(")
	return render_template('flaskform.html')


app.run(debug=True)
