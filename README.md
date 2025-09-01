# Proyecto web de extracción de etiquetas usando un servicio de un tercero (GCP)

Este proyecto consiste en una aplicación web para cargar una imágen que es enviada a una API (backend) que a su vez consume el servicio de Google Cloud Vision para obtener etiquetas sobre la imagen, estas etiquetas son formateadas y traducidas(usando la API de Google Translate) para ser mostradas al usuario.

## Estructura del Proyecto

- **backend/**: API REST desarrollada en FastAPI que procesa las imágenes.
- **frontend/**: Interfaz web desarrollada con HTML, CSS y JS, expuesta a través de Flask para cargar imágenes.

## Ejecución del proyecto

Este proyecto puede ser ejecutado por a parte el backend y el frontend, para esto se pueden seguir las instrucciones del README dentro de cada carpeta; estas ejecuciones pueden hacerse tanto en python como con docker.

## Ejecución del proyecto completo usando docker composer

Para ejecutar el proyecto completo, primero debe estar configurado el archivo .env con las variables VISION_ENDPOINT, API_KEY y 
TRANSLATION_ENDPOINT.

Teniendo docker ejecutandose, ejecutar el siguiente comando para condtruír y ejecutar los contenedores:

docker-compose up --build

### Acceder a las Aplicaciones

- **Frontend**: http://localhost:5000
- **Backend API**: http://localhost:8000

### Variables de Entorno
Asegúrate de que el archivo `.env` esté configurado correctamente, el archivo env.example es un ejemplo de como podría quedar.

### Puertos en Uso
Si los puertos 5000 o 8000 están ocupados, puedes modificarlos en el `docker-compose.yml`.

