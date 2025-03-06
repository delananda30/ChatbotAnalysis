# Chatbot Analysis dengan Streamlit

<table>
  <tr>
    <td><img src="https://github.com/user-attachments/assets/1835125c-eadb-4117-902a-f9139014a263" width="300"></td>
    <td><img src="https://github.com/user-attachments/assets/681f453d-45c4-479e-aada-f5fbdd39104a" width="300"></td>
  </tr>
  <tr>
    <td><img src="https://github.com/user-attachments/assets/87dffbdf-8caf-49bd-aec5-54f58d876253" width="300"></td>
    <td><img src="https://github.com/user-attachments/assets/562874b8-1f57-4dbb-86e0-0074735485a4" width="300"></td>
  </tr>
</table>


Proyek ini adalah aplikasi berbasis Streamlit yang mengimplementasikan chatbot menggunakan model Gemini dari Google Generative AI. Selain itu, aplikasi ini juga menyediakan analisis percakapan berbasis sentimen dan kata kunci.

## 📌 Fitur Utama
- **Chatbot Interaktif**: Menggunakan model Gemini untuk menjawab pertanyaan pengguna.
- **Analisis Sentimen**: Mengkategorikan sentimen percakapan menjadi POSITIVE, NEGATIVE, atau NEUTRAL.
- **Word Cloud & Kata Kunci**: Mengekstrak kata kunci dari percakapan untuk mendapatkan wawasan topik.
- **Statistik Percakapan**: Menampilkan jumlah chat, rata-rata kata per chat, total durasi percakapan, dan lainnya.

## 🛠 Teknologi yang Digunakan
- Python 3.12.9
- [Streamlit](https://streamlit.io/) (1.43.0)
- [Google Generative AI](https://ai.google.dev/) (0.8.4)
- [Streamlit-Chat](https://github.com/AI-Yash/st-chat) (0.1.1)
- [NLTK](https://www.nltk.org/) (3.9.1)
- [LangDetect](https://pypi.org/project/langdetect/) (1.0.9)
- [Pandas](https://pandas.pydata.org/) (2.0.1)
- [Plotly](https://plotly.com/) (5.18.0)
- [WordCloud](https://github.com/amueller/word_cloud) (1.9.4)
- [Scikit-Learn](https://scikit-learn.org/) (1.2.2)

## 🚀 Cara Instalasi
### 1. Clone Repository
```bash
git clone https://github.com/username/chatbot-analysis.git
cd chatbot-analysis
```

### 2. Buat Virtual Environment (Opsional)
```bash
python -m venv venv
source venv/bin/activate  # Untuk macOS/Linux
venv\Scripts\activate    # Untuk Windows
```

### 3. Instal Dependensi
```bash
pip install -r requirements.txt
```

### 4. Konfigurasi API Key
Buat file `.env` dan tambahkan API Key dari Google AI:
```env
GOOGLE_API_KEY=your_api_key_here
```

### 5. Jalankan Aplikasi
```bash
streamlit run chatbot.py
```

## 📂 Struktur Proyek
```
chatbot-analysis/
│── chatbot.py        # Chatbot utama
│── analysis.py       # Analisis percakapan
│── requirements.txt  # Daftar dependensi
│── .env              # API Key (tidak disertakan dalam repo)
│── README.md         # Dokumentasi
```

## 📈 Analisis Percakapan
- **Sentimen Chat**: Ditampilkan dalam bentuk pie chart dan bar chart.
- **Word Cloud**: Visualisasi kata kunci dari percakapan.
- **Statistik Chat**: Total percakapan, durasi rata-rata, dan lainnya.

## ✅ TODO List
- [ ] Integrasi database untuk menyimpan histori chat.
- [ ] Implementasi model NLP untuk analisis topik lebih mendalam.
- [ ] Menambahkan fitur konfigurasi bahasa secara manual.

## 📜 Lisensi
Proyek ini menggunakan lisensi MIT. Silakan cek file `LICENSE` untuk detail lebih lanjut.

---

Jika Anda menemukan bug atau memiliki saran, jangan ragu untuk mengajukan issue atau pull request! 🚀

