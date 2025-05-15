import smtplib
from dotenv import load_dotenv
import os
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders

load_dotenv()
def send_email(to_email):
    email = os.getenv("USER_NAME")
    password = os.getenv("PASSWORD")
    server = smtplib.SMTP("smtp.gmail.com",587)
    check = server.ehlo()
    if check[0] == 250:
        print("Successfully connected with mail server")
    else:
        print("Unable to connect with mail server")
        return
    server.starttls()
    try:
        server.login(email,password)
        print("Logged in successfully")
    except smtplib.SMTPAuthenticationError:
        print("Failed to login due to some authentication error")

    subject = "This is an email sent using python !!"
    body = "Wow !! Python can also send emails"
    message = f"Subject: {subject} \n\n {body}"
    try:
        server.sendmail(email,to_email,message)
        print("The email has been sent successfully")
    except Exception as e:
        print(f"Failed to send email {e}")
    server.quit()

send_email("arnabmitra471@gmail.com")


def send_email_with_attachment(to_email,subject,body,file_path):

    # Retrieving the credentials
    email = os.getenv("USER_NAME")
    password = os.getenv("PASSWORD")

    # Creating the email structure with MIMEMultipart

    msg = MIMEMultipart()
    msg["From"] = email
    msg["To"] = to_email
    msg["Subject"] = subject

    msg.attach(MIMEText(body,"html"))
    try:
        with open(file_path,"rb") as attachment:
            part = MIMEBase("application","octet-stream")
            part.set_payload(attachment.read())
            encoders.encode_base64(part)
            part.add_header("Content-Disposition",f"attachment; filename={os.path.basename(file_path)}")
            msg.attach(part)
    except FileNotFoundError as FNE:
        print(f"File not found {file_path},{FNE}")
        return

    # Establishing connection with the server
    server = smtplib.SMTP("smtp.gmail.com",587)
    check = server.ehlo()

    # Checking if the connection has been established successfully or not
    if check[0] == 250:
        print("Successfully connected with the server")
    else:
        print("Unable to connect with the server")
    # Once connected try to login with the credentials
    server.starttls()
    try:
        server.login(email,password)
        print("Logged in successfully")
    except smtplib.SMTPAuthenticationError:
        print("Failed to login because authentication was unsuccessful")
    try:
        server.sendmail(email,to_email,msg.as_string())
    except Exception as e:
        print(f"Failed to send email {e}")
    finally:
        server.quit()

subject = "This is the output for experiment 5"

body = '''
I am sending this file for you to <strong>verify that
everything works properly</strong>

<p> By the way it is very interesting to tweak such programs 
and make small but non breaking changes</p>
'''
send_email_with_attachment("arnabmitra471@gmail.com",subject,body,"exception_handling_output.png")
