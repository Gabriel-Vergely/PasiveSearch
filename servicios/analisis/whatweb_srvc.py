import subprocess

def analizar_tecnologias_web(url: str) -> str:
    comando = ['whatweb', url]

    try:
        resultado = subprocess.run(comando, capture_output=True, text=True)

        salida = f"🔍 Análisis de tecnologías con WhatWeb para: {url}\n\n"
        salida += "▶ Salida de WhatWeb:\n"
        salida += resultado.stdout + "\n"

        if resultado.stderr:
            salida += "\n⚠️ Errores:\n"
            salida += resultado.stderr + "\n"

        return salida

    except FileNotFoundError:
        return "[✗] Error: 'whatweb' no está instalado o no se encuentra en el PATH."
    except Exception as e:
        return f"[✗] Error al ejecutar WhatWeb: {e}"
