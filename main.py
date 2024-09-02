from pytube import YouTube, StreamQuery
import streamlit as st

#最高の画質と音質を動画をダウンロードする
fmt = "video"
def download_file(stream, fmt):
    """  """
    title = stream.title + '.'+ stream_final.subtype

    stream.download(filename=title)
    
text = st.text_input("URL：")

if text != "":#動画のURLを指定
    download_file(text, fmt)
