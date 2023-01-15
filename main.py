import streamlit as st

st.markdown("### Kakaotalk Spoiler Maker")

title = st.text_input("Enter title", "< Spoiler >")
text = st.text_input("Enter text", "content")
blank = '\u200b' * 500
result = title + blank + '\n' + text
st.text_area("Result", result)