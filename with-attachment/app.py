from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import smtplib, csv, codecs, ssl, os
import pandas as pd

def sendMail(receiver):
  serverMail = ''
  usernameMail = ''
  passwordMail = ''
  portMail = 587

  name = ''
  subject = ''
  message = codecs.open('email.html', 'r')
  message = message.read()

  contentEmail = MIMEMultipart()
  contentEmail['From'] = ""
  contentEmail['To'] = receiver
  contentEmail['Subject'] = subject
  contentEmail.attach(MIMEText(message, 'html'))

  filename = f'file/{receiver}.pdf'
  with open(filename, 'rb') as attachment:
    part = MIMEBase('application', 'octet-stream')
    part.set_payload(attachment.read())
  
  encoders.encode_base64(part)
  part.add_header('Content-Disposition', f'attachment; filename=filename.pdf')
  contentEmail.attach(part)

  try:
    mail = smtplib.SMTP(serverMail, portMail)
    mail.ehlo()
    mail.starttls()
    mail.login(usernameMail, passwordMail)
    mail.sendmail(usernameMail, receiver, contentEmail.as_string())
    print('Send Email Successfully!')

  except Exception as err:
    print("Server Mail Error... ")
    print(err)

def readCsv():
  listEmail = []
  listFileName = []

  data = pd.read_csv('email.csv')
  emailData = data['Email']
  path = os.getcwd()+'\\file'
  
  with os.scandir(path) as listFile:
    for file in listFile:
      if file.is_file():
        name = file.name
        listFileName.append(name.replace('.pdf', ''))
  
  for email in emailData:
    print('Send email to : '+email)
    if(email in listEmail):
      print('A message has been sent to the email')
    else:
      sendMail(email)

readCsv()