import streamlit as st
import pandas as pd
st.title("Website Developing using Python")
st.header("Website Developing using Python")
st.subheader("	✨Suteekarn	✨")
st.image('images.jpg')

dt=pd.read_csv('./data/iris.csv')
st.subheader("ข้อมูลดอกไม้")
st.write(dt.head(10))

st.subheader("ข้อมูลดอกไม้")
