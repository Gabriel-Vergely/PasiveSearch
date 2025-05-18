import smtplib
from email.message import EmailMessage

email = EmailMessage()
email['From'] = 'gabriel.vergey@gmail.com'
email['To'] = 'gabriel.vergey@gmail.com'
email['Subject'] = 'Prueba'
email.set_content('Esto es un correo de prueba.')

with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
    smtp.set_debuglevel(1)
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()
    smtp.login('gabriel.vergey@gmail.com', 'qxnsrfomyjchbggp')
    smtp.send_message(email)

print("Correo enviado.")
