import subprocess

def analizar_dns(dominio: str) -> str:
    comando = ['dnsrecon', '-d', dominio, '-t', 'std']
    
    try:
        resultado = subprocess.run(comando, capture_output=True, text=True)

        salida = f"🔍 Análisis DNS para {dominio}\n\n"
        salida += "▶ Salida de dnsrecon:\n"
        salida += resultado.stdout + "\n"

        if resultado.stderr:
            salida += "\n⚠️ Errores:\n"
            salida += resultado.stderr + "\n"

        return salida

    except FileNotFoundError:
        return "[✗] Error: 'dnsrecon' no está instalado o no se encuentra en el PATH."
    except Exception as e:
        return f"[✗] Error al ejecutar dnsrecon: {e}"
