# 音声を日本語に翻訳

######## Streamlitの設定 ########
import streamlit as st

st.title("音声で入力する")
st.write("マイクに話しかけてください。")

######## 録音関係の設定 ########
import pyaudio
import wave

p = pyaudio.PyAudio()  # PyAudioのインスタンス化

######## 音声翻訳関係の設定 ########
import openai

# ハルっているか判定する関数
def hallcinated_transcription(t:str):
    hallcination_texts = ['ご視聴ありがとう', '最後まで視聴','最後までご視聴','視聴してくださって', '本日はご覧いただき', 'おやすみなさい']
    return any(phrase in t for phrase in hallcination_texts)

######## 録音のフラグ ########
if 'recording' not in st.session_state:
    st.session_state.recording = False

######## 録音停止ボタン ########
if st.button("停止", key="stop_button"):
    st.session_state.recording = False

######## 録音開始ボタン ########
if st.button("おしゃべり", key="start_button"):
    st.session_state.recording = True
    st.write("何か話しかけてください")

    chunk = 1024  # フレーム単位での音声の読み込みサイズ
    sample_format = pyaudio.paInt16  # 16ビットの音声
    channels = 1  # モノラル音声
    rate = 16000  # サンプリングレート
    record_seconds = 2

    stream = p.open(format=sample_format,
                    channels=channels,
                    rate=rate,
                    input=True,
                    frames_per_buffer=chunk)
    
    for i in range(5):

        data = stream.read(chunk, exception_on_overflow=False)

        frames = []
        for _ in range(0, int(rate / chunk * record_seconds)):
            data = stream.read(chunk)
            frames.append(data)

        # waveを使って、framesをwavファイルとして書き出す
        with wave.open(f'output{i}.wav', 'wb') as wf:
            wf.setnchannels(channels)
            wf.setsampwidth(p.get_sample_size(sample_format))
            wf.setframerate(rate)
            wf.writeframes(b''.join(frames))

        # openaiのtranscriptionsを使って音声をテキスト変換
        transcription = openai.audio.transcriptions.create(
            file=open(f'output{i}.wav', "rb"),
            model="whisper-1",
            language="ja"
        )
        
        print(f'---------{i}---------')
        print(transcription.text,f'。ハルシネーション:{hallcinated_transcription(transcription.text)}')

        if hallcinated_transcription(transcription.text) is False:
            st.write(transcription.text)


    # トークが終わったら録音ストリームを閉じる
    stream.stop_stream()
    stream.close()
    p.terminate()
