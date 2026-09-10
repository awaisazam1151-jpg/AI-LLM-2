import streamlit as st
from google import genai
from google.genai import types

st.set_page_config(page_title="AI Mentor", page_icon="🧠")
st.title("🧠 My Personal AI Assistant")
st.write("Welcome! Ask me anything about technology, coding, or AI.")

# Safely retrieve the API key from Streamlit Secrets
api_key = st.secrets.get("GEMINI_API_KEY")

if not api_key:
    st.error("Setup Error: Please add your GEMINI_API_KEY to Streamlit Secrets.")
    st.stop()

# Initialize the Gemini Client
client = genai.Client(api_key=api_key)

# Get user input
user_question = st.text_input("What would you like to learn about today?")

if user_question:
    try:
        # Generate the response using Gemini 2.0 Flash
        response = client.models.generate_content(
            model="gemini-3.6-flash",
            contents=user_question,
            config=types.GenerateContentConfig(
                # This instruction shapes the AI's teaching style
                system_instruction=(
                    "You are an expert AI Educator and Mentor. Explain concepts from "
                    "absolute scratch using plain, accessible language and relatable "
                    "real-world analogies. Break down complex topics into digestible steps."
                )
            )
        )
        st.write(response.text)
    except Exception as e:
        st.error(f"An error occurred: {e}")
