import streamlit as st
from src.gpt_model import get_gpt_response

def process_user_input(user_input):
    user_message = user_input
    question = "Identifica las emociones positivas en un rango de [0, 1.0] [Activo, Alerta, Emocionado, Entusiasta, Determinado, Inspirado, Orgulloso, Interesado, Fuerte,] y las emociones negativas en el rango de [-1.0,0] [ Hostil, Avergonzado, Culpable, Angustiado, Molesto, Asustado, Miedo, Inquieto, Irritable, Nervioso]. que están en" + user_message + "y creame una lista con las emociones que ya te dije que se encuentran en el texto y su valor, ejemplo Atento : 0.5"
    modified_emotions = get_gpt_response(question, list(st.session_state["messages"]), is_first_question=True)
    
    if modified_emotions is not None:
        # Después de procesar las emociones, hacer otra pregunta
        question_2 = "Tengo la entrada del usuario " + user_input + " y tengo el arreglo de emociones modificadas " + str(modified_emotions) + " Ahora quiero que me ayudes a redactar una respuesta con empatía y aumentando el estado con las emociones modificadas."
        response_2 = get_gpt_response(question_2, list(st.session_state["messages"]), is_first_question=False)
        if response_2 is not None:
            if "\n" in response_2:
                response_2 = response_2.split("\n", 1)[1]  
            st.chat_message("assistant").write(response_2)
            return response_2
        else:
            st.error("No se pudo obtener una respuesta del modelo. Por favor, inténtalo de nuevo más tarde.")
    return None