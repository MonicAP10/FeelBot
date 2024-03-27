# ChatEmotional

Este es un proyecto de chatbot que utiliza OpenAI GPT-3.5 para respuestas emocionales.

## Configuración

1. Copia el archivo `.env` y renómbralo a `.env`.
2. Completa las siguientes variables de entorno en el archivo `.env` con los valores correspondientes:
   - `OPENAI_API_KEY`: Clave de la API de OpenAI.
   - `LAMBDA_API_URL`: URL de la API Lambda.

## Ejecución

Para ejecutar el chatbot, puedes ejecutar el script `chatbot.py` desde la línea de comandos o IDE de Python.

```bash
python chatbot.py


Con esta estructura y configuración:

- Los archivos sensibles como la clave de API se mantienen fuera del control de versiones al ser listados en el archivo `.gitignore`.
- El archivo `.env` proporciona una plantilla clara para que los colaboradores puedan configurar sus propias variables de entorno.
- Las instrucciones en el archivo `README.md` guían a los usuarios sobre cómo configurar correctamente las variables de entorno antes de ejecutar el proyecto.

Esta configuración garantiza que tus claves y configuraciones sensibles estén protegidas y que otros colaboradores puedan configurar fácilmente su entorno de desarrollo.

