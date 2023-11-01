import streamlit as st
import abusify_id as ai

st.title("Abusify Streamlit App")

input_text = st.text_area("Masukkan teks:")

if st.button("Submit"):
    if input_text:
        prediction, detection, filtered_text = process_text(input_text)
        st.write("Prediksi Tingkat Abusiveness:", prediction)
        st.write("Deteksi Kata Kasar:", detection)
        st.write("Teks Setelah Difilter:", filtered_text)

col1, col2, col3, col4 = st.columns(4)

if col1.button("Predict"):
    if input_text:
        prediction = ai.predict_abusiveness(input_text)
        st.write("Prediksi Tingkat Abusiveness:", prediction)

if col2.button("Detect"):
    if input_text:
        detection = ai.abusiveword_detector(input_text)
        st.write("Deteksi Kata Kasar:", detection)

if col3.button("Filter"):
    if input_text:
        filtered_text = ai.abusiveword_filter(input_text)
        st.write("Teks Setelah Difilter:", filtered_text)
