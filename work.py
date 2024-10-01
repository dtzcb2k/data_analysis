import streamlit as st
import pandas as pd

st.write("Hello World")
# 在要跑streamlit時要在terminal中輸入streamlit run 檔案名稱
# 要用的資訊 id purp1 again recom nation age gender
df = pd.read_csv("110.csv", encoding="ISO-8859-1")
# :是代表要選幾個，要全選就是:
df_use = df.loc[:, ["nation", "purp1", "age", "gender", "again"]]

# 定義 nation 的對應表
nation_dict = {
    "1": "日本", "2": "中國大陸", "3": "韓國",
    "50": "新加坡", "51": "馬來西亞", "52": "印尼",
    "53": "菲律濱", "54": "泰國", "55": "越南", "59": "印度",
    "60": "美國", "71": "德.英.法", "72": "歐洲其他地區",
    "80": "紐澳", "88": "中華民國", "90": "其他地區"
}

# 替換 nation 列中的ID為相應的國家名稱
df_use['nation'] = df_use['nation'].astype(str).replace(nation_dict)

st.write(df_use)

# 計算各個國家的人數
nation_counts = df_use['nation'].value_counts()

# 將數據轉換為 DataFrame，以便使用 st.bar_chart
nation_counts_df = pd.DataFrame(nation_counts).reset_index()
nation_counts_df.columns = ['Nation', 'Counts']

# 使用 st.bar_chart 顯示直方圖
st.bar_chart(nation_counts_df.set_index('Nation'))
