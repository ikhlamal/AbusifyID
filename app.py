import streamlit as st
import abusify_id as ai

# Fungsi untuk mengakses tiga fungsi abusify-id
def process_text(text):
    prediction = ai.predict_abusiveness(text)
    detection = ai.abusiveword_detector(text)
    filtered_text = ai.abusiveword_filter(text)

    return prediction, detection, filtered_text

# Aplikasi Streamlit
st.title("AbusifyID")
st.write("Abusiveness Verification in Bahasa Indonesia.")

# Input teks
input_text = st.text_area("", placeholder="Input Text Here")

# Membuat tiga kolom dengan CSS untuk mengatur tampilan tombol-tombol
col1, col2, col3, col4 = st.columns(4)
col1.markdown(
    f'<style>div.stButton > button {{width: 100%; text-align: center;}}</style>',
    unsafe_allow_html=True,
)
col2.markdown(
    f'<style>div.stButton > button {{width: 100%; text-align: center;}}</style>',
    unsafe_allow_html=True,
)
col3.markdown(
    f'<style>div.stButton > button {{width: 100%; text-align: center;}}</style>',
    unsafe_allow_html=True,
)
col4.markdown(
    f'<style>div.stButton > button {{width: 100%; text-align: center;}}</style>',
    unsafe_allow_html=True,
)

# Tombol "Submit"
if col1.button("Submit"):
    if input_text:
        prediction, detection, filtered_text = process_text(input_text)
        st.write("Abusiveness Level:", st.info(prediction))
        st.write("Abusive Words Detected:", st.info(detection))
        st.write("Abusive Words Filtered:", st.info(filtered_text))

# Tombol "Predict"
if col2.button("Predict"):
    if input_text:
        prediction, _, _ = process_text(input_text)
        st.write("Prediksi Tingkat Abusiveness:", prediction)

# Tombol "Detect"
if col3.button("Detect"):
    if input_text:
        _, detection, _ = process_text(input_text)
        st.write("Deteksi Kata Kasar:", detection)

# Tombol "Filter"
if col4.button("Filter"):
    if input_text:
        _, _, filtered_text = process_text(input_text)
        st.write("Teks Setelah Difilter:", filtered_text)
