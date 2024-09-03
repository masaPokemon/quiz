import streamlit as st
from pytube import YouTube, StreamQuery
url = st.text_input("youtubeのURL")
if url != "":
    tube1 = YouTube(url)
    tube2 = tube1.streams
    tube2.download(filename="video.mp4")
    video_file = open("video.mp4", "rb")
    video_bytes = video_file.read()

    st.video(video_bytes)
