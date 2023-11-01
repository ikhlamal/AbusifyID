import streamlit as st
import abusify_id as ai

# Fungsi untuk mengakses tiga fungsi abusify-id
def process_text(text):
    prediction = ai.predict_abusiveness(text)
    detection = ai.abusiveword_detector(text)
    filtered_text = ai.abusiveword_filter(text)

    return prediction, detection, filtered_text

# Aplikasi Streamlit
st.title("Abusify Streamlit App")

# Input teks
input_text = st.text_area("Masukkan teks:")

# Membuat kolom dengan layout horizontal
col1, col2, col3, col4 = st.columns(4)

# Tombol "Predict"
if col1.button("Predict"):
    if input_text:
        prediction, _, _ = process_text(input_text)
        col1.write("Prediksi Tingkat Abusiveness:", prediction)

# Tombol "Detect"
if col2.button("Detect"):
    if input_text:
        _, detection, _ = process_text(input_text)
        col2.write("Deteksi Kata Kasar:", detection)

# Tombol "Filter"
if col3.button("Filter"):
    if input_text:
        _, _, filtered_text = process_text(input_text)
        col3.write("Teks Setelah Difilter:", filtered_text)

# Tombol "Submit" untuk menampilkan output semua fungsi
if col4.button("Submit"):
    if input_text:
        prediction, detection, filtered_text = process_text(input_text)
        col4.write("Prediksi Tingkat Abusiveness:", prediction)
        col4.write("Deteksi Kata Kasar:", detection)
        col4.write("Teks Setelah Difilter:", filtered_text)
