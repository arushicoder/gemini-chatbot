import streamlit as st
import os
from dotenv import load_dotenv
from google import genai

# Load API key
load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

st.title("🤖 Study Buddy AI")

question = st.text_input("Ask me anything")

if st.button("Send"):

    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=question,
    )

    st.write(response.text)