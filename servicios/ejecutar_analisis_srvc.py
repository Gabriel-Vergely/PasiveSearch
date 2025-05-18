from servicios.analisis.cookies_srvc import analizar_cookies
from servicios.analisis.headers_srvc import analizar_headers_http
from servicios.analisis.ssl_srvc import analizar_certificado_ssl
from servicios.analisis.dnsrecon_srvc import analizar_dns
from servicios.analisis.whatweb_srvc import analizar_tecnologias_web
from utils.resultados_parser import unir_resultados

def ejecutar_todos_los_servicios(dominio: str):
    """
    Devuelve el resultado de los diferentes analisis pasivos.
    """  
    url = f"https://{dominio}"

    cookies_output = analizar_cookies(url)        
    headers_output = analizar_headers_http(url)      
    ssl_output = analizar_certificado_ssl(dominio) 
    whatweb_output = analizar_tecnologias_web(url)        
    dnsrecon_output = analizar_dns(dominio)   

    # Parsear los diferentes resultados en uno
    analisis_completo = unir_resultados(cookies_output, headers_output, ssl_output, whatweb_output, dnsrecon_output)
    
    return analisis_completo 

    
