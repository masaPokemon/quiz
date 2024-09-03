import streamlit as st
import requests

url=st.text_input("YoutubeのURL")
filename='youtube.mp4'

urlData = requests.get(url).content

with open(filename ,mode='wb') as f: # wb でバイト型を書き込める
  st.write(urlData)
  
