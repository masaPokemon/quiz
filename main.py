import streamlit as st
from pytube import YouTube, StreamQuery
file_url = st.text_input("youtubeのURL")
if file_url != "":
    with open(file_url,'rb') as fh:
        st.download_button(
            label = 'Download Video',
            data = fh,
            file_name = os.path.basename(file_url)
        )
    video_file = open("video.mp4", "rb")
    video_bytes = video_file.read()

    st.video(video_bytes)
