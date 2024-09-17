from main import AI
import streamlit as st
import time

st.set_page_config(page_title="AI Project", page_icon="🤖", layout="centered")

st.markdown("""
    <style>
    .reportview-container {
        background-color: #f5f5f5;
        padding: 10px;
    }
    .header {
        text-align: center;
        padding-top: 20px;
    }
    .title {
        font-size: 32px;
        font-weight: bold;
    }
    textarea {
        font-size: 16px;
        height: 200px !important;
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown('<div class="header"><h1 class="title">AI Project</h1></div>', unsafe_allow_html=True)
st.write("Welcome! Enter a prompt below and get AI-generated responses. ")

prompt = st.text_area("Enter your prompt here:", height=150, placeholder="Type something for AI to generate...")
generate_button = st.button("Generate Response")

if generate_button:
    if prompt.strip() == "":
        st.warning("Please enter a prompt before generating a response.")
    else:
        with st.spinner("Generating response..."):
            response = AI(prompt)
        
        st.text_area("AI Output", value=response, height=800)
        st.success("Response generated successfully!")
        st.write("Thank you for using our AI service! 🎉")

