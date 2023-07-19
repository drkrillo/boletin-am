# Boletin Oficial Cortito y en Criollo

Este proyecto se encarga de levantar la información de la primera sección del Boletín Oficial de Argentina, los resume y puntúa para definir aquellas publicaciones que podrían ser de interés general.

## Setup

Instalar librerías necesarias:
```
pip install -r requirements.txt 
```
Creat en la carpeta base, una nueva carpeta llamada ```
.env``` que contenga la siguiente variable de entorno:
```
OPENAI_API_KEY=<tu api key de Open AI>
```
Puedes crear una API Key de Open AI una vez te crees un usuario. Hay una versión gratuita.

## Scraping y Resummidor

Para cargar información diaria en data.json, correr desde la carpeta base:
```
python etl/main.py
```

## Ranker

Para hacer un ranking del día, correr:
```
pyhon publisher/main.py
```






