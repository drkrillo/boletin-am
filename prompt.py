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

            Generar un resumen del documento. El mensaje debe ser informativo, detallado, \ 
            pero conciso y orientado a un lector promedio sin conocimientos \
            en leyes.
            No hace falta un texto introductorio aclarando que se  \
            trata de un resumen.
            No debe incluirse la fecha de publicación ni que fue \
            publicada en el Boletín Oficial.
            El texto generado debe ser arreglado como una noticia, \
            y deberá cumplir con todos los requisitos necesarios para su \
            uso como tweet diario. Debe ser corto, preciso, informativo, \
            y generar engagement a través de pocos hashtags.

            Usar el siguiente formato:
            Paso 1:{delimiter} <Si/No Paso 1>
            Paso 2:{delimiter} <Si/No Paso 2>
            Paso 3:{delimiter} <Si/No Paso 3>
            Paso 4:{delimiter} <Si/No Paso 4>
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

            Generar un resumen del documento. El mensaje debe ser informativo, detallado, \ 
            pero conciso y orientado a un lector promedio sin conocimientos \
            en leyes.
            No hace falta un texto introductorio aclarando que se  \
            trata de un resumen.
            No debe incluirse la fecha de publicación ni que fue \
            publicada en el Boletín Oficial.
            El texto generado debe ser arreglado como una noticia, \
            y deberá cumplir con todos los requisitos necesarios para su \
            uso como tweet diario. Debe ser corto, preciso, informativo, \
            y generar engagement a través de pocos hashtags.

            Usar el siguiente formato:
            Paso 1:{delimiter} <Razonamiento Paso 1>
            Paso 2:{delimiter} <Razonamiento Paso 2>
            Paso 3:{delimiter} <Razonamiento Paso 3>
            Paso 4:{delimiter} <Razonamiento Paso 4>
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

    tweet = rest.split(delimiter)[1].strip()

    return social, economic, sustainable, politic, tweet