from yt_dlp import YoutubeDL
import streamlit as st

#最高の画質と音質を動画をダウンロードする
ydl_opts = {
    'outtmpl': 'video.mp4',
    'format': 'best'
}
text = st.text_input("URL：")

if text != "":#動画のURLを指定
    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([text])
    files.download('video.mp4')
