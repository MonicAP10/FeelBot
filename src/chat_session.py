import streamlit as st

def initialize_session():
    """
    Inicializa la sesión del chat.
    """
    if "messages" not in st.session_state:
        st.session_state["messages"] = [{"role": "assistant", "content": "Hello, I'm ChatGPT Emotional, ¿Can I help you?"}]

def display_messages(messages):
    """
    Muestra los mensajes en la interfaz de usuario.
    """
    for msg in messages:
        if msg["role"] == "user" or msg["role"] == "assistant":
            st.chat_message(msg["role"]).write(msg["content"])

def get_user_input():
    """
    Obtiene la entrada del usuario.
    """
    user_input = st.chat_input()
    if user_input:
        st.session_state["messages"].append({"role": "user", "content": user_input})
        st.chat_message("user").write(user_input)
        return user_input
    return None
