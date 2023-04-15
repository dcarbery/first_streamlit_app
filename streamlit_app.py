# import streamlit and pandas libraries
import streamlit
import pandas

sheet_url = "https://docs.google.com/spreadsheets/d/1tADOzIdSGwTCUXE0Uz3uNIRVrMqFk47nhwJLNGVr4Pg/edit?usp=sharing"
df = pd.DataFrame(sheet_url)
# build page of title, headers and text
streamlit.title("FOF Summer Tournament")


# write your own comment - what does this do?
streamlit.dataframe(df)
