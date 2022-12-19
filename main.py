import streamlit as st
import pandas

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png", width=300)

with col2:
    st.title("Anthony Marshall")
    content = """
    Hi, I am Anthony! I'm an Embedded Systems developer. I graduated in 2012 with a BEng(Hons) in Electronic Engineering
    from the University of Central Lancashire.
    """
    st.info(content)

content2 = """Below you can find some of the apps I have built in Python."""
st.write(content2)

col3, col4 = st.columns(2)

df = pandas.read_csv("data.csv", sep=";")

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])