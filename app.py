import streamlit as st
import time
from PIL import Image
import os

# Page configuration
st.set_page_config(page_title="Assistant Inpulse", layout="centered")

# App title
st.title("Assistant Inpulse")

st.caption("Comment puis-je vous aider aujourd'hui ?")

# Load custom avatars
# Assistant avatar from URL
assistant_avatar = "https://cdn-images.welcometothejungle.com/Qojwbnsrxfd-OEm0RvtfMfuTwohSeNkum_0y7wJQyyA/rs:auto:400::/q:85/czM6Ly93dHRqLXByb2R1Y3Rpb24vdXBsb2Fkcy9vcmdhbml6YXRpb24vbG9nby8zMjE5LzE1MDc2NS8zOGNmNjA3NS0zNGM4LTRmODMtYjljNS0yNWFiZDlkOGY5NDgucG5n"

# User avatar from local file
# Create a directory named 'images' in your project and place user_avatar.png in it
current_dir = os.path.dirname(os.path.abspath(__file__))
user_avatar_path = os.path.join(current_dir, "images", "user_icon.png")

# Check if the file exists
if os.path.exists(user_avatar_path):
    user_avatar = Image.open(user_avatar_path)
else:
    # Fallback to a default avatar or None if file doesn't exist
    user_avatar = None
    st.warning("User avatar image not found. Please place 'user_icon.png' in the 'images' directory.")

# Initialize message history
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "Bonjour ! Comment puis-je vous aider aujourd'hui ?"}]

# Display chat messages from history
for message in st.session_state.messages:
    if message["role"] == "assistant":
        with st.chat_message(message["role"], avatar=assistant_avatar):
            st.markdown(message["content"])
    else:
        with st.chat_message(message["role"], avatar=user_avatar):
            st.markdown(message["content"])

# User input area
if prompt := st.chat_input("Votre message..."):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Display user message
    with st.chat_message("user", avatar=user_avatar):
        st.markdown(prompt)
    
    # Display assistant response with animation
    with st.chat_message("assistant", avatar=assistant_avatar):
        message_placeholder = st.empty()
        
        # Simulate response time
        with st.spinner("..."):
            time.sleep(1)  # 1 second delay
        
        # Hardcoded response
        bot_response = "Bonjour ! Ceci est une réponse automatique."
        
        # Character by character animation
        full_response = ""
        for char in bot_response:
            full_response += char
            time.sleep(0.02)  # Delay between characters
            message_placeholder.markdown(full_response + "▌")  # Blinking cursor
        
        # Final response display
        message_placeholder.markdown(full_response)
    
    # Add bot response to chat history
    st.session_state.messages.append({"role": "assistant", "content": bot_response})
