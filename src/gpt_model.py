import openai
import os
from dotenv import load_dotenv
from src.emotion_extractor import extract_emotions
from src.emotion_modifier import modify_emotions

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def get_gpt_response(question, messages, is_first_question):
    if is_first_question:
        messages.append({"role": "user", "content": question})
    
    try:
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages
        )
    except Exception as e:
        print(f"Error al obtener respuesta del modelo: {e}")
        return None
    
    response_message_content = response.choices[0].message.content
    print("Respuesta del modelo:", response_message_content)
    
    emotions = extract_emotions(response_message_content)
    print("emotions", emotions)
    if emotions:
        modify_emotions(emotions)
    return response_message_content
