# API Backend - Extracción de etiquetas de una imagen usando servicio externo

El proyecto es una API construída con FastAPI que expone un endpoint para interactuar con el sistema: 
- POST /api/analyze (Recibe la imágen a través de multipart/form-data)

## Variables de entorno:
Para el funcionamiento del proyecto es necesario asignar las variables VISION_ENDPOINT, API_KEY y TRANSLATION_ENDPOINT. El archivo env.sample muestra un ejemplo.

## Ejecución local:

Se recomienda primero la creación de un entorno virtual.

python -m venv env

Activar el entorno virtual:

.\env\Scripts\activate (para windows)

Instalar las dependencias:

pip install .

Ejecutar el Api:

python .\src\api_handler.py 