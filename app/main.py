# main.py

from fastapi import FastAPI, Query
from app.password_service import PasswordService

# Creamos la aplicación FastAPI
app = FastAPI()

# Creamos una instancia del servicio
password_service = PasswordService()


@app.get("/health")
def health_check():

    return {"status": "ok"}


@app.get("/generate")
def generate_password(length: int = Query(8, description="Longitud de la contraseña")):
    
    try:
        password = password_service.generate_password(length)

        return {
            "success": True,
            "length": length,
            "password": password
        }

    except ValueError as e:
        return {
            "success": False,
            "error": str(e)
        }
