import streamlit as st
import google.generativeai as genai

# Set your Gemini API key here
genai.configure(api_key="AIzaSyB47tMMs0HWuvzVttT0Zj7l4WNGH5ojaRg")  # Replace this with your actual key

# Page configuration
st.set_page_config(page_title="AI Message Rewriter", layout="centered")

# Title and UI
st.title("✉️ AI Message Rewriter")
st.markdown("Easily rewrite your messages with the tone you want using Gemini AI.")

# Text input from user
user_message = st.text_area("🔤 Enter your original message:", height=150)

# Tone options
tone = st.selectbox("🎭 Select tone:", ["Professional", "Casual", "Friendly", "Formal", "Polite", "Angry", "Apologetic"])

# When user clicks the rewrite button
if st.button("🔁 Rewrite Message"):
    if user_message.strip() == "":
        st.warning("Please enter a message first.")
    else:
        with st.spinner("Gemini AI is rewriting your message..."):
            try:
                prompt = f"""
You are an AI writing assistant. Rewrite the following message in a {tone.lower()} tone:

Original: "{user_message}"

Rewritten:"""

                model = genai.GenerativeModel(model_name="models/gemini-1.5-flash-latest")
                response = model.generate_content(prompt)
                rewritten = response.text.strip()

                st.subheader("📝 Rewritten Message")
                st.success(rewritten)
                st.code(rewritten, language="markdown")

            except Exception as e:
                st.error(f"❌ Error: {e}")
