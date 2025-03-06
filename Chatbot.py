import os
import time
import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
from streamlit_chat import message
from langdetect import detect

load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    st.error("API Key tidak ditemukan! Pastikan file .env berisi GOOGLE_API_KEY.")
    st.stop()

genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-1.5-flash-latest')

st.set_page_config(page_title="Chatbot Gemini", layout="centered")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "sentiments" not in st.session_state:
    st.session_state.sentiments = []  
if "topics" not in st.session_state:
    st.session_state.topics = []
if "durations" not in st.session_state:
    st.session_state.durations = []  
if "chat_timestamps" not in st.session_state:
    st.session_state.chat_timestamps = []  
if "total_chats" not in st.session_state:
    st.session_state.total_chats = 0  

def get_language(text):
    try:
        return detect(text)
    except:
        return 'en'

def analyze_sentiment(text):
    try:
        prompt = f"Analyze the sentiment: '{text}'. Respond with POSITIVE, NEGATIVE, or NEUTRAL."
        response = model.generate_content(prompt)
        sentiment = response.text.strip().upper()
        return sentiment if sentiment in ["POSITIVE", "NEGATIVE", "NEUTRAL"] else "NEUTRAL"
    except:
        return "NEUTRAL"

st.title("Chatbot")

with st.sidebar:
    clear_button_container = st.empty()  

if clear_button_container.button("Clear Chat", use_container_width=True):
    st.session_state.chat_history = []
    st.session_state.sentiments = []
    st.session_state.topics = []
    st.session_state.durations = []
    st.session_state.chat_timestamps = []
    st.session_state.total_chats = 0

if prompt := st.chat_input("Ketik pesan Anda..."):
    start_time = time.time()  
    user_language = get_language(prompt)
    chat_history = "\n".join(st.session_state.chat_history)

    full_prompt = f"""
    You are an AI chatbot. The user is speaking in {user_language}.
    Always respond in {user_language}.
    This is the chat history:
    {chat_history}

    User: {prompt}
    AI:"""

    try:
        response = model.generate_content(full_prompt)
        chatbot_response = response.text.strip()
        sentiment_label = analyze_sentiment(prompt)

        st.session_state.chat_timestamps.append(start_time)

        if len(st.session_state.chat_timestamps) > 1:
            duration = start_time - st.session_state.chat_timestamps[-2]
            st.session_state.durations.append(duration)

        st.session_state.total_chats += 1

        st.session_state.chat_history.append(f"User: {prompt}")
        st.session_state.chat_history.append(f"AI: {chatbot_response}")
        st.session_state.sentiments.append((prompt, sentiment_label))  
        st.session_state.topics.append(prompt)

    except:
        chatbot_response = "Maaf, terjadi kesalahan."

for i, chat_entry in enumerate(st.session_state.chat_history):
    message(chat_entry, is_user=chat_entry.startswith("User:"), key=f"chat_{i}")
