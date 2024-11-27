FROM python:3.9-slim

# Configuración del contenedor
WORKDIR /app

# Copiar y configurar dependencias
COPY requirements.txt .
RUN apt-get update && apt-get install -y \
    libpq-dev \
    postgresql-client && \
    pip install --no-cache-dir -r requirements.txt

# Copiar el código de la aplicación
COPY . .

# Exponer puerto
EXPOSE 80

# Comando de inicio
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
