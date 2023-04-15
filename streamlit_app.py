# import streamlit and pandas libraries
import streamlit as st
import pandas as pd


# Connect to the Google Sheet
sheet_id = "1tADOzIdSGwTCUXE0Uz3uNIRVrMqFk47nhwJLNGVr4Pg"
sheet_name = "results"
url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"
#df = pd.read_csv(url, dtype=str)
df = pd.read_csv(url)
df.index=['Match' + str(x) for x in range(1, 11)]

# build page of title, headers and text
st.title("FOF Summer Tournament")

# write your own comment - what does this do?
st.dataframe(df)
