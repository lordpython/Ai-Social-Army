from langchain_groq import ChatGroq
from langchain_anthropic import ChatAnthropic
from langchain_openai import ChatOpenAI

def initialize_llm(api, api_key, model, temp):
    try:
        if api == 'Groq':
            return ChatGroq(temperature=temp, api_key=api_key)
        elif api == 'OpenAI':
            return ChatOpenAI(temperature=temp, api_key=api_key, model=model)
        elif api == 'Anthropic':
            return ChatAnthropic(temperature=temp, anthropic_api_key=api_key, model_name=model)
    except Exception as e:
        print(f"Error initializing LLM: {str(e)}")
    return None