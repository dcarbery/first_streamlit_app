# import streamlit and pandas libraries
import streamlit as st
import pandas as pd

"1tADOzIdSGwTCUXE0Uz3uNIRVrMqFk47nhwJLNGVr4Pg"

url = f"https://docs.google.com/spreadsheets/d/{"1tADOzIdSGwTCUXE0Uz3uNIRVrMqFk47nhwJLNGVr4Pg"}/gviz/tq?tqx=out:csv&sheet={"results"}"
df = pd.read_csv(url)

# build page of title, headers and text
st.title("FOF Summer Tournament")


# write your own comment - what does this do?
st.dataframe(df)
