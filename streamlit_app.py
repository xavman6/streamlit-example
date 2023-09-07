import streamlit as st
import time

# Set up the page's title and header
st.title("Timer App")
st.header("Start and Stop A Timer")

# Initialize the time
time_elapsed = 0

# Create the UI
start_stop = st.button("Start/Stop Timer")
reset = st.button("Reset Timer")

# Define the actions
if start_stop:
    if start_stop.text == "Start Timer":
        start_stop.text = "Stop Timer"
        while start_stop.text == "Stop Timer":
            time_elapsed += 1
            st.write(f"Time Elapsed: {time_elapsed} seconds")
            time.sleep(1)
    else:
        start_stop.text = "Start Timer"

# Reset the timer
if reset:
    time_elapsed = 0
    st.write("Timer reset")
