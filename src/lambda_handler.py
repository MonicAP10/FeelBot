import requests
import json
import os
from dotenv import load_dotenv


# Cargar las variables de entorno desde el archivo .env
load_dotenv()

# Obtener la URL de la API Lambda y la clave de API de OpenAI desde las variables de entorno

def send_request_to_lambda(data):
    lambda_url = os.getenv("LAMBDA_API_URL")
    payload = json.dumps(data, ensure_ascii=False)
    lambda_response = requests.post(lambda_url, data=payload)
    return lambda_response

# Función para procesar la respuesta de la función Lambda
def process_lambda_response(lambda_result):
    try:
        # Verificar si la cadena JSON es válida
        body_content = json.loads(lambda_result["body"])
        
        # Si la cadena JSON es válida, proceder con el procesamiento
        print("modified emotion:", body_content)
        
        # Guardar el JSON en el archivo
        with open("modified_emotion.json", "w") as lambda_file:
            json.dump(body_content, lambda_file, indent=2, ensure_ascii=False)
        
        # Leer el archivo y guardar el contenido en una variable
        with open("modified_emotion.json", "r") as lambda_file:
            modified_emotions = json.load(lambda_file)

        # Opcionalmente, si deseas imprimir el contenido de la variable:
        print("Contenido guardado en la variable:", modified_emotions)
        
        return modified_emotions

    except json.JSONDecodeError as e:
        return None
    
def modify_emotions_in_lambda(data):
    try:
        lambda_response = send_request_to_lambda(data)
        if lambda_response.status_code == 200:
            lambda_result = lambda_response.json()
            modified_emotions = process_lambda_response(lambda_result)
            return modified_emotions
        else:
            print(f"Error from Lambda: {lambda_response.text}")
            return None
    except Exception as e:
        print(f"Error al comunicarse con la función Lambda: {e}")
        return None

