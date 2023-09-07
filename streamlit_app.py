# Create the Streamlit App

import streamlit as st 

# Set the title and header 
st.title("Timer App")
st.header("Start and Stop Timer")

# Create the Start/Stop toggle
start_stop = st.button("Start Timer")

# Create the timer 
if start_stop.text == "Start Timer":
    timer = 0 
    while start_stop.text != "Stop Timer":
        timer += 1
        st.write(timer)
    else:
        st.write("Timer stopped")
        st.button("Start Timer")
