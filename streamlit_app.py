# Create the Streamlit App

import streamlit as st 
import time

# Set the title and header 
st.title("Timer App")
st.header("Start and Stop Timer")

# Placeholder for timer
timer_placeholder = st.empty()

# Create the Start/Stop toggle
start_stop = st.button("Start Timer")

# Create the timer 
if start_stop:
    timer = 0 
    while True:
        timer += 1
        timer_placeholder.write(timer)
        time.sleep(1)
        if st.button("Stop Timer"):
            timer_placeholder.write("Timer stopped")
            break

