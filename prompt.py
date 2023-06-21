import os
import openai

from dotenv import load_dotenv
load_dotenv()

MAX_TOKENS = 4096
openai.api_key  = os.getenv('OPENAI_API_KEY')


def get_completion(prompt, model="gpt-3.5-turbo"): 
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0, 
    )
    return response.choices[0].message["content"]

def summarize(text):
    prompt = f"""
            Extraer la siguiente información relevante del texto \ 
            jurídico entre triple comillas manteniendo los detalles \
            relevantes a dinero, nombres, y la importancia para la  \
            ciudadanía sobre quienes aplica.

            Información a extraer:
            Instituciones involucradas,
            Cargos o personas involucradas,
            Potenciales impactos sobre el común ciudadano,
            Datos relativos a dinero que implica el documento.

            Generar un resumen del documento incluyendo los datos antes \
            mencionados. El mensaje debe ser informativo, detallado, \ 
            pero conciso y orientado a un lector promedio sin conocimientos \
            en leyes.
            No hace falta un texto introductorio aclarando que se  \
            trata de un resumen y obviar detalles como la ciudad \
            en la que sucede, y que se trata de una norma.
            El texto generado debe ser arreglado como una noticia, \
            y deberá cumplir con todos los requisitos necesarios para su \
            uso como tweet diario. Ser muy corto, preciso, informativo, \
            y generar engagement.
            Review: ```{text}```
        """
    response = get_completion(prompt)

    return response