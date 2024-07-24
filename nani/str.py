import streamlit as st
st.title("sum of integers in a string")
a=st.text_input(label="enter a string")
if st.button("submit"):
    try:
        s=0
        for i in a:
            if i.isnumeric():
                s+=int(i)
        if s==0:
            st.write("no number")
        else:
            st.write(s)
    except ValueError:
        st.write("error")
    
