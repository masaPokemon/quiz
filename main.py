import streamlit as st
from audio_recorder_streamlit import audio_recorder

audio_bytes = audio_recorder()

if st.button("Save Recording"):
    with open("recorded_audio.wav", "wb") as f:
        f.write(audio_bytes)
    st.success("Recording saved!")
