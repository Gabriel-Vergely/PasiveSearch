import requests

def analizar_cookies(url: str) -> str:
    try:
        response = requests.get(url)

        resultado = "Cookies:\n"
        for cookie in response.cookies:
            resultado += f"{cookie.name} = {cookie.value}\n"

        resultado += "\nCabecera Content-Security-Policy:\n"
        csp = response.headers.get('Content-Security-Policy', 'No especificada')
        resultado += f"{csp}\n"

        return resultado

    except requests.RequestException as e:
        return f"[✗] Error al acceder a la URL: {e}"
