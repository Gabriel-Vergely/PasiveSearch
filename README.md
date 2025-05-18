# 🔍 PasiveSearch

**PasiveSearch** es una herramienta de análisis pasivo para pentesters y analistas de seguridad. Automatiza la recolección de información sin generar tráfico activo sospechoso, utilizando utilidades comunes ya incluidas en Kali Linux, y complementa el análisis con un informe redactado automáticamente mediante **OpenAI**.

---

## 🧰 Herramientas utilizadas

Esta herramienta integra varias utilidades de análisis pasivo:

- **[dnsrecon]** – Recolección pasiva de DNS y registros públicos.
- **[WhatWeb]** – Detección de tecnologías del sitio objetivo.
- **Cabeceras HTTP** – Análisis de headers del servidor.
- **SSL** – Evaluación de configuración y certificados TLS/SSL.
- **Cookies** – Revisión de cookies (atributos de seguridad).
- **[OpenAI API]** – Generación de un informe automatizado en forma de email, dirigido a posibles clientes, destacando riesgos detectados en el análisis.

---

## 🤖 ¿Qué hace PasiveSearch?

1. Ejecuta herramientas pasivas para recolectar información del dominio objetivo.
2. Procesa resultados de DNS, tecnologías, headers, cookies y SSL.
3. **Envía automáticamente esta información a ChatGPT** (vía la API de OpenAI), junto con un contexto de ventas.
4. Obtiene un **informe estilo email** redactado como si fuera desde una empresa de pentesting, explicando por qué el sitio puede requerir una auditoría de seguridad ofensiva.

---

## 📦 Requisitos

- Python 3.8+
- Kali Linux (o Linux con herramientas instaladas):
  - `dnsrecon`
  - `whatweb`
- API Key de [OpenAI](https://platform.openai.com/)
- Librerías Python:
  ```bash
  pip install requests openai

---

## ⚙️ Uso

Ejecutar el archivo de la api de openAI:

python3 api/openai_api.py

---

## 📧 Ejemplo email generado

Asunto: Análisis de seguridad pasiva - Riesgos potenciales detectados

Estimado equipo técnico,

Espero que este mensaje os encuentre bien. Basándome en el reciente análisis pasivo de seguridad de nuestro dominio, he detectado varias señales que indican que podríamos beneficiarnos de una auditoría de seguridad ofensiva.

Primero, el informe muestra que DNSSEC (Domain Name System Security Extensions) no está configurado para nuestro dominio. La falta de DNSSEC puede hacer que nuestro sitio web sea vulnerable a ataques de envenenamiento de DNS, lo que podría redirigir a los usuarios a sitios web maliciosos.

Además, no se ha especificado la cabecera Content-Security-Policy (CSP). Sin una política de CSP, corremos el riesgo de ataques de cross-site scripting (XSS) y de inyección de datos.

Por último, el servidor parece estar utilizando una versión anterior de JQuery. Las versiones antiguas de JQuery pueden contener vulnerabilidades que los ciberdelincuentes podrían explotar para comprometer nuestro sitio web.

Por todo lo anterior, recomiendo que consideremos una auditoría de seguridad ofensiva. Este tipo de pruebas nos ayudará a identificar y corregir cualquier vulnerabilidad de seguridad antes de que pueda ser explotada.

Quedo a vuestra disposición para discutir más detalles o para responder a cualquier pregunta que podáis tener.

Saludos cordiales,

[Tu nombre]
[Tu cargo]

---

## ⚠️ Disclaimer

Esta herramienta está diseñada exclusivamente para uso ético, educativo o profesional bajo autorización explícita. No debe ser utilizada en dominios sin permiso. El autor no se responsabiliza por un uso indebido.