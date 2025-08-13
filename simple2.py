import streamlit as st
st.title("サンプルアプリ：少し複雑なアプリ")

st.write("##### 動作モード1：文字数カウント")
st.write("入力されたテキストの文字数をカウントします。")
st.write("##### 動作モード2：BMI値の計算")
st.write("入力された身長と体重からBMI値を計算します。")

selected_item = st.radio(
    "動作モードを選択してください",
    ["文字数カウント", "BMI値の計算"]
)

st.divider()

if selected_item == "文字数カウント":
    input_message = st.text_input(label="文字数カウント対象となるテキストを入力してください。")
    text_count = len(input_message)

else:
    height =  st.text_input(label="身長を入力（cm）")
    weight = st.text_input(label="体重を入力（kg）")

if st.button("実行"):
    st.divider()

    if selected_item == "文字数カウント":
        if input_message:
            st.write(f"入力されたテキストの文字数は {text_count} 文字です。")

        else:
            st.write("テキストが入力されていません。")

    else:
        if height and weight:
            try:
                bmi = round(int(weight) / ((int(height) / 100) ** 2), 1)
                st.write(f"入力された身長 {height} cm と体重 {weight} kg のBMI値は {bmi} です。")
            except ValueError as e:
                st.error("身長と体重は数値で入力してください。")

        else:
            st.write("身長と体重の両方が入力されていません。")