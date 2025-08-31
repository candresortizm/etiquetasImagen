from dotenv import load_dotenv
import os
from dotenv import load_dotenv
import base64, requests, json

load_dotenv()

# Función que hace el llamado del API para obtener las etiquetas de la imagen
# input: [bytes] de la imagen
# output: el mismo json que entrega el API
# TODO: limpiar el json y traducir etiquetas
def obtener_analisis(file):
    try:
        endpoint = os.environ["VISION_ENDPOINT"]
        key = os.environ["VISION_KEY"]
        
        url = f"{endpoint}?key={key}"

        #Convertir la imagen a base 64 para ser enviada al servicio de GCP
        img_b64 = base64.b64encode(file).decode("utf-8")

        payload = {
        "requests": [
            {
            "image": {"content": img_b64},
            "features": [{"type": "LABEL_DETECTION", "maxResults": 15}]
            }
        ]
        }

        resp = requests.post(url, json=payload, timeout=30)

        return resp.json()
    except KeyError as err:
        print("Variables de entorno no encontradas")
        print("Set them before running this sample.")
        raise
    except Exception as err:
        print(f"Error inesperado {err=}, {type(err)=}")
        raise

