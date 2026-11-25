# LangChain-Based AI Chatbot

## Project Overview
This project is an AI-powered conversational chatbot built using Python, LangChain, Google Gemini API, and Streamlit.

The chatbot can answer user questions, maintain conversation history during a session, and provide clear and simple responses.

## Technologies Used
- Python
- LangChain
- Google Gemini API (Gemini 2.5 Flash)
- Streamlit
- Python-dotenv

## Project Structure

```text
LangChain-Based Chatbot/
│
├── app.py
├── .env
├── .gitignore
├── README.md
│
└── utils/
    ├── __init__.py
    ├── llm.py
    ├── prompt.py
    └── chain.py
```

## Architecture

1. **app.py:** Handles the Streamlit user interface and conversation history.
2. **llm.py:** Loads the Gemini API key from environment variables and initializes the language model.
3. **prompt.py:** Defines the system prompt and conversation message structure.
4. **chain.py:** Connects the prompt and language model using LangChain.

## Setup Instructions

### 1. Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_LINK
```

### 2. Navigate to the Project Folder

```bash
cd LangChain-Based-Chatbot
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

### 4. Activate the Virtual Environment

Windows:

```bash
venv\Scripts\activate
```

### 5. Install Dependencies

```bash
pip install streamlit langchain langchain-google-genai python-dotenv
```

### 6. Configure API Key

Create a `.env` file in the project root directory.

Add your Gemini API key:

```env
GOOGLE_API_KEY=your_gemini_api_key
```

Do not share or upload your API key publicly.

### 7. Run the Application

```bash
streamlit run app.py
```

## Features

- Google Gemini LLM integration.
- LangChain prompt templates and chains.
- Multi-turn conversations.
- Conversation history using Streamlit session state.
- Environment-based API key configuration.
- Basic error handling.
- Modular Python code structure.

## Sample Chatbot Interaction

**User:** Hello!

**Assistant:** Hello! How can I help you today?

**User:** Explain Artificial Intelligence in simple words.

**Assistant:** Artificial Intelligence is a technology that enables machines to perform tasks that normally require human intelligence.

## Design Decisions

- Used LangChain to organize prompts and connect the language model.
- Used Google Gemini 2.5 Flash as the LLM.
- Used Streamlit to create a simple interactive interface.
- Stored API credentials in a `.env` file for security.
- Divided the application into separate modules for better readability and maintainability.
- Used session-based conversation history to support multi-turn conversations.

## Future Improvements

- Persistent conversation storage.
- Chat export functionality.
- Support for additional language models.

## Author

Gouri Chinchkar   (AI/ML Fresher)