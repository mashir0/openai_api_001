
import streamlit as st
import openai

openai.api_key = st.secrets.OpenAIAPI.openai_api_key

if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role": "system", "content": "あなたは優秀なアシスタントAIです"}
    ]

def communicate():
    messages = st.session_state{"messages"}

    user_message = {"role": "user", "content": st.session_state["user_input"]}
    messages.append(user_message)

    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages=messages
    )

    bot_message = response["choices"][0]["message"]
    messages.append(bot_message)

    st.session_state["user_input"] = ""


st.title("my AI assistant")
st.write("ChtGPT bot")

user_input = st.text_input("メッセージを入力して下さい", key="user_input", on_change=communicate)

if st.session_state["messages"]:
    messages = st.session_state["messages"]

    for message in reversed(messages[1:]):
        speaker = "😃"
        if message["role"]=="assistant"
            speaker = "🤖"

        st.write(speaker + ": " + message["content"])
