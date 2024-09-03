import streamlit as st
import urllib.request

from __future__ import unicode_literals
import youtube_dl

url = st.text_input("youtubeのURL")

ydl_opts = {}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])

video_file = open("youtube.mp4", "rb")
video_bytes = video_file.read()

st.video(video_bytes)

