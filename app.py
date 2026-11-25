import streamlit as st

from langchain_core.messages import HumanMessage, AIMessage
from utils.chain import get_chat_chain


# Page Configuration
st.set_page_config(
    page_title="My AI Chatbot",
    page_icon="🤖"
)

# Initialize Chat Chain
chain = get_chat_chain()

st.title("🤖 My AI Chatbot")
st.write("Hello! Ask me anything.")


# Initialize Conversation Memory
if "messages" not in st.session_state:
    st.session_state.messages = []


# Display Previous Messages
for message in st.session_state.messages:

    if isinstance(message, HumanMessage):
        with st.chat_message("user"):
            st.write(message.content)

    elif isinstance(message, AIMessage):
        with st.chat_message("assistant"):
            st.write(message.content)


# User Input
user_input = st.chat_input("Type your message here...")

if user_input:

    with st.chat_message("user"):
        st.write(user_input)

    try:
        response = chain.invoke({
            "chat_history": st.session_state.messages,
            "user_input": user_input
        })

        with st.chat_message("assistant"):
            st.write(response.content)

        # Save Conversation History
        st.session_state.messages.append(
            HumanMessage(content=user_input)
        )

        st.session_state.messages.append(
            AIMessage(content=response.content)
        )

    except Exception as e:
        st.error("Sorry! Something went wrong.")

        with st.expander("See error details"):
            st.write(str(e))

        st.info("Please check your internet connection and try again.")