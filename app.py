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

# Membuat satu kolom untuk menampilkan tombol secara horizontal
col1 = st.columns(1)

# Tombol "Predict"
if col1.button("Predict"):
    if input_text:
        prediction, _, _ = process_text(input_text)
        st.write("Prediksi Tingkat Abusiveness:", prediction)

# Tombol "Detect"
if col1.button("Detect"):
    if input_text:
        _, detection, _ = process_text(input_text)
        st.write("Deteksi Kata Kasar:", detection)

# Tombol "Filter"
if col1.button("Filter"):
    if input_text:
        _, _, filtered_text = process_text(input_text)
        st.write("Teks Setelah Difilter:", filtered_text)

# Tombol "Submit" untuk menampilkan output semua fungsi
if col1.button("Submit"):
    if input_text:
        prediction, detection, filtered_text = process_text(input_text)
        st.write("Prediksi Tingkat Abusiveness:", prediction)
        st.write("Deteksi Kata Kasar:", detection)
        st.write("Teks Setelah Difilter:", filtered_text)
