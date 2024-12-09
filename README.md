Demo video link: https://drive.google.com/file/d/1HZRLsgjYBSQ2-Rj9eVwYwmsxI2vDSyt3/view?usp=sharing

# Search Engine with AI Agents

This project is a **Streamlit-based application** that integrates AI tools to provide a conversational and intelligent search experience. It uses resources such as Arxiv, Wikipedia, and DuckDuckGo to answer user queries effectively.

---

## Features

### Conversational Interface
- A chatbot interface where users can type queries and receive detailed responses.

### AI-Powered Search
- Powered by LangChain's `ChatGroq` API and the Llama 3.1 model for robust and context-aware responses.

### Integrated Information Sources
- Retrieves data from:
  - **Arxiv** for academic papers.
  - **Wikipedia** for general knowledge.
  - **DuckDuckGo** for web searches.

### Real-Time Interaction
- Streaming responses showcase the AI's thought process and provide instant feedback.

### Robust Error Handling
- Handles errors gracefully to maintain app stability during user interactions.

### Session History
- Keeps track of user queries and responses for continuous and seamless interaction.

---

## Installation and Setup

### Prerequisites
- **Python Version**: 3.8 or later.
- **Required Libraries**: All dependencies are listed in the `requirements.txt` file.
- **Environment Variables**: A `.env` file containing your Groq API key (`groqkey`).

