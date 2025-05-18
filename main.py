from fastapi import FastAPI
import uvicorn
from api.openai_api import generar_email_comercial
from servicios.ejecutar_analisis_srvc import ejecutar_todos_los_servicios  # módulo donde llamas a todos los servicios
from servicios.email_srvc import enviar_email
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from pydantic import BaseModel

app = FastAPI()


load_dotenv()

# Configuración de CORS para permitir todos los orígenes
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permitir todos los orígenes
    allow_credentials=True,
    allow_methods=["*"],  # Permitir todos los métodos
    allow_headers=["*"],  # Permitir todos los encabezados
)



class DomainRequest(BaseModel):
    dominio: str
    cliente_email: str

@app.post("/analizar")
async def analizar(request: DomainRequest):
    domain = request.dominio
    cliente_email = request.cliente_email
    # Ejecutar todos los servicios que generan output.txt
    contenido = ejecutar_todos_los_servicios(domain)

    # Ahora generar email pasando el output.txt que ya está creado
    email_generado = generar_email_comercial(contenido)

    # Por último enviaremos un email al cliente
    enviado = enviar_email(email_generado, cliente_email)

    return {
        "status": "✓ Análisis completado y email enviado.",
        "succes": enviado
    }

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
