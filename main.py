import numpy as np
import pandas as pd
import streamlit as st

from snowflake.snowpark.session import Session
session = Session.builder.configs(st.secrets.connections.snowflake).create()

st.header('クイズ大会')

# 回答のページと結果発表のページをtabで分けて用意
tab1, tab2 = st.tabs(['回答ページ', '結果発表'])

with tab1:

     answer = []
     st.subheader('参加者情報')
     answer.append(st.text_input('氏名', ''))

# 4択問題の回答箇所
     st.subheader('張り切っていってみよ〜✊')
     for iii in range(1,11):
          answer.append(st.selectbox(f'解答{iii}', ['1','2','3','4']))
                    
     renames = ['名前','解答1','解答2','解答3','解答4','解答5'
                 ,'解答6','解答7','解答8','解答9','解答10']
     df_answer = pd.DataFrame(answer, index=renames).T

# 既に用意している回答と結合して正解数を計算
     query = "select * from QUIZ.QUIZ_APP.ANSWER;"
     df_collect = session.sql(query).to_pandas()
     df = pd.merge(df_answer.T.reset_index().rename(columns={'index':'ID'})
                    , df_collect, on='ID')
     answer.append((df[0] == df.ANSWER).sum())     

# Snowflakeへデータを登録する用のクエリを作成
     query = f'''insert into QUIZ.QUIZ_APP.RESULT
          select \n
     '''
     for iii in range(len(answer)):
          if iii == 0:
               query = query + f"'{answer[iii]}'\n"
          else:
               query = query + f", '{answer[iii]}'\n"

# 回答の登録
     st.write('以下の解答で送信するよ')
     st.write(df_answer)

# st.buttonを利用してボタンを押したら回答が登録される仕組み
     st.write('問題なかったら、下記ボタンから解答を送信してね！')
     transfer = st.button('解答を送信する')

     if transfer:
          session.sql(query).collect()
          st.subheader(f'「{answer[0]}」さんの解答を受け付けました！')
          st.balloons()       


with tab2:
     st.subheader('🥁結果発表🥁')
# 結果・順位を取得
     query ='''select 
                    *, rank() over( order by collect_answer desc) as rank
               from 
                    QUIZ.QUIZ_APP.RESULT 
               order by 
                    collect_answer desc'''
     df_result =  session.sql(query).to_pandas()
     df_result.rename(columns={'NAME':'名前','COLLECT_ANSWER':'正解数', 'RANK':'順位'}, inplace=True)

# 結果発表
     open_under_4 = st.button(f'4位以下の順位は〜〜')
     if open_under_4:
          st.snow()
          st.write(df_result[df_result['順位'] >= 4].set_index('順位')[['名前', '正解数']])
     
     column1, column2, column3 = st.columns(3)
     with column1:
          open_top2 = st.button(f'2位の人は〜〜', key='No2')
          if open_top2:
               st.snow()
               df_2 = df_result[df_result['順位'] == 2].set_index('順位')[['名前', '正解数']]
               st.write(f'2位は')
               for iii in range(df_2.shape[0]):
                    st.write(f'##### {df_2.iloc[iii].名前} さん')
               st.write(f'でした🎉')
     
     with column2:
          open_top1 = st.button(f'1位の人は〜〜', key='No1')

     with column3:
          open_top3 = st.button(f'3位の人は〜〜', key='No3')
          if open_top2 == True:
               open_top3 = True
          if open_top3:
               st.snow()
               df_3 = df_result[df_result['順位'] == 3].set_index('順位')[['名前', '正解数']]
               st.write(f'3位は')
               for iii in range(df_3.shape[0]):
                    st.write(f'##### {df_3.iloc[iii].名前} さん')
               st.write(f'でした🎉')

     if open_top1:
          st.snow()
          df_1 = df_result[df_result['順位'] == 1].set_index('順位')[['名前', '正解数']]
          for iii in range(df_1.shape[0]):
               st.subheader(f'1位は　🎉　{df_1.iloc[iii].名前}　🎉　さんでした！')
          
     open_all_result = st.button(f'全員の順位は〜〜')
     if open_all_result:
          st.snow()
          st.write(df_result.set_index('順位')[['名前', '正解数']])
