import streamlit as st  
from streamlit_qrcode_scanner import qrcode_scanner  
import sqlite3 

qrcodeButton = False

if qrcodeButton:
  qr_code = qrcode_scanner(key='qrcode_scanner')  

  if qr_code:  
    st.write(qr_code)

# SQLiteに接続する
conn = sqlite3.connect('/databse.db')
# テーブルを作成する conn.execute('''
 CREATE TABLE IF NOT EXISTS sleep_data ( 
　　　id INTEGER PRIMARY KEY, 
　　　date TEXT NOT NULL, 
　　　sleep_time TEXT NOT NULL, 
　　　wake_time TEXT NOT NULL５。 
) 
''')
