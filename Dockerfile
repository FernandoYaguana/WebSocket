# Usa una imagen base con Python
FROM python:3.9-slim

# Establece el directorio de trabajo
WORKDIR /app

# Copia el archivo del código Python
COPY . /app

# Instala las dependencias necesarias
RUN pip install websockets

# Expone el puerto 8765
EXPOSE 8765

# Ejecuta el servidor WebSocket
CMD ["python", "server.py"]