import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage


def send_email(sender_email, sender_password, recipient_email, subject, body, image_path):
    # Set up the MIME
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = recipient_email
    message['Subject'] = subject
    message.attach(MIMEText(body, 'plain'))

    # Attach the image
    with open(image_path, 'rb') as attachment:
        image_mime = MIMEImage(attachment.read(), _subtype="png")
        attachment.close()
        image_mime.add_header('Content-Disposition', 'attachment', filename=image_path)
        message.attach(image_mime)

    # Connect to the SMTP server
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()

    # Log in to your Gmail account
    server.login(sender_email, sender_password)

    # Send the email
    server.sendmail(sender_email, recipient_email, message.as_string())

    # Quit the server
    server.quit()


# Replace the following with your own information
sender_email = 'zaithwazonke@gmail.com'
sender_password = 'cihk icag tfgf zrob'
recipient_email = 'martinsilungwe12@gmail.com'
subject = 'Subject of the email'
body = 'Body of the email'
image_path = 'assets/images/gold/qrcode.png'

# Send the email
send_email(sender_email, sender_password, recipient_email, subject, body, image_path)
