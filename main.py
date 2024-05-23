from fastapi import FastAPI
from api import router as api_router

# Crear una instancia de FastAPI llamada app
app = FastAPI()

# Incluir los endpoints de la API definidos en api_router en la aplicación FastAPI
app.include_router(api_router)


# Este bloque se ejecuta solo si este archivo se ejecuta como script principal
if __name__ == "__main__":
    import uvicorn            # Importar uvicorn para ejecutar la aplicación en un servidor web
    uvicorn.run(app, host="0.0.0.0", port=8000)     # Ejecutar la aplicación en el host 0.0.0.0 y el puerto 8000
