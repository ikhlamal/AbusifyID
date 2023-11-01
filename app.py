# Tombol "Submit"
if col1.button("Submit"):
    if input_text:
        prediction, detection, filtered_text = process_text(input_text)
        st.info("Abusiveness Level: " + prediction)
        st.info("Abusive Words Detected: " + detection)
        st.info("Abusive Words Filtered: " + filtered_text)

# Tombol "Predict"
if col2.button("Predict"):
    if input_text:
        prediction, _, _ = process_text(input_text)
        st.info("Abusiveness Level: " + prediction)

# Tombol "Detect"
if col3.button("Detect"):
    if input_text:
        _, detection, _ = process_text(input_text)
        st.info("Abusive Words Detected: " + detection)

# Tombol "Filter"
if col4.button("Filter"):
    if input_text:
        _, _, filtered_text = process_text(input_text)
        st.info("Abusive Words Filtered: " + filtered_text)
