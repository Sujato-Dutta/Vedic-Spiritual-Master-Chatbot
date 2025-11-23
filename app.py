import streamlit as st
from bot import get_rag_chain
import os

st.set_page_config(page_title="Vedic Spiritual Master", page_icon="🕉️")

st.title("🕉️ Vedic Spiritual Master")
st.subheader("Ancient Wisdom for Modern Life")

# Sidebar for setup
with st.sidebar:
    st.info("This bot uses RAG to retrieve wisdom from Yoga Vashishta, Gita, and Upanishads.")
    if not os.path.exists("chroma_db"):
        st.error("Database not found! Please run `ingest_data.py` first.")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
if prompt := st.chat_input("Seek guidance... (e.g., 'How do I handle anxiety?')"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate response
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        try:
            chain = get_rag_chain()
            with st.spinner("Consulting the ancient texts..."):
                response = chain.invoke({"query": prompt})
                result = response["result"]
                sources = response["source_documents"]
                
                # Format response
                full_response = result + "\n\n---\n*Sources:*\n"
                for doc in sources:
                    source_name = os.path.basename(doc.metadata.get("source", "Unknown"))
                    full_response += f"- {source_name}\n"
                
                message_placeholder.markdown(full_response)
                
                # Add assistant message to chat history
                st.session_state.messages.append({"role": "assistant", "content": full_response})
        except Exception as e:
            st.error(f"Error: {e}")
