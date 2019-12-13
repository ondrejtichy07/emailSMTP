import smtplib
import os

EMAIL_ADDRESS = 'ondrejtichy07@gmail.com'
EMAIL_PASSWORD = os.environ.get('GMAIL_APP_PASSWORD') #Environment variable - nano .bash_profile

def sendAlert(subject, text, receiver):
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()

        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

        msg = f'Subject: {subject}\n\n{text}'
        smtp.sendmail(EMAIL_ADDRESS, receiver, msg)
