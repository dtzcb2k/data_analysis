import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.write("Hello World")
# 在要跑streamlit時要在terminal中輸入 streamlit run 檔案名稱
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
purpost = {"1":"觀光", "2":"業務",
"3":"國際會議或展覽", "4":"探親或訪友",
"5":"求學", "6":"醫療", "7":"其他(開放式)"}

# 替換 nation 列中的ID為相應的國家名稱
df_use['nation'] = df_use['nation'].astype(str).replace(nation_dict)

# st.write(df_use)

# 計算各個國家的人數
nation_counts = df_use['nation'].value_counts()

# 將數據轉換為 DataFrame，以便使用 st.bar_chart
# reset_index()重置 DataFrame 的索引，將原本的索引（即國家名稱）轉換成 DataFrame 的一列
nation_counts_df = pd.DataFrame(nation_counts).reset_index()
nation_counts_df.columns = ['Nation', 'Counts']

# 使用 st.bar_chart 顯示直方圖
st.bar_chart(nation_counts_df.set_index('Nation'))

# 計算各個旅遊目的的出現次數
# purp1_counts = df_use['purp1'].astype(str).replace(purpost).value_counts()

# # 將數據轉換為 DataFrame 以便顯示
# purp1_counts_df = pd.DataFrame(purp1_counts).reset_index()
# purp1_counts_df.columns = ['Purpose', 'Counts']

# # 使用 Matplotlib 繪製圓餅圖
# plt.figure(figsize=(10, 6))
# plt.pie(purp1_counts_df['Counts'], labels=purp1_counts_df['Purpose'], autopct='%1.1f%%', startangle=140)
# plt.title('Distribution of Travel Purposes')

# # 使用 st.pyplot 顯示圓餅圖
# st.pyplot(plt)


# 模擬數據
labels = ['trap', '業務', '國際會議或展覽', '探親或訪友', '求學', '醫療', '其他(開放式)']
sizes = [20, 15, 10, 25, 5, 15, 10]  # 模擬數據的百分比
explode = (0, 0.1, 0, 0, 0, 0, 0)  # 只爆炸第二塊（即 '業務'）

# 創建圖表
fig, ax = plt.subplots()
ax.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', startangle=90)
ax.axis('equal')  # 確保圓餅圖為正圓形

# 顯示圖表
st.pyplot(fig)

df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
    })

option = st.selectbox(
    'Which number do you like best?',
     df['first column'])

'You selected: ', option