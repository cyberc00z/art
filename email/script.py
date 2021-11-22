#!/usr/bin/env python3

import smtplib

#helper email address
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import sys
import yaml
import pandas as pd
import time
#send credentials

##load credentials from yaml file
email_username =yaml.load(open('creds.yml'), Loader=FullLoader)
email_user = email_username['creds']['email_username']

email_pass = yaml.load(open('creds.yml'), Loader=FullLoader)  # create a good password
email_password = email_pass['creds']['email_password']

#list of users to whom email is to be sent
#save in email.xlsx file, 

start = time.time()
df = pd.read_excel("emails.xlsx")
for file_number in range(1, 1500):
    df.append(pd.read_excel(f"Dummy {file_number}.xlsx"))
end = time.time()
print("Excel file : ", end-start)


#load and read buffer and 
#create a object names emails

email_send = ['LIST OF EMAILS']
subject = 'Sri Arbinduo Hive Adda'

msg = MIMEMultipart()
msg['From'] = email_user 

#converting list of recipients into comma separated string
msg['To'] = ", ".join(email_send)

msg['Subject'] = subject
body = 'EMAIL_BODY'
msg.attach(MIMEText(body, 'plain'))

text = msg.as_string()

try:
   server = smtplib.SMTP('smtp.gmail.com',587)
   server.starttls()
   server.login(email_user, email_password)
   server.sendmail(email_user, email_send, text)
except Exception as err:
   print(err)
   sys.exit(0)

print("Exiting from here")
server.quit()

"""
using html for Sending EMAILs with HTML Content

"""
body = """<html>
        <body>
          <p>Hi, <b>Freshers. This is the email from Sri Arbinduo College Hive Mind.</b></p>
          <p>Write the inspiring stuff here!</p>
        </body>
</html>

msg.attach(MIMEText(body,'html'))
"""
