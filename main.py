import streamlit as st
import pyperclip

title = st.text_input("Enter title", "-- Spoiler --")
text = st.text_input("Enter text", "content")
blank = '\u200b' * 500
result = title + blank + text
st.text_area("Result", result)

if st.button("Copy to clipboard"):
   pyperclip.copy(result)