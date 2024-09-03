from __future__ import unicode_literals
import yt_dlp

import streamlit as st
import urllib.request

url = st.text_input("youtubeのURL")

ydl_opts = {
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])


import os

dir_path = ""

files = os.listdir(dir_path)

video_file = open(files[0], "rb")
video_bytes = video_file.read()

st.video(video_bytes)

