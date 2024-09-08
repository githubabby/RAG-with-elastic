import streamlit as st
import time

def return_output():
    x = "this is the output"
    for c in x:
        time.sleep(0.05)
        yield c
st.title('RAG-with-elastic')
with st.chat_message("rohit"):
    st.write("yahoo!!")
with st.chat_message("bot"):
    st.write("goo!")
question = st.chat_input('type your question here')
if question:
    st.write_stream(return_output())