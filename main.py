import streamlit as st
from pytube import YouTube, StreamQuery

if st.text_input("youtubeのURL"):
    tube = YouTube(url)
    tube.download(filename="video.mp4")
    video_file = open("video.mp4", "rb")
    video_bytes = video_file.read()

    st.video(video_bytes)
