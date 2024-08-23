import streamlit as st

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
tokuten = 0
# 最初のページ
def main():
    st.markdown(
        "<h1 style='text-align: center;'>💕💕Wedding Quiz💕💕</h1>",
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
        if st.session_state.answer1 == "何もprintされない":
            st.session_state.answers.append(st.session_state.answer1)
            st.session_state.page_id = "page2"
            tokuten + 1
        else:
            st.session_state.answers.append(st.session_state.answer1)
            st.session_state.page_id = "page2"

    with st.form("f1"):
        code = '''
            def hello():
                print("Hello")
        '''
        st.code(code, language="python")
        st.radio("上のコードを実行するとなんとprintされる？", ["Hello","hello", "何もprintされない"], key="answer1")
        st.form_submit_button("回答", on_click=change_page)


# 問題２
def page2():
    st.markdown(
        "<h1 style='text-align: center;'>第２問</h1>",
        unsafe_allow_html=True,
    )

    def change_page():
        if st.session_state.answer2 == "エラー":
            st.session_state.answers.append(st.session_state.answer2)
            st.session_state.page_id = "page3"
            tokuten + 1
        else:
            st.session_state.answers.append(st.session_state.answer2)
            st.session_state.page_id = "page3"

    with st.form("f2"):
        code = '''
            int1 = 100
            print("str" + int1) 
        '''
        st.code(code, language="python")
        
        st.radio("上のコードを実行するとどうなる", ["str100", "str 100", "エラー"], key="answer2")
        st.form_submit_button("回答", on_click=change_page)


# 問題３
def page3():
    st.markdown(
        "<h1 style='text-align: center;'>第３問</h1>",
        unsafe_allow_html=True,
    )

    def change_page():
        if st.session_state.answer3 == "エラー":
            st.session_state.answers.append(st.session_state.answer3)
            st.session_state.page_id = "page4"
            tokuten + 1
        else:
            st.session_state.answers.append(st.session_state.answer3)
            st.session_state.page_id = "page4"

    with st.form("f3"):
        code = '''
            number = "10"
            print("str" + " " + "number") 
        '''
        st.code(code, language="python")
        
        st.radio("上のコードを実行するとなんとなる", ["str number", "strnumber", "number + str", "エラー"], key="answer3")
        st.form_submit_button("回答", on_click=change_page)


# 問題４
def page4():
    st.markdown(
        "<h1 style='text-align: center;'>第４問</h1>",
        unsafe_allow_html=True,
    )

    def change_page():
        if st.session_state.answer4 == "エラー":
            st.session_state.answers.append(st.session_state.answer4)
            st.session_state.page_id = "page5"
            tokuten + 1
        else:
            st.session_state.answers.append(st.session_state.answer4)
            st.session_state.page_id = "page5"

    with st.form("f4"):
        code = '''
            int1 = 100
            print("str" + "int1") 
        '''
        st.code(code, language="python")
        st.radio("上のコードを実行すると何とprintされる？", ["str int1", "strint1", "str 100", "エラー"], key="answer4")
        st.form_submit_button("回答", on_click=change_page)


# 問題５
def page5():
    st.markdown(
        "<h1 style='text-align: center;'>第５問</h1>",
        unsafe_allow_html=True,
    )

    def change_page():
        if st.session_state.answer4 == "str  \n  int":
            st.session_state.answers.append(st.session_state.answer4)
            st.session_state.page_id = "page_end"
            tokuten + 1
        else:
            st.session_state.answers.append(st.session_state.answer4)
            st.session_state.page_id = "page_end"

    with st.form("f5"):
        code = """
            int = 100
            int += 100
            int = "str  \n  int"
            print(int)
        """
        st.radio("上のコードを実行すると何とprintされる？", ["str  \n  int", "str    int", "エラー", "表示されない"], key="answer5")
        st.form_submit_button("回答", on_click=change_page)


# 最終ページ
def page_end():

    username = st.text_input("名前を教えてください。")

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
    st.balloons()


# ページ遷移のための判定
if st.session_state.page_id == "main":
    main()

if st.session_state.page_id == "page1":
    page1()

if st.session_state.page_id == "page2":
    page2()

if st.session_state.page_id == "page3":
    page3()

if st.session_state.page_id == "page4":
    page4()

if st.session_state.page_id == "page5":
    page5()

if st.session_state.page_id == "page_end":
    page_end()


import database

db = database.Database()



def setdb():
  db.insert_chat_log(
    chat_id=1,
    username=username,
    name=name,
    message=tokuten,
    sent_time=datetime.datetime.now(),
  )
