import streamlit as st
import pandas as pd
import numpy as np 

# 要用的資訊 id purp1 again recom nation age gender
df = pd.read_csv( "110.csv", encoding = "ISO-8859-1")
# :是代表要選幾個，要全選就是:
df_use = df.loc[:,["nation","purp1","age","gender","again"]]