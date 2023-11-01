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

# Tombol-tombol
if st.button("Submit"):
    if input_text:
        prediction, detection, filtered_text = process_text(input_text)
        st.write("Prediksi Tingkat Abusiveness:", prediction)
        st.write("Deteksi Kata Kasar:", detection)
        st.write("Teks Setelah Difilter:", filtered_text)

st.button("Predict")
st.button("Detect")
st.button("Filter")
