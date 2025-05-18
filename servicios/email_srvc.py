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
