import streamlit as st
from streamlit_chat import message
import google.generativeai as palm

st.title('PaLM Tutorial')

if "messages" not in st.session_state:
    st.session_state["messages"]=[{"role":"assistant","content":"Say something to get started"}]

with st.form("chat",clear_on_submit=True):
    a,b=st.columns([4,1])

    user_input=a.text_input(
        label="Your Message",
        placeholder="Say Something!!",
        label_visibility="collapsed"
    )

    b.form_submit_button("Send",use_container_width=True)

for msg in st.session_state.messages:
    message(msg["content"],is_user=msg["role"]=="user")

palm_api_key="AIzaSyBxEkSQYiusBC351ddul0125So0IEhE_4E"
if user_input and palm_api_key:
    palm.configure(api_key=palm_api_key)
    st.session_state.messages.append({"role":"user","content":user_input})
    message(user_input,is_user=True)

    response=palm.chat(messages=[user_input])
    msg={"role":"assistant","content":response.last}
    st.session_state.messages.append(msg)
    message(msg["content"])
    

