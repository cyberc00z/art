#!/usr/bin/env python3

import smtplib
from openpyxl import load_workbook
#helper email address
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import sys
import yaml
import time
from yaml.loader import FullLoader, Loader
#send credentials

##load credentials from yaml file
email_username =yaml.load(open('creds.yml'), Loader=FullLoader)
email_user = email_username['creds']['email_username']

email_pass = yaml.load(open('creds.yml'), Loader=FullLoader)  # create a good password
email_password = email_pass['creds']['email_password']


# extract emails from xls file
wb = load_workbook("email.xlsx")
source = wb["Sheet1"]
for emails_send in source['A']:
     emails_send = emails_send.value
     

#load and read buffer and 
#create a object names emails

email_send = list(emails_send)
print(type(email_send))
assert isinstance(email_send, list)
subject = 'Put Subject here'
msg = MIMEMultipart('alternative')
msg['From'] = email_user 

#converting list of recipients into comma separated string
msg['To'] = ", ".join(email_send)

msg['Subject'] = ""
body = """<html>
 
       <body>
         <h1></h1>
       </body>
 
 </html>"""
            


msg.attach(MIMEText(body, 'html'))
#msg.attach(MIMEText(template.render(),'html')
#print(text)
text = msg.as_string()

try:
   server = smtplib.SMTP('smtp.gmail.com',587)
   server.starttls()
   server.login(email_user, email_password)
   start = time.time()
   server.sendmail(email_user, email_send, text)
   end = time.time()
   print("Total time taken in sending emails : {}".format(end-start))
except Exception as err:
   print(err)
   sys.exit(0)

print("Exiting from here")
server.quit()
