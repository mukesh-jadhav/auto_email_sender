import smtplib
import random
import time
import pandas as pd
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

mail_content = "HI! This is a mail to kindly request you to stop spamming me. \
                You are gonna recceive several of such requests from me as a good note. \
                Now you know how irritating it is receive 100's of email daiyly from people \
                like you who buy our mails information from other companies and send us such spams. \
                This is very kind request to you. Please stop all spams you have been sending people \
                like me. For your information, I know you are going to ask me why didn't I unsubscribe \
                from your service? I clicked on unscubscribe as told but that page is not available. \
                I have been trying since a month now. You just mailed wrong person who is a coder. \
                Be ready for getting spammed now. Thank you so much for your patience."

subjects = list(pd.read_csv("QUOTE.csv")['quote'])

#The mail addresses and password
sender_address = 'dailyproblems123@gmail.com'
sender_pass = 'Muks@2512'
receiver_address = 'newsletter@donamails.in'

#Setup the MIME

mail_count = 0
while(1):
    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] = receiver_address
    message['Subject'] = random.choice(subjects)
    
    #The body and the attachments for the mail
    message.attach(MIMEText(mail_content, 'plain'))
    
    #Create SMTP session for sending the mail
    session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
    session.starttls() #enable security
    session.login(sender_address, sender_pass) #login with mail_id and password
    text = message.as_string()
    session.sendmail(sender_address, receiver_address, text)
    session.quit()
    
    mail_count +=1
    print('Mail Sent: ', str(mail_count))
    
    time.sleep(2)
