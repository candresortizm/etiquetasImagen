from dotenv import load_dotenv
from pydantic import BaseModel
import os
from dotenv import load_dotenv
import base64, requests, json
from typing import List

load_dotenv()

#Estructura de los objetos que se retornan
class ElementoRespuesta(BaseModel):
    etiqueta: str
    valor: int

# Función que orquesta el flujo del analisis de la imagen
# input: [bytes] de la imagen
# output: listado de diccionarios con etiqueta y valor
def obtener_analisis(file: bytes) -> List[ElementoRespuesta]:
    try:
        json_etiquetas = invocar_api_etiquetas(file)
        etiquetas = [item["description"] for item in json_etiquetas["responses"][0]["labelAnnotations"]]
        valores = [item["score"] for item in json_etiquetas["responses"][0]["labelAnnotations"]]
        print(etiquetas) # Para ver las etiquetas y valores originales entregados por GCP
        print(valores)
        json_traduccion = invocar_api_traduccion(etiquetas)
        etiquetas = [item["translatedText"] for item in json_traduccion["data"]["translations"]]
        json_respuesta = []
        for i in range(len(etiquetas)):
            json_respuesta.append({"etiqueta":etiquetas[i],"valor":valores[i]})
        return json_respuesta
    except KeyError as err:
        print("Variables de entorno no encontradas")
        print("Set them before running this sample.")
        raise
    except Exception as err:
        print(f"Error inesperado {err=}, {type(err)=}")
        raise

# Función que hace el llamado del API para obtener las etiquetas de la imagen
# input: [bytes] de la imagen
# output: el json que entrega el API
def invocar_api_etiquetas(file: bytes):
    endpoint = os.environ["VISION_ENDPOINT"]
    key = os.environ["API_KEY"]
    
    url = f"{endpoint}?key={key}"

    #Convertir la imagen a base 64 para ser enviada al servicio de GCP
    img_b64 = base64.b64encode(file).decode("utf-8")

    payload = {
        "requests": [
            {
            "image": {"content": img_b64},
            "features": [{"type": "LABEL_DETECTION", "maxResults": 10}]
            }
        ]
    }

    resp = requests.post(url, json=payload, timeout=30)
    return resp.json()

# Función que hace el llamado del API para obtener la traducción de una lista de palabras
# input: lista de strings con palabras en inglés
# output: lista de strings con las palabras traducidas a español
def invocar_api_traduccion(listado_etiquetas: List[str]):
    try:
        endpoint = os.environ["TRANSLATION_ENDPOINT"]
        key = os.environ["API_KEY"]
        
        url = f"{endpoint}?key={key}"

        payload = {
                    "q": listado_etiquetas,
                    "source": "en",
                    "target": "es",
                    "format": "text"
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

