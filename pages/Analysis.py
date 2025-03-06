import streamlit as st
import pandas as pd
import plotly.express as px
from wordcloud import WordCloud
import numpy as np
import re
import os
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import LatentDirichletAllocation
import google.generativeai as genai
from dotenv import load_dotenv
import nltk

nltk.download('punkt')
nltk.download('stopwords')

load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    st.error("API Key tidak ditemukan!")
    st.stop()

genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-1.5-flash-latest')

st.set_page_config(page_title="Analisis", layout="wide")

st.title("Analisis Chat")

def preprocess_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    words = word_tokenize(text)
    stop_words = set(stopwords.words('indonesian'))
    words = [word for word in words if word not in stop_words]
    stemmer = PorterStemmer()
    words = [stemmer.stem(word) for word in words]
    return " ".join(words)

def extract_keywords_using_api(text_data):
    try:
        combined_text = " ".join(text_data)
        prompt = f"""
        Dari teks berikut, ekstrak kata kunci utama yang paling sering muncul dan penting dalam percakapan.
        Pastikan kata kunci disajikan dalam bahasa asli percakapan dan dipisahkan dengan koma (,).
        
        Teks percakapan:
        {combined_text}
        
        Output hanya berupa daftar kata kunci tanpa penjelasan tambahan.
        """
        response = model.generate_content(prompt)
        keywords = response.text.strip().split(",")
        return keywords
    except Exception as e:
        return [f"Error: {str(e)}"]

with st.container():
    col1, col2, col3, col4 = st.columns(4)
    total_chats = st.session_state.get("total_chats", 0)
    with col1:
        st.markdown("Jumlah Chat")
        st.info(f"**{total_chats} chat**")
    if "topics" in st.session_state and st.session_state.topics:
        total_kata = sum(len(chat.split()) for chat in st.session_state.topics)
        avg_kata = total_kata / max(total_chats, 1)
    else:
        avg_kata = 0
    with col2:
        st.markdown("Rata-rata Kata")
        st.info(f"**{avg_kata:.2f} kata**")
    total_durasi = sum(st.session_state.get("durations", []))
    total_durasi_jam = total_durasi / 3600
    with col3:
        st.markdown("Total Waktu")
        st.info(f"**{total_durasi_jam:.2f} jam**")
    avg_durasi = total_durasi / max(total_chats, 1)
    with col4:
        st.markdown("Rata-rata Waktu")
        st.info(f"**{avg_durasi:.2f} detik**")

st.divider()

st.subheader("Sentimen")

if "sentiments" in st.session_state and st.session_state.sentiments:
    df_sentimen = pd.DataFrame(st.session_state.sentiments, columns=["Teks", "Sentimen"])
    df_sentimen["Sentimen"] = df_sentimen["Sentimen"].str.upper()
    sentiment_counts = df_sentimen["Sentimen"].value_counts().reset_index()
    sentiment_counts.columns = ["Sentimen", "Jumlah"]
    sentiment_counts["Persentase"] = (sentiment_counts["Jumlah"] / sentiment_counts["Jumlah"].sum()) * 100
    colormap = px.colors.sequential.Blues
    warna_sentimen = {sentiment: colormap[i] for i, sentiment in enumerate(sentiment_counts["Sentimen"])}
    col1, col2 = st.columns([2, 2])
    with col1:
        fig_pie = px.pie(
            sentiment_counts, names="Sentimen", values="Persentase", 
            title="Distribusi Sentimen",
            color="Sentimen",
            color_discrete_map=warna_sentimen,
            hole=0.4
        )
        fig_pie.update_layout(title_font=dict(size=20))
        st.plotly_chart(fig_pie, use_container_width=True)
    with col2:
        fig_bar = px.bar(
            sentiment_counts, x="Sentimen", y="Jumlah", 
            color="Sentimen",
            color_discrete_map=warna_sentimen,
            title="Jumlah Chat per Sentimen"
        )
        fig_bar.update_layout(title_font=dict(size=20))
        st.plotly_chart(fig_bar, use_container_width=True)
else:
    st.warning("Belum ada data sentimen.")

st.divider()

st.subheader("Kata Kunci")
if "topics" in st.session_state and st.session_state.topics:
    keywords = extract_keywords_using_api(st.session_state.topics)
    combined_text = " ".join(keywords)
    wordcloud = WordCloud(width=800, height=400, background_color="white").generate(combined_text)
    wordcloud.recolor(colormap="Blues")
    wordcloud_image = wordcloud.to_image()
    wordcloud_array = np.array(wordcloud_image)
    fig_wc = px.imshow(wordcloud_array)
    fig_wc.update_layout(
        xaxis_visible=False,
        yaxis_visible=False,
        plot_bgcolor='white',
    )
    st.plotly_chart(fig_wc, use_container_width=True)
else:
    st.warning("Belum ada data kata kunci.")
