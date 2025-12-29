import smtplib

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

my_email = ""

def send_email(to_addresses, body):
  password = "password"
  
  msg = MIMEMultipart()
  msg['from'] =  my_email
  msg['to'] = ", ".join(to_addresses)
  
  msg['subject'] = "Confirmação de viagem!"
  msg.attach(MIMEText(body, 'plain'))
  
  server = smtplib.SMTP('smtp.ethereal.email', 587)
  server.starttls()
  server.login(my_email, password)
  text = msg.as_string()
  
  for email in to_addresses:
    server.sendmail(my_email, email, text)
    
  server.quit()