import requests

def analizar_headers_http(url: str) -> str:
    try:
        response = requests.get(url)

        resultado = f"🔍 Cabeceras HTTP obtenidas para: {url}\n\n"
        for header, value in response.headers.items():
            resultado += f"{header}: {value}\n"

        return resultado

    except requests.RequestException as e:
        return f"[✗] Error al realizar la solicitud: {e}"
