import yagmail
import os
import time 

sender_email = 'thewayalgotrading@gmail.com'
receiver_email = 'thewayalgotrading@gmail.com'

subject = """"
This is the subject
"""
contents = """"
Here is the content of the email!
Hi!
"""
while True:
  yag = yagmail.SMTP(user=sender_email, password=os.getenv('PASSWORD'))
  yag.send(to=receiver_email, subject=subject, contents=contents)
  print('Email Sent!')
  time.sleep(60)
