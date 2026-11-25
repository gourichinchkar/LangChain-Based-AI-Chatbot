from utils.llm import get_llm
from utils.prompt import get_chat_prompt

def get_chat_chain():

    llm = get_llm()
    prompt = get_chat_prompt()

    chain = prompt | llm

    return chain
