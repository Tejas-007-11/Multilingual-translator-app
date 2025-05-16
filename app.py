# app.py
import streamlit as st
from translator import translate

st.set_page_config(page_title="Multilingual Translator", layout="centered")

st.title("🌍 Multilingual Translator App")
st.markdown("Translate text from one language to another using AI!")

text_input = st.text_area("Enter text to translate")

col1, col2 = st.columns(2)
with col1:
    src_lang = st.selectbox("From", ['en', 'fr', 'de', 'es', 'hi', 'ja'])
with col2:
    tgt_lang = st.selectbox("To", ['en', 'fr', 'de', 'es', 'hi', 'ja'])

if st.button("Translate"):
    if src_lang == tgt_lang:
        st.warning("Source and target languages must be different.")
    elif text_input.strip() == "":
        st.warning("Please enter some text to translate.")
    else:
        with st.spinner("Translating..."):
            try:
                output = translate(text_input, src_lang, tgt_lang)
                st.success("Translation complete!")
                st.markdown(f"**Translated Text:**\n\n{output}")
            except Exception as e:
                st.error(f"Translation failed: {str(e)}")
