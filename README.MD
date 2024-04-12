# text-to-image-dalle3

Este proyecto es un servicio simple basado en Flask para generar imágenes utilizando DALL·E 3 de OpenAI.

## Disclaimer

Este ejemplo no debe utilizarse en un entorno de producción, ya que no se han implementado medidas de seguridad en el endpoint.

## Requisitos

- Docker
- Clave API de OpenAI

## Instrucciones de Uso

1. **Clonar el repositorio:**
   ```
   git clone https://github.com/gerickt/text-to-image-dalle3.git
   ```
2. **Navegar al directorio del proyecto:**
   ```
   cd text-to-image-dalle3
   ```
3. **Configurar el archivo .env:**
    - Copia el archivo de ejemplo y edita el nuevo archivo `.env` para incluir tu clave API de OpenAI:
    ```
    cp .env.example .env
    ```
4. **Construir la imagen de Docker:**
   ```
   docker build -t text-to-image-dalle3 .
   ```
5. **Ejecutar el contenedor:**
   - Este comando ejecuta la aplicación en el puerto 5000:
    ```
     docker run -p 5000:5000 text-to-image-dalle3
    ```

## Contribuciones

Para contribuir a este proyecto, sigue estos pasos:

1. **Fork del repositorio:**
   - Haz un fork del repositorio a tu cuenta de GitHub.
2. **Crear una nueva rama:**
   ```
   git checkout -b tu-nueva-rama
   ```
3. **Realiza tus cambios:**
   - Haz tus cambios y haz commit:
    ```
    git commit -am "Descripción de los cambios"
    ```
4. **Subir los cambios a tu fork:**
   ```
   git push origin tu-nueva-rama
   ```
5. **Crear un pull request:**
   - Abre un pull request en el repositorio original para que tus cambios sean considerados.

## Licencia

Este proyecto está licenciado bajo la Licencia GPL v3.
