import uvicorn
from typing import Annotated
from fastapi import FastAPI, APIRouter, File, HTTPException, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from analisis.analisis_imagen import obtener_analisis

# API con FastAPI
app = FastAPI(title="EtiquetasImagen",docs_url="/api/docs", redoc_url=None)

v1_router = APIRouter(prefix="/api")

#Inclusión del host frontend para aceptar las peticiones
origins = [
    "http://localhost:5000", #Para el consumo desde el proyecto frontend
]

#Configuración CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Ruta para analizar una imagen
# input: archivo cargado
# otput: Json entregado por la función obtener_analisis del modulo anlisis
@v1_router.post("/analyze")
def analizar_imagen(file: UploadFile):
    try:
        if "image" in file.content_type: #Validación que el tipo de archivo sea imagen
            json = obtener_analisis(file.file.read())
            return json
        else:
            raise HTTPException(status_code=400, detail="El archivo no es una imagen.")     
    except  KeyError as err:
        raise HTTPException(status_code=400, detail="Ocurrión un error al llamar la API, verifique las variables de entorno.")
    except Exception as err:
        raise HTTPException(status_code=400, detail=f"Ocurrió una excepción {err=}, {type(err)=}")

app.include_router(v1_router)

if __name__ == "__main__":
    # Run this as a server directly.
    port = 8000
    print(f"Running the FastAPI server on port {port}.")
    uvicorn.run("api_handler:app", host="0.0.0.0", port=port)
