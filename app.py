from email.mime.text import MIMEText
from smtplib import SMTP

import smtplib, csv, codecs, ssl
import pandas as pd

def sendMail(receiver):
  serverMail = ''
  usernameMail = ''
  passwordMail = ''
  portMail = 465
  contextMail = ssl.create_default_context()

  name = ''
  subject = ''
  message = codecs.open('email.html', 'r')
  message = message.read()

  contentEmail = MIMEText(message, 'html')
  contentEmail['From'] = ""
  contentEmail['To'] = receiver
  contentEmail['Subject'] = subject

  try:
    with smtplib.SMTP_SSL(serverMail, portMail, context=contextMail) as mail:
      mail.ehlo()
      mail.set_debuglevel(True)
      mail.login(usernameMail, passwordMail)
      print('Server Mail Connected')
      mail.ehlo()
      mail.sendmail(usernameMail, receiver, contentEmail.as_string())
      print('Send Mail Successfully!')
      mail.quit()

  except Exception as err:
    print("Server Mail Error... ")
    print(err)

def readCsv():
  listEmail = []

  print('Reading file csv...')
  data = pd.read_csv('email.csv')
  emailData = data['Email']
  for email in emailData:
    print('Send email to : '+email)
    if(email in listEmail):
      print('A message has been sent to the email')
    else:
      sendMail(email)
      listEmail.append(email)

readCsv()