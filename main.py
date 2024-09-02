import streamlit as st  
from streamlit_qrcode_scanner import qrcode_scanner  
import sqlite3 

qrcodeButton = False

if qrcodeButton:
  qr_code = qrcode_scanner(key='qrcode_scanner')  

  if qr_code:  
    st.write(qr_code)

# SQLiteに接続する
conn = sqlite3.connect('resource/database.db')
# テーブルを作成する 
conn.execute('''
  CREATE TABLE IF NOT EXISTS Point ( 
    id INTEGER PRIMARY KEY, 
    point TEXT NOT NULL, 
) 
''')
