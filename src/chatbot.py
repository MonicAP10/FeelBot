import sys
sys.path.append('.')

import streamlit as st
from src.chat_session import initialize_session, display_messages, get_user_input
from src.user_input_processor import process_user_input


def main():
    st.title("FeelBot")
    initialize_session()
    display_messages(st.session_state["messages"])

    user_input = get_user_input()
    if user_input:
        last_response = process_user_input(user_input)
        if last_response is not None:
            st.session_state["messages"].append({"role": "assistant", "content": last_response})

if __name__ == "__main__":
    main()