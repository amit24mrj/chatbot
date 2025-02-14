# Q & A chatbot using streamlit and Gemini Generative AI
from dotenv import load_dotenv
import streamlit as st
import os 
import textwrap
import google.generativeai as genai
# from IPython.display import display, Markdown

# Load environment variables (e.g., API keys) from a .env
load_dotenv()
genai_api_key = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=genai_api_key)

# Function to interact with the Gemini Generative AI model and get a response
def get_gemini_response(question):
    try:
        model = genai.GenerativeModel('gemini-pro')
        response = model.generate_content(question)
        return response.text
    except Exception as e:
        return f"An error occurred: {e}"

# Initialize the streamlit app with a custom page title
with open("index.html","r") as file:
    html_content=file.read()
st.set_page_config(page_title="Question & Answer bot")
# Display the header for the applicatio
st.header("MY ChatBot App")
st.subheader("Ask your question and get the response")
user_input = st.text_input("Input", key="input")
submit = st.button("Ask the question")
if submit:
    response = get_gemini_response(user_input)
    st.subheader("The Response is")
    st.write(response)
