import streamlit as st 
from datetime import timedelta

def add_time():
    intial = st.session_state["start_date"]
    days = int(st.session_state["days"].split(" ")[0])
    st.session_state["end_date"] = intial + timedelta(days=days)

def minus_time():
    intial = st.session_state["end_date"]
    days = int(st.session_state["days"].split(" ")[0])
    st.session_state["start_date"] = intial - timedelta(days=days)



 ####
 
st.radio(
    "Select Days",["7 days","10 days" , "15 days"],
    horizontal=True,
    index=0,
    key="days",
    on_change=add_time
    )

col1 , col2 = st.columns(2)
col1.date_input("Start Date",key="start_date",on_change=add_time)
col2.date_input("End Date",key="end_date",on_change=minus_time)


st.write(st.session_state)