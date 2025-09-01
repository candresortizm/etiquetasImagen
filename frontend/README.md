# WEB Frontend - Interfaz web para hacer llamados al API de extracción de etiquetas

Se trata de una interfaz web usando HTML, CSS y Js, expuesta usando Flask. Cuenta con una única pantalla cuyo objetivo es cargar la imagen, mostrarla, enviarla al API de extracción de etiquetas y mostrar el JSON obtenido de respuesta.

## Variable de entorno:
Para el funcionamiento del proyecto es necesario asignar la variable de entorno API_URL. El archivo env.sample muestra un ejemplo.

## Ejecución local:

Se recomienda primero la creación de un entorno virtual.

python -m venv env

Activar el entorno virtual:

.\env\Scripts\activate (para windows)

Instalar las dependencias:

pip install .

Ejecutar el Api:

python .\src\server.py 


## Ejecución con Docker:

Hacer la construcción de la imagen de Docker:

docker build -t frontend-web .

Ejecutar un contenedor:

docker run -p 5000:5000 --env-file .env frontend-web