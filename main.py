from __future__ import unicode_literals
import yt_dlp

import streamlit as st
import urllib.request

url = st.text_input("youtubeのURL")

ydl_opts = {
    'format':'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]',
    'outtmpl':url + "mp4",
}


with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])

video_file = open(url + "mp4", "rb")
video_bytes = video_file.read()

st.video(video_bytes)

