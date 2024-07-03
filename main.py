import streamlit as st
import time
# ページのタイトル設定
st.set_page_config(
    page_title="Wedding Quiz",
)

# セッション情報の初期化
if "page_id" not in st.session_state:
    st.session_state.page_id = "main"
    st.session_state.answers = []

# 各種メニューの非表示設定
hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden; }
        footer {visibility: hidden;}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)

# 最初のページ
def main():
    st.markdown(
        "<h1 style='text-align: center;'>Quiz</h1>",
        unsafe_allow_html=True,
    )

    def change_page():
        st.session_state.answers.append(st.session_state.answer0)
        st.session_state.page_id = "page1"

    with st.form("f0"):
        st.radio("テーブル番号を選んでね", ["A", "B", "C", "D", "E", "F", "G"], key="answer0")
        st.form_submit_button("スタート！", on_click=change_page)


# 問題１
def page1():
    st.markdown(
        "<h1 style='text-align: center;'>第１問</h1>",
        unsafe_allow_html=True,
    )

    def change_page():
        if str(st.session_state.answer1) == "(1, 2, 3, 4, 1, 2, 3, 4)":
            st.session_state.answers.append(st.session_state.answer1 + "⭕️")
            st.balloons()
        else:
            st.session_state.answers.append(st.session_state.answer1 + "❌")
        
        st.session_state.page_id = "page2"

    with st.form("f1"):
        code = '''
            tuple1 = (1,2)
            tuple2 = (3,4)
            tuple3 = tuple1 + tuple2
            tuple3 = tuple3 * 2
            print(tuple3)'''
        st.code(code, language='python')
        st.radio("を実行するとprintされるのは何", [ "(1, 2, 3, 4)","(1, 2, 3, 4, 1, 2, 3, 4)", "(1234)","(2468)"], key="answer1")
        st.form_submit_button("回答", on_click=change_page)


# 問題２
def page2():
    st.markdown(
        "<h1 style='text-align: center;'>第２問</h1>",
        unsafe_allow_html=True,
    )

    def change_page():
        if st.session_state.answer2 == "30":
            st.session_state.answers.append(st.session_state.answer2 + "⭕️")
            st.balloons()
        else:
            st.session_state.answers.append(st.session_state.answer2 + "❌")
        st.session_state.page_id = "page3"

    with st.form("f2"):
        code = '''
            int1 = 10
            int2 = 20
            int3 = int1 + int2
            print(int3)'''
        st.code(code, language='python')
        
        st.radio("を実行するとprintされるのは何", ["1020", "30", "エラー"], key="answer2")
        st.form_submit_button("回答", on_click=change_page)


# 問題３
def page3():
    st.markdown(
        "<h1 style='text-align: center;'>第３問</h1>",
        unsafe_allow_html=True,
    )

    def change_page():
        if st.session_state.answer3 == "エラー":
            st.session_state.answers.append(st.session_state.answer3 + "⭕️")
            st.balloons()
        else:
            st.session_state.answers.append(st.session_state.answer3 + "❌")
        st.session_state.page_id = "page4"

    with st.form("f3"):
        code = '''
            str1 = "こんにちは"
            str2 = "hello"
            str2 = str1 + str2
            print(str3)'''
        st.code(code, language='python')
        st.radio("を実行するとprintされるのは何", ["こんにちはhello", "helloこんにちは", "hello", "こんにちは","エラー"], key="answer3")
        st.form_submit_button("回答", on_click=change_page)


# 問題４
def page4():
    st.markdown(
        "<h1 style='text-align: center;'>第４問</h1>",
        unsafe_allow_html=True,
    )

    def change_page():
        if st.session_state.answer4 == "[1, 2, 3, 4, 5, 'h', 'e', 'l', 'l', 'o']":
            st.session_state.answers.append(st.session_state.answer4 + "⭕️")
            st.balloons()
        else:
            st.session_state.answers.append(st.session_state.answer4 + "❌")
        st.session_state.page_id = "page5"

    with st.form("f4"):
        
        code = '''
            list1= [1,2,3,4,5]
            str2 = "hello"
            list1 += str2
            print(list1)'''
        st.code(code, language='python')
        st.radio("を実行するとprintされるのは何", ["[1, 2, 3, 4, 5, 'h', 'e', 'l', 'l', 'o']", "[1, 2, 3, 4, 5, 'hello']", "[ 'h', 'e', 'l', 'l', 'o', 1, 2, 3, 4, 5]", "エラー"], key="answer4")
        st.form_submit_button("回答", on_click=change_page)


# 問題５
def page5():
    st.markdown(
        "<h1 style='text-align: center;'>第５問</h1>",
        unsafe_allow_html=True,
    )

    def change_page():
        if st.session_state.answer5 == "エラー":
            st.session_state.answers.append(st.session_state.answer5 + "⭕️")
            st.balloons()
        else:
            st.session_state.answers.append(st.session_state.answer5 + "❌")
        st.session_state.page_id = "page_end"

    with st.form("f5"):
        code = '''
            list1 = [1,2,3,4,5]
            list2 = [1,2,3,4,5]
            str2 = "hello"
            list1 += str2 & list2
            print(list1)
        '''
        st.code(code, language='python')
        
        
        st.radio("を実行するとprintされるのは何", ["[1, 2, 3, 4, 5, 'hello']", "[1, 2, 3, 4, 5, 'h', 'e', 'l', 'l', 'o'", "エラー"], key="answer5")
        st.form_submit_button("回答", on_click=change_page)


# 最終ページ
def page_end():

    # 回答内容をサーバに送ったりなんなり

    st.markdown(
        "<h1 style='text-align: center;'>回答ありがとう🎉</h1>",
        unsafe_allow_html=True,
    )
    st.markdown("---")
    st.markdown(
        "<h2 style='text-align: center;'>あなたの回答</h2>",
        unsafe_allow_html=True,
    )
    st.markdown(
        f"<div style='text-align: center;'>テーブル：{st.session_state.answers[0]}</div>",
        unsafe_allow_html=True,
    )
    for num, value in enumerate(st.session_state.answers, 0):
        if num != 0:
            st.markdown(
                f"<div style='text-align: center;'>第{num}問：{value}</div>",
                unsafe_allow_html=True,
            )
    ## バルーンを飛ばす


# ページ遷移のための判定
if st.session_state.page_id == "main":
    main()

if st.session_state.page_id == "page1":
    page1()

if st.session_state.page_id == "page2":
    time.sleep(5)
    page2()

if st.session_state.page_id == "page3":
    time.sleep(5)
    page3()

if st.session_state.page_id == "page4":
    time.sleep(5)
    page4()

if st.session_state.page_id == "page5":
    time.sleep(5)
    page5()

if st.session_state.page_id == "page_end":
    time.sleep(5)
    page_end()
