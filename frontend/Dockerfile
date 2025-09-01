FROM python:3.11-slim

WORKDIR /app

# Instalar dependencias del sistema
RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Copiar archivos de dependencias
COPY pyproject.toml .

# Instalar dependencias de Python
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir .

# Copiar código fuente y archivos estáticos
COPY src/ ./src/

# Exponer puerto
EXPOSE 5000

# Comando para ejecutar la aplicación
CMD ["python", "src/server.py"]
