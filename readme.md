# EasyMail

## Description

Python3 library for easy sending of mails. Uses smtplib library.

You need to set all needed variables (listed in \_\_init\_\_.py (or you can modify default values))
before calling send_mail.

Look into \_\_init\_\_.py to see what's included and into specific .py files to se functions..

## Example

### send_mail

You need to set all needed variables and after that you can call send_mail as many times you would like,
as you can see below.

	import easymail
	easymail.send_mail.use_ssl = False
	easymail.send_mail.use_tls = True
	easymail.send_mail.server = 'example.org'
	easymail.send_mail.user = 'user@example.org'
	easymail.send_mail.password = 'password'
	
	easymail.send_mail('user@example.org', 'user2@example.org', 'test', 'test2')
	easymail.send_mail('user@example.org', 'user2@example.org', 'test', 'test3')
	easymail.send_mail('user@example.org', 'user2@example.org', 'test', 'test4')
