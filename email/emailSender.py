import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path #

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'Avery Gaksins'
email['to'] = 'someone93@gmail.com'
email['subject'] = 'You just won to 1,000,000 dollars!'

email.set_content(html.substitute({'name': 'Avery'}), 'html')

#Code to send email
with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.ehlo() #server - I'm awake
    smtp.starttls() # encrpytiong mechanism to connect to server
    smtp.login('dummymcdummy288@gmail.com', '**** **** **** ****') #login to account actual pass removed for security
    smtp.send_message(email)
    print('email sent!')




