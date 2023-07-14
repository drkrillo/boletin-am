# Boletin Oficial Cortito y en Criollo

Este proyecto se encarga de levantar la información de la primera sección del Boletín Oficial de Argentina, los resume y puntúa para definir aquellas publicaciones que podrían ser de interés general.

## Setup

Para correr el proyecto, desde la carpeta base crear un nuevo entorno virtual:
```
python -m venv .venv
```
Una vez creado, activarlo usando:
```
.venv\scripts\activate
```
y correr:
```
pip install -r requirements.txt 
```

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






