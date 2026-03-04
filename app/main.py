# main.py

from fastapi import FastAPI, Query
from app.password_service import PasswordService
import webbrowser

# Creamos la aplicación FastAPI
app = FastAPI()

@app.on_event("startup")
def open_browser():
    webbrowser.open("http://127.0.0.1:8000/generate?length=12")

# Creamos una instancia del servicio
password_service = PasswordService()

@app.get("/")
def root():
    return {"message": "API funcionando correctamente"}


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
