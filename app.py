import streamlit as st
import google.generativeai as genai

# Configure API Key
genai.configure(api_key="AIzaSyA0gFVSeBYBoexZs3BWZNvyiTTU0e8UcDg")

# System Prompt
sys_prompt = """You are a helpful data science tutor. You can only resolve data science-related queries. 
If someone asks unrelated queries, politely ask them to stay on topic."""

# Load Model
model = genai.GenerativeModel(model_name='gemini-1.5-flash', system_instruction=sys_prompt)

# Streamlit UI
st.title("🤖 Data Science Tutor (AI)")
st.write("Ask me any data science-related question!")

# User Input
user_prompt = st.text_input("Enter your query:")

# Generate and Display Response
if st.button("Generate Response") and user_prompt:
    response = model.generate_content(user_prompt)
    st.markdown(response.text)
