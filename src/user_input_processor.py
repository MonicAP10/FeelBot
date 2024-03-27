import streamlit as st
from src.gpt_model import get_gpt_response

def process_user_input(user_input):
    user_message = user_input
    question = "Identifica en el rango de [-1, 1] los valores para las emociones de Activo, Alerta, Emocionado, Entusiasta, Determinado, Inspirado, Orgulloso, Interesado, Fuerte, Hostil, Avergonzado, Culpable, Angustiado, Molesto, Asustado, Miedo, Inquieto, Irritable, Nervioso. que están en" + user_message + "?" 
    modified_emotions = get_gpt_response(question, list(st.session_state["messages"]), is_first_question=True)
    
    if modified_emotions is not None:
        # Después de procesar las emociones, hacer otra pregunta
        question_2 = "Con esto " + user_input + " y esto " + str(modified_emotions) + ". ¿Puedes ayudarme a redactar una respuesta con empatía y aumentando el estado con las emociones modificadas que te envié?"
        response_2 = get_gpt_response(question_2, list(st.session_state["messages"]), is_first_question=False)
        if response_2 is not None:
            if "\n" in response_2:
                response_2 = response_2.split("\n", 1)[1]  
            st.chat_message("assistant").write(response_2)
            return response_2
        else:
            st.error("No se pudo obtener una respuesta del modelo. Por favor, inténtalo de nuevo más tarde.")
    return None