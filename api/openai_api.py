import openai
import os
from dotenv import load_dotenv

load_dotenv()

# Inicializa el cliente de OpenAI
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generar_email_comercial(descripcion_analisis: str, modelo: str = "gpt-3.5-turbo") -> str:
    try:
        messages = [
            {
                "role": "system",
                "content": (
                    "Eres un captador de clientes a los que les das un email comercial sin asunto. "
                    "Tu trabajo es analizar informes pasivos de dominios y, si ves señales de riesgo, "
                    "redactar un email breve y profesional dirigido al equipo técnico de esa empresa explicando por qué "
                    "deberían interesarse en un pentest en la empresa [Empresa]."
                )
            },
            {
                "role": "user",
                "content": f"Aquí tienes el análisis pasivo:\n\n{descripcion_analisis}"
            }
        ]

        response = client.chat.completions.create(
            model=modelo,
            messages=messages,
            max_tokens=800,
            temperature=0.7
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"[✗] Error al generar el email: {e}"

