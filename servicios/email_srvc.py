import smtplib
import os
import logging
from email.message import EmailMessage
from dotenv import load_dotenv

load_dotenv()

# Configura logging
logging.basicConfig(
    level=logging.INFO,  # Cambia a DEBUG para más detalle
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def enviar_email(contenido: str, destinatario: str, asunto: str = "Informe de seguridad") -> bool:
    try:
        logging.info(contenido)
        email = EmailMessage()
        email['From'] = os.getenv("EMAIL_ADDRESS")
        email['To'] = destinatario
        email['Subject'] = asunto
        email.set_content(contenido)

        host = os.getenv("EMAIL_HOST")
        port = int(os.getenv("EMAIL_PORT"))
        usuario = os.getenv("EMAIL_ADDRESS")
        password = os.getenv("EMAIL_PASSWORD")

        logging.info(f"Conectando a SMTP en {host}:{port} como {usuario}")

        with smtplib.SMTP(host, port) as smtp:
            smtp.starttls()
            smtp.login(usuario, password)
            smtp.send_message(email)

        logging.info("Email enviado correctamente.")
        return True

    except Exception as e:
        logging.error(f"Error al enviar el email: {e}", exc_info=True)
        return False

""" 
import boto3
import os
from botocore.exceptions import BotoCoreError, ClientError
from dotenv import load_dotenv

load_dotenv()  # Para cargar las variables de entorno

def enviar_email_ses(destinatario, asunto, contenido):
    ses = boto3.client(
        'ses',
        region_name=os.getenv("AWS_REGION"),
        aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
        aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY")
    )

    try:
        respuesta = ses.send_email(
            Source=os.getenv("SES_FROM_ADDRESS"),
            Destination={
                'ToAddresses': [destinatario],
            },
            Message={
                'Subject': {
                    'Data': asunto,
                    'Charset': 'UTF-8'
                },
                'Body': {
                    'Text': {
                        'Data': contenido,
                        'Charset': 'UTF-8'
                    }
                }
            }
        )
        print("[✓] Email enviado correctamente.")
        return True

    except (BotoCoreError, ClientError) as error:
        print(f"[✗] Error al enviar el email con SES: {error}")
        return False
 """