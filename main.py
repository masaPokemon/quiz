import streamlit as st
from pytube import YouTube, StreamQuery
vid_url = st.text_input("youtubeのURL")
yt = YouTube(vid_url).streams.first().download()
