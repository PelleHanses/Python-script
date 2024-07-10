#!/usr/bin/python3
'''
send_email.py
Examples of sending email to a SMTP-server, like Postfix.

Check the env.py example to

The function can be included in other scripts like this:
    from send_email import send_mail
    result = send_mail()

'''

import os
from dotenv import load_dotenv
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

def send_email(sender_email, receiver_email, body, subject, attached):
    """
    Sends email with attached files, if given
    """
    load_dotenv()  # Loads .env
    smtp_server = os.getenv('SMTP_SERVER')
    smtp_port = os.getenv('SMTP_PORT')
    if not sender_email:
        sender_email = os.getenv('SENDER_EMAIL')
    if not receiver_email:
        receiver_email = os.getenv('RECIEVER_EMAIL')


    # Create a multipart message
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject

    # Attach the body to the message
    msg.attach(MIMEText(body, 'plain'))

    # Attach files
    for filepath in attached:
        result = attach_file(msg, filepath)

    try:
        # Send the email
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.send_message(msg)
            return True
    except smtplib.SMTPException as e:
        return False
    except Exception as e:
        return False

def attach_file(msg, filepath):
    """
    Adds files as attached files
    """
    try:
        with open(filepath, "rb") as attachment:
            part = MIMEBase("application", "octet-stream")
            part.set_payload(attachment.read())
            encoders.encode_base64(part)
            part.add_header(
                "Content-Disposition",
                f"attachment; filename= {os.path.basename(filepath)}",
            )
            msg.attach(part)
            return True
    except FileNotFoundError as e:
        return False
    except Exception as e:
        return False


## Start
if __name__ == "__main__":
    sender_email = False
    receiver_email = "from_me@example.com"
    body = "This is my first test email"
    subject = "Testing testing"
    attached = ["your_file.csv", "your_file.pdf"]
    result = send_email(sender_email, receiver_email, body, subject, attached)
    if result:
        print("Email sent successfully.")
    else:
        print("Failed to send email.")
