# Nombre del Proyecto

text-to-image-dalle3

## Requisitos

- Docker
- API from OpenAI

## Instrucciones de Uso

1. Clona el repositorio: `git clone https://github.com/gerickt/text-to-image-dalle3.git`
2. Navega al directorio del proyecto: `cd text-to-image-dalle3`
3. Copia y edita el archivo .env para incluir tu clave de la AIP: `cp .env.example .env`
4. Construye la imagen de Docker: `docker build -t text-to-image-dalle3 .`
5. Ejecuta el contenedor: `docker run -p 5000:5000 text-to-image-dalle3`

## Contribuciones

Si deseas contribuir a este proyecto, por favor sigue los siguientes pasos:

1. Haz un fork del repositorio
2. Crea una rama para tu contribución: `git checkout -b nombre-rama`
3. Realiza tus cambios y haz commit: `git commit -m "Descripción de los cambios"`
4. Sube tus cambios a tu repositorio: `git push origin nombre-rama`
5. Abre un pull request en el repositorio original

## Licencia

Este proyecto está bajo la Licencia GPL v3.