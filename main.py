import random

roles = ['村人', '村人', '人狼', '占い師', '狩人']

def assign_roles(players):
    random.shuffle(roles)
    assigned_roles = {player: role for player, role in zip(players, roles)}
    return assigned_roles

def night_phase(roles):
    # 人狼がプレイヤーを襲撃
    wolves = [player for player, role in roles.items() if role == '人狼']
    victim = random.choice(list(roles.keys()))
    return f"夜のフェーズ: 人狼が{victim}を襲撃しました！"

def day_phase(roles):
    # プレイヤー同士の議論フェーズ
    return "昼のフェーズ: プレイヤー同士で議論してください。"

import streamlit as st

st.title("オンライン人狼ゲーム")

# プレイヤー名の入力
players = st.text_input("プレイヤー名（カンマ区切り）")

if st.button("ゲームを開始"):
    player_list = players.split(',')
    roles = assign_roles(player_list)

    st.write("プレイヤーに役職が割り当てられました。")

    if st.button("夜のフェーズ"):
        st.write(night_phase(roles))
        
    if st.button("昼のフェーズ"):
        st.write(day_phase(roles))
