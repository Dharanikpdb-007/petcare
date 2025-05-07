import streamlit as st
from chatbot import DogCareBot


bot = DogCareBot()


st.set_page_config(
    page_title="Dog Pet Care Assistant",
    page_icon="🐕",
    layout="wide"
)


st.markdown("""
    <style>
    .stApp {
        max-width: 800px;
        margin: 0 auto;
    }
    </style>
""", unsafe_allow_html=True)


st.title("🐕 Dog Pet Care Assistant")
st.markdown("Your friendly assistant for all dog care questions and advice!")


if 'messages' not in st.session_state:
    st.session_state.messages = []


for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


if prompt := st.chat_input("Ask me about dog care..."):
  
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    
    response = bot.process_query(prompt)

  
    st.session_state.messages.append({"role": "assistant", "content": response})
    with st.chat_message("assistant"):
        st.markdown(response)

with st.sidebar:
    st.header("Available Commands")
    st.markdown("""
    - Type 'categories' to see all topics
    - Type 'help' for usage instructions
    - Ask about specific breeds
    - Ask about feeding, training, health, or grooming
    """)

    st.header("Example Questions")
    st.markdown("""
    - "How often should I feed my dog?"
    - "What's the best way to train a puppy?"
    - "Tell me about Labrador breed"
    - "How do I groom my dog properly?"
    """)
