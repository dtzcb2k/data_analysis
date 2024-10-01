import streamlit as st
# 在要跑streamlit時要在terminal中輸入streamlit run 檔案名稱

import pandas as pd
import numpy as np 
# 將東西輸出到網頁上
st.write("Hello World")
# 在要跑streamlit時要在terminal中輸入streamlit run 檔案名稱
# 會跳到網頁上
# 不過由於streamlit是安裝在vnev中所以要先開起虛擬環境才能執行
# 開啟虛擬環境 輸入 activate 關閉 deactivate
# 停止streamlit用 ctrl+c 就可以了

df = pd.DataFrame({ 'first column': [1, 2, 3, 4], 
'second column': [10, 20, 30, 40] }) 
st.write(df)
# st的內建資料框
dataframe = np.random.randn(10, 20) 
# 差別在於有沒有y軸的id
st.dataframe(dataframe)#沒有
st.table(dataframe)#有
# DATA_URL = ('https://raw.githubusercontent.com/wtlee/dataanalysis/main/data/winequalityN.csv ') 
chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
st.scatter_chart(chart_data)


st.text_input("Your name", key="name") 
# You can access the value at any point with:
st.session_state.name
# session 是在wed上的一個臨時儲存端，只要server沒關就會存在