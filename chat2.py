import streamlit as st
from openai import OpenAI
import time

with st.sidebar:
    openai_api_key = st.text_input("OpenAI API Key", key="chatbot_api_key", type="password")
    uploaded_file = st.file_uploader("Choose a file")
    #"[Get an OpenAI API key](https://platform.openai.com/account/api-keys)"
    #"[View the source code](https://github.com/streamlit/llm-examples/blob/main/Chatbot.py)"
    #"[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/streamlit/llm-examples?quickstart=1)"

i = 0.5
st.image("C:/Users/SE922PU/OneDrive - EY/Desktop/zzz/고객사로고..png", width=81)
st.title("💬 Multi-Modal RAG Chatbot")
col1, col2, col3 = st.columns([4, 0.5, 0.1])
with col1:
    st.write("\n")
    st.write("\n")
with col2:
    st.caption("🚀🚀🚀   created by")
with col3:
    st.image("C:/Users/SE922PU/OneDrive - EY/Desktop/zzz/이와이로고.png", width=36)


if "messages" not in st.session_state: # 챗봇 맨처음 상황
    st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"]) # 이전기록 화면 출력
    i += 0.5
  
if prompt := st.chat_input("Type a message👋"):
    if uploaded_file is not None:
        st.image(uploaded_file)
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt) # 화면 출력
    # response = f"{i}" #client.chat.completions.create(model="gpt-3.5-turbo", messages=st.session_state.messages) # 답변
    with st.spinner('작성 중..'):
        time.sleep(1)
        msg = f"{i}" #response.choices[0].message.content
    st.session_state.messages.append({"role": "assistant", "content": msg})
    st.chat_message("assistant").write(msg) # 화면 출력
