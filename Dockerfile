# imagen
FROM python:3.11-slim

# carpeta dentro del contenedor
WORKDIR /app

# archivo de dependencias
COPY requirements.txt .

# librerías
RUN pip install --no-cache-dir -r requirements.txt

# Copiamos todo el proyecto al contenedor
COPY . .

# Abrimos el puerto 8000 (FastAPI)
EXPOSE 8000

# Comando que arranca la app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]