import ssl
import socket
import pprint

def analizar_certificado_ssl(dominio: str, puerto: int = 443) -> str:
    try:
        context = ssl.create_default_context()

        with socket.create_connection((dominio, puerto)) as sock:
            with context.wrap_socket(sock, server_hostname=dominio) as ssock:
                certificado = ssock.getpeercert()

        resultado = f"🔒 Certificado SSL para: {dominio}:{puerto}\n\n"
        resultado += pprint.pformat(certificado)

        return resultado

    except Exception as e:
        return f"[✗] Error al obtener el certificado SSL: {e}"
