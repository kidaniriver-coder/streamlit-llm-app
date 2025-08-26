from dotenv import load_dotenv
load_dotenv()

import streamlit as st
from langchain_openai import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage

st.title("科目別講師アプリ")

st.write("##### 文理別回答")
st.write("受験勉強において、文系と理系の科目は異なるアプローチが必要です。このアプリでは、文系と理系の専門家がそれぞれの視点から質問に答えます。")

selected_item = st.radio(
    "質問したい分野を選択してください。",
    ["文系", "理系"]
)

st.divider()

input_message = st.text_input(label="質問したい内容を入力してください。")

if st.button("実行"):
    if input_message:  # 入力チェックを最初に行う
        st.divider()
        
        # LLMの初期化を一度だけ行う
        llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0)
        
        if selected_item == "文系":
            st.write("### 文系の専門家からの回答")
            messages = [
                SystemMessage(content="You are an excellent humanities teacher, specializing in subjects such as English, Japanese, and history."),
                HumanMessage(content=input_message),
            ]
            
        elif selected_item == "理系":
            st.write("### 理系の専門家からの回答")
            messages = [
                SystemMessage(content="You are an excellent science teacher, specializing in subjects such as mathematics, physics, chemistry, and biology."),
                HumanMessage(content=input_message),
            ]
        
        # 共通の処理でLLMを実行
        result = llm(messages)
        st.write(result.content)
        
    else: 
        st.error("質問のテキストを入力してから「実行」ボタンを押してください。")