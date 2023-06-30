import os
import time

import openai

from dotenv import load_dotenv
load_dotenv()

delimiter = "####"
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

def summarize(chunks):
    if len(chunks) <= 1:
        prompt = f"""
            Seguir los siguientes pasos para generar un tweet del resumen del \
            texto jurídico del Boletín Oficial de Argentina delimitado \
            por cuatro hastags, {delimiter}.

            Paso 1: {delimiter} Primero, responder: ¿Es el texto \
            relevante desde un punto de vista social? Responder \
            sólo con una palabra: Si / No
            Paso 2: {delimiter} Segundo, responder: ¿Es el texto \
            relevante desde un punto de vista económico? Responder \
            sólo con una palabra: Si / No
            Paso 3: {delimiter} Tercero, responder: ¿Es el texto \
            relevante desde un punto de vista ecológico y \
            sustentable? Responder sólo con una palabra: Si / No
            Paso 4: {delimiter} Cuarto, responder: ¿Es el texto \
            relevante desde un punto de vista político? Responder \
            sólo con una palabra: Si / No
            Paso 5: {delimiter} Quinto, responder: ¿Es el texto \
            relevante para el ciudadano común? Responder sólo con \
            una palabra: Si / No
            Paso 6: {delimiter} Sexto, responder: ¿Es el texto \
            relevante para el trabajador promedio? Responder sólo con \
            una palabra: Si / No
            Paso 7: {delimiter} Séptimo, responder: ¿El texto expande o \
            vulnera o trata sobre algún derecho primordial? Responder sólo con \
            una palabra: Si / No
            Paso 8: Asignar al texto una puntuación numérica entre 0 y 100 \
            dependiendo la importancia y trascendencia del comunicado desde \
            un punto de vista popular, ambiental y tecnológico. Responder \
            con un número: 0-100.

            Generar un resumen del documento. El mensaje debe ser informativo, detallado, \ 
            conciso y orientado a un lector promedio sin conocimientos \
            en leyes.
            Agregar un párrafo dando detalles acerca de números, fechas, \
            u otro dato relevante del documento importante para el ciudadano.
            No hace falta un texto introductorio aclarando que se  \
            trata de un resumen.
            No debe incluirse la fecha de publicación ni que fue \
            publicada en el Boletín Oficial.
            El texto generado debe ser arreglado como una noticia, \
            y deberá cumplir con todos los requisitos necesarios para su \
            uso como tweet diario.

            Usar el siguiente formato:
            Paso 1:{delimiter} <Si/No Paso 1>
            Paso 2:{delimiter} <Si/No Paso 2>
            Paso 3:{delimiter} <Si/No Paso 3>
            Paso 4:{delimiter} <Si/No Paso 4>
            Paso 5:{delimiter} <Si/No Paso 5>
            Paso 6:{delimiter} <Si/No Paso 6>
            Paso 7:{delimiter} <Si/No Paso 7>
            Paso 8:{delimiter} <0-100 Paso 8>
            Tweet:{delimiter} <Tweet con resumen del artículo>

            Texto:{delimiter}{chunks[0]}{delimiter}
        """
        response = get_completion(prompt)

    else:
        print(f"{len(chunks)} chunks. Please wait!")
        initial_response = ''
        for i, chunk in enumerate(chunks):
            prompt = f"""
                Resumir el fragmento de un artículo publicado en el Boletín \
                Oficial de Argentina delimitado por cuatro hastags, {delimiter}.
                Tener en cuenta que es el trozo {i+1} de {len(chunks)+1} trozos. \
                Luego, todos estos trozos serán unificados en el mismo mensaje.

                Review: {delimiter}{chunk}{delimiter}
            """
            initial_response += get_completion(prompt)
            time.sleep(20)
            print(f"{i+1} done.")

        prompt = f"""
            Seguir los siguientes pasos para generar un tweet del resumen del \
            texto jurídico del Boletín Oficial de Argentina delimitado \
            por cuatro hastags, {delimiter}.

            Paso 1: {delimiter} Primero, responder: ¿Es el texto \
            relevante desde un punto de vista social? Responder \
            sólo con una palabra: Si / No
            Paso 2: {delimiter} Segundo, responder: ¿Es el texto \
            relevante desde un punto de vista económico? Responder \
            sólo con una palabra: Si / No
            Paso 3: {delimiter} Tercero, responder: ¿Es el texto \
            relevante desde un punto de vista ecológico y \ 
            sustentable? Responder sólo con una palabra: Si / No
            Paso 4: {delimiter} Cuarto, responder: ¿Es el texto \
            relevante desde un punto de vista político? Responder \
            sólo con una palabra: Si / No      
            Paso 5: {delimiter} Quinto, responder: ¿Es el texto \
            relevante para el ciudadano común? Responder sólo con \
            una palabra: Si / No
            Paso 6: {delimiter} Sexto, responder: ¿Es el texto \
            relevante para el trabajador promedio? Responder sólo con \
            una palabra: Si / No
            Paso 7: {delimiter} Séptimo, responder: ¿El texto expande o \
            vulnera o trata sobre algún derecho primordial? Responder sólo con \
            una palabra: Si / No
            Paso 8: Asignar al texto una puntuación numérica entre 0 y 100 \
            dependiendo la importancia y trascendencia del comunicado desde \
            un punto de vista popular, ambiental y tecnológico. Responder \
            con un número: 0-100.

            Generar un resumen del documento. El mensaje debe ser informativo, detallado, \ 
            pero conciso y orientado a un lector promedio sin conocimientos \
            en leyes.
            Agregar un párrafo dando detalles acerca de números, fechas, \
            u otro dato relevante del documento importante para el ciudadano.
            No hace falta un texto introductorio aclarando que se  \
            trata de un resumen.
            No debe incluirse la fecha de publicación ni que fue \
            publicada en el Boletín Oficial.
            El texto generado debe ser arreglado como una noticia, \
            y deberá cumplir con todos los requisitos necesarios para su \
            uso como tweet diario.

            Usar el siguiente formato:
            Paso 1:{delimiter} <Si/No Paso 1>
            Paso 2:{delimiter} <Si/No Paso 2>
            Paso 3:{delimiter} <Si/No Paso 3>
            Paso 4:{delimiter} <Si/No Paso 4>
            Paso 5:{delimiter} <Si/No Paso 5>
            Paso 6:{delimiter} <Si/No Paso 6>
            Paso 7:{delimiter} <Si/No Paso 7>
            Paso 8:{delimiter} <0-100 Paso 8>
            Tweet:{delimiter} <Tweet con resumen del artículo>

            Texto:{delimiter}{initial_response}{delimiter}
        """
        response = get_completion(prompt)

    social, rest = response.split('\n', 1)
    social = int(social.split(delimiter)[1]
                 .replace('No', '0')
                 .replace('Sí', '1')
                 .replace('Si', '1')
                 .strip()
    )

    economic, rest = rest.split('\n', 1)
    economic = int(economic.split(delimiter)[1]
                   .replace('No', '0')
                   .replace('Sí', '1')
                   .replace('Si', '1')
                   .strip()
    )

    sustainable, rest = rest.split('\n', 1)
    sustainable = int(sustainable.split(delimiter)[1]
                      .replace('No', '0')
                      .replace('Sí', '1')
                      .replace('Si', '1')
                      .strip()
    )

    politic, rest = rest.split('\n', 1)
    politic = int(politic.split(delimiter)[1]
                  .replace('No', '0')
                  .replace('Sí', '1')
                  .replace('Si', '1')
                  .strip()
    )
    citizen, rest = rest.split('\n', 1)
    citizen = int(citizen.split(delimiter)[1]
                  .replace('No', '0')
                  .replace('Sí', '1')
                  .replace('Si', '1')
                  .strip()
    )
    worker, rest = rest.split('\n', 1)
    worker = int(worker.split(delimiter)[1]
                  .replace('No', '0')
                  .replace('Sí', '1')
                  .replace('Si', '1')
                  .strip()
    )
    rights, rest = rest.split('\n', 1)
    rights = int(rights.split(delimiter)[1]
                  .replace('No', '0')
                  .replace('Sí', '1')
                  .replace('Si', '1')
                  .strip()
    )
    score, rest = rest.split('\n', 1)
    score = int(score.split(delimiter)[1]
                  .strip()
    )

    tweet = rest.split(delimiter)[1].strip()

    return social, economic, sustainable, politic, citizen, worker, rights, score, tweet