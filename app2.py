import streamlit as st
import time
import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_community.utilities import ArxivAPIWrapper, WikipediaAPIWrapper
from langchain_community.tools import ArxivQueryRun, WikipediaQueryRun, DuckDuckGoSearchRun
from langchain.agents import initialize_agent, AgentType
from langchain.callbacks import StreamingStdOutCallbackHandler

# Load environment variables
load_dotenv()
groqkey = os.getenv('groqkey')

# Initialize Arxiv and Wikipedia tools
arxiv_wrapper = ArxivAPIWrapper(top_k_results=1, doc_content_chars_max=200)
arxiv = ArxivQueryRun(api_wrapper=arxiv_wrapper)
wikipedia_wrapper = WikipediaAPIWrapper(top_k_results=1, doc_content_chars_max=200)
wiki = WikipediaQueryRun(api_wrapper=wikipedia_wrapper)

# Initialize DuckDuckGo Search tool
search = DuckDuckGoSearchRun(name="Search")

# Streamlit UI
st.title("LangChain - Chat With Search")
"""
In this example, we are using  'StreamlitCallbackHandler' to display the thoughts and actions of an agent in an interactive Streamlit app.
"""

# Sidebar for settings
st.sidebar.title("Settings")
api_key = groqkey

# Initialize session state for messages
if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role": "assistant", "content": "Hi, I'm a chatbot who can search the web. How can I help you?"}
    ]

# Display chat messages
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

# Handle user input
if prompt := st.chat_input(placeholder="What is Machine Learning?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)

    # Initialize LLM
    llm = ChatGroq(groq_api_key=api_key, model_name="llama-3.1-70b-versatile", temperature=0.8, streaming=True)
    tools = [search, arxiv, wiki]

    # Initialize agent with robust error handling
    search_agent = initialize_agent(
        tools,
        llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        handle_parsing_errors=True,
        verbose=True
    )

    # Respond to the user
    with st.chat_message("assistant"):
        try:
            st_cb = StreamingStdOutCallbackHandler()
            response = search_agent.run(st.session_state.messages, callbacks=[st_cb])
            st.session_state.messages.append({"role": "assistant", "content": response})
            st.write(response)
        except Exception as e:
            st.error(f"An error occurred: {e}")
            time.sleep(10)  # Optional retry delay
