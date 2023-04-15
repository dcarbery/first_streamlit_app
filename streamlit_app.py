# import streamlit and pandas libraries
import streamlit as st
import pandas as pd


# Connect to the Google Sheet
sheet_id = "1tADOzIdSGwTCUXE0Uz3uNIRVrMqFk47nhwJLNGVr4Pg"
#sheet_name = "results"
url = r"https://docs.google.com/spreadsheets/d/" + sheet_id"
df = pd.read_csv(url)

# build page of title, headers and text
st.title("FOF Summer Tournament")


# write your own comment - what does this do?
st.dataframe(df)
