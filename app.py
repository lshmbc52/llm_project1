import streamlit as st
from utils import ChatGPT, openai_api_key

if 'client' not in st.session_state:
    st.session_state['client'] = ChatGPT(openai_api_key=openai_api_key)
chatbot = st.session_state['client']
prompt = st.chat_input("채팅")
if prompt:
    messages = chatbot.chatting(prompt)
    for message in messages[1:]:
        if message["role"] == "user":
            with st.chat_message("human"):
                st.write(message['content'])
        else:
            with st.chat_message("ai"):
                st.write(message['content'])