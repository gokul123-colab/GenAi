import streamlit as st
st.set_page_config(page_icon="😘",page_title="nani",layout="wide")

st.title("satya gokul ram",anchor=False) 

st.subheader("Gen AI Developer | Gamer")
with st.container(border=True):
    st.info("I am..................")

col1,col2,col3=st.columns(3)

with col1:
    with st.expander(label="know me",expanded=False):
        st.image("th.jpeg",width=420)
        st.info("hey...........")
with col2:
    with st.expander(label="risk",expanded=False):
        
        st.info("0yy...........")
with col3:
    with st.expander(label="mine",expanded=True):
        st.info("Hm............")
