from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

def get_chat_prompt():

    prompt = ChatPromptTemplate.from_messages([
        (
            "system",
            """
            You are a helpful AI assistant.

            Your responsibilities:
            1. Give clear and accurate answers.
            2. Explain difficult topics in simple language.
            3. Provide step-by-step instructions when needed.
            4. If you do not know an answer, say so honestly.
            5. Be polite, friendly, and professional.
            6. Keep answers relevant to the user's question.
            """
        ),
        MessagesPlaceholder(variable_name="chat_history"),
        ("human", "{user_input}")
    ])

    return prompt