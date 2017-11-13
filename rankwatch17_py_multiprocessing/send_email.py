import smtplib

from email.mime.text import MIMEText

msg = MIMEText('Testing some Mailgun awesomness')
msg['Subject'] = "Hello"
msg['From'] =   "pyra@YOUR_DOMAIN_NAME"
msg['To']      = "priyankakr2312@gmail.com"

s = smtplib.SMTP('smtp.mailgun.org', 587)

s.login('postmaster@sandbox6dc2133cdb134e0d91d7bdd622587b3f.mailgun.org','0e46c6c7a788dc5e193d124de309d561')
s.sendmail(msg['From'], msg['To'], msg.as_string())
s.quit()
