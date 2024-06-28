import streamlit as st
from src.config.config_manager import update_config, get_config

def dynamic_input(label, key, input_type='text', options=None, help=None):
    value = get_config(key, '')
    
    if input_type == 'text':
        new_value = st.text_input(label, value=value, key=f"{key}_input", help=help)
    elif input_type == 'textarea':
        new_value = st.text_area(label, value=value, key=f"{key}_area", help=help)
    elif input_type == 'selectbox':
        new_value = st.selectbox(label, options or [], index=options.index(value) if value in options else 0, key=f"{key}_select", help=help)
    else:
        raise ValueError(f"Unsupported input type: {input_type}")
    
    if new_value != value:
        update_config(key, new_value)
    
    return new_value

def configuration_tab():
    st.header("Configuration")
    
    api_options = ['Groq', 'OpenAI', 'Anthropic']
    api = dynamic_input('Choose an API', 'api', input_type='selectbox', options=api_options)
    api_key = dynamic_input('Enter API Key', 'api_key')
    temp = st.slider("Model Temperature", min_value=0.0, max_value=1.0, value=get_config('temp', 0.7), step=0.1, key='temp_slider')
    update_config('temp', temp)

    model_options = {
        'Groq': ['llama3-70b-8192', 'mixtral-8x7b-32768', 'gemma-7b-it'],
        'OpenAI': ['gpt-4-turbo', 'gpt-4-1106-preview', 'gpt-3.5-turbo-0125', 'gpt-4'],
        'Anthropic': ['claude-3-5-sonnet-20240620', 'claude-3-opus-20240229', 'claude-3-haiku-20240307']
    }

    model = dynamic_input('Choose a model', 'model', input_type='selectbox', options=model_options.get(api, []))

    with st.expander("Agent Definitions", expanded=False):
        agent_1_role = dynamic_input("Agent 1 Role", "agent_1_role")
        agent_1_backstory = dynamic_input("Agent 1 Backstory", "agent_1_backstory", input_type='textarea')
        agent_1_goal = dynamic_input("Agent 1 Goal", "agent_1_goal", input_type='textarea')
        
        agent_2_role = dynamic_input("Agent 2 Role", "agent_2_role")
        agent_2_backstory = dynamic_input("Agent 2 Backstory", "agent_2_backstory", input_type='textarea')
        agent_2_goal = dynamic_input("Agent 2 Goal", "agent_2_goal", input_type='textarea')
        
        agent_3_role = dynamic_input("Agent 3 Role", "agent_3_role")
        agent_3_backstory = dynamic_input("Agent 3 Backstory", "agent_3_backstory", input_type='textarea')
        agent_3_goal = dynamic_input("Agent 3 Goal", "agent_3_goal", input_type='textarea')

    return api, api_key, temp, model, agent_1_role, agent_1_backstory, agent_1_goal, agent_2_role, agent_2_backstory, agent_2_goal, agent_3_role, agent_3_backstory, agent_3_goal