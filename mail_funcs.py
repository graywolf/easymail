import smtplib
import string

def send_mail(sender, recipient, subject, message, mail_options=[], rcpt_options=[]):
	'''Function for easy mail sending.

	Args:
		sender: mail adress of sender
		recipient: mail adress of recipient
		subject: subject of the mail
		message: body of the message
		mail_options: mail_options of SMTP object sendmail
		rcpt_options: rcpt_options of SMTP object sendmail
	Returns:
		None
	Raises:
		Appropriate error from called functions
'''
	#create smtp ssl object
	if send_mail.use_ssl:
		smtp = smtplib.SMTP_SSL(
							send_mail.server,
							send_mail.port,
							send_mail.local_hostname,
							send_mail.keyfile,
							send_mail.certfile
							)
	#create regular smpt object
	else:
		smtp = smtplib.SMTP(
						send_mail.server,
						send_mail.port,
						send_mail.local_hostname
						)
	
	#enable tls?
	if send_mail.use_tls:
		smtp.starttls(send_mail.keyfile, send_mail.certfile)
	
	#do we need login?
	if send_mail.user is not None:
		smtp.login(send_mail.user, send_mail.password)
	
	#construct message and send it
	body = "From: {!s}\nTo: {!s}\nSubject: {!s}\n\n{!s}\n".format(
																sender,
																recipient,
																subject,
																message
																)
	smtp.sendmail(sender, recipient, body, mail_options, rcpt_options)
	
	#close smtp object
	smtp.quit()
	