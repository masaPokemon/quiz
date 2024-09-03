import streamlit as st
from pytube import YouTube, StreamQuery
vid_url = st.text_input("youtubeのURL")
yt = YouTube(url)
if yt != "":
    with open(yt,'rb') as fh:
        st.download_button(
            label = 'Download Video',
            data = fh,
            file_name = os.path.basename(file_url)
        )
    video_file = open("video.mp4", "rb")
    video_bytes = video_file.read()

    st.video(video_bytes)
