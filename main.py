import streamlit as st
import urllib.request

url = st.text_input("youtubeのURL")
urllib.request.urlretrieve(url, './ex.html')
