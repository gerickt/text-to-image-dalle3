# Usar una imagen base oficial de Python
FROM python:3.9-slim

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar los archivos de requisitos e instalar las dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto del código fuente de la aplicación
# Copiar el archivo .env
COPY .env .env
COPY . .

# Exponer el puerto que Flask usará
EXPOSE 5000

# Definir el comando para ejecutar la aplicación
CMD ["flask", "run", "--host=0.0.0.0"]
