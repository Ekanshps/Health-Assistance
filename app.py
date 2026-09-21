import streamlit as st
import os

# st.set_page_config(page_title="Health Assistance",
#               page_icon="💪",
#               layout="wide")

st.title("AI Health Assistance 💪")

st.write("Personal Health Assistance and Diet Reccomndation Agent")

st.header("Health Information")

st.sidebar.header("Your Information 🤷‍♀️")

gender=st.sidebar.selectbox("Gender",["Male","Female"])
weight=st.sidebar.number_input("Weight(Kg)",1,120)
height=st.sidebar.number_input("Height(cm)",100,200)

