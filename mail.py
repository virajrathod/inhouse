'''
This script is a simple python code to send an email using the smtp library

LAST_UPDATED_ON: 10/26/2022

'''
__author__ = ['Viraj Rathod']
__version__ = '0.1'

from email.message import EmailMessage
from re import sub
import smtplib
import os
import ssl

email_sender = 'vir9981@gmail.com'
email_password = os.environ.get('password')
email_rec = 'virajrathod99@gmail.com'

subject = 'Check out this email sent from python'
body = '''
Isn't this cool
'''

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_rec
em['Subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_rec, em.as_string())
    # print('Mail sent')
