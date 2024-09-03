import streamlit as st

VIDEO_URL = st.text_input("YoutubeのURL")
st.video(VIDEO_URL)

#import streamlit as st
#import urllib.request

#url = st.text_input("youtubeのURL")
#urllib.request.urlretrieve(url, 'youtube.mp4')
#st.video

#video_file = open("youtube.mp4", "rb")
#video_bytes = video_file.read()

#st.video(video_bytes)
