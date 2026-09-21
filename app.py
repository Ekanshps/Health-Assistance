import streamlit as st
import os
from diet import bmi_calculator, bmr_calculator, tdee_calculator, calorie_target


# st.set_page_config(page_title="Health Assistance",
#               page_icon="💪",
#               layout="wide")

st.title("AI Health Assistance 💪")

st.write("Personal Health Assistance and Diet Reccomndation Agent")

st.header("Health Information")

st.sidebar.header("Your Information 🤷‍♀️")

##-------------------------------Controls Sidebar------------------------------------##

gender=st.sidebar.selectbox("Gender",["MALE","FEMALE"])
weight=st.sidebar.number_input("Weight(Kg)",1,120)
height=st.sidebar.number_input("Height(cm)",100,200)
activity=st.sidebar.selectbox("Activity",[ "Sedentary","Modrately Active","Very Active","Extra Active"])
aim=st.sidebar.selectbox("Aim",["weight maintain","weight loss","weight gain"])
age=st.sidebar.number_input("Age",1,100)

##---------------------------Calculation Starts Here ----------------------------##


bmi=bmi_calculator(weight,height)

bmr=bmr_calculator(gender,age,weight,height)

tdee=tdee_calculator(bmr,activity)

calories=calorie_target(tdee,aim)

##---------------------------------------------------------##

col1,col2,col3,col4=st.columns(4)

col1.metric("BMI",bmi)
col2.metric("BMR",f"{bmr} Kacl")
col3.metric("TDEE",f"{tdee} Kacl")
col4.metric("CALORIE TARGET",f"{calories} Kacl")