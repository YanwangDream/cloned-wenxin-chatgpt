import streamlit as st
import streamlit.components.v1 as components
import requests
import json
from wenxin_utils import get_wenxinchat_response
import streamlit as st
from langchain.memory import ConversationBufferMemory


st.title("💬 克隆ChatGPT")

with st.sidebar:
    api_key = st.text_input('请输入API Key：', type="password")
    secret_key = st.text_input('请输入Secret Key：', type="password")
    st.markdown("[获取文心一言 API Key和Secret Key](https://console.bce.baidu.com/)")

if "memory" not in st.session_state:
    st.session_state["memory"] = ConversationBufferMemory(return_messages=True)
    st.session_state["messages"] = [{"role": "AI",
                                     "content": "您好，我是你的AI助手，有什么可以帮助你的吗？"}]

for message in st.session_state["messages"]:
    st.chat_message(message["role"]).write(message["content"])

prompt = st.chat_input()
if prompt:
    if not api_key:
        st.info("请输入你的文心一言 API Key和Secret Key")
        st.stop()
    st.session_state["messages"].append({"role": "human", "content": prompt})
    st.chat_message("human").write(prompt)

    with st.spinner("AI正在思考中，请稍等..."):
        response = get_wenxinchat_response(st.session_state["memory"],prompt, api_key,secret_key)
    msg = {"role": "ai", "content": response}
    st.session_state["messages"].append(msg)
    st.chat_message("ai").write(response)