# using SendGrid's Python Library - https://github.com/sendgrid/sendgrid-python
import sendgrid
from octy import app

sg = sendgrid.SendGridClient(app.config['SENDGRID_USER'], app.config['SENDGRID_KEY'])
message = sendgrid.Mail()

def sendEmail(user, emailTemplate):
	message.add_to(user.email)
	message.set_from("hi@vahidjozi.com")
	if emailTemplate is 'newUser':
		message.set_subject("Welcome to Octy muthfuka!")
		message.set_html("<p>Sup!</p><p>So you came to your senses and decided to see where your career path is taking you. Good!</p><p>Stay tuned.</p>")
		sg.send(message)
		print "emails sent w/ newUser tempalte"
	else:
		print "template doesn't exist dude!"