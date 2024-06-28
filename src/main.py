import streamlit as st
from src.ui.configuration_tab import configuration_tab
from src.ui.execution_tab import execution_tab
from src.ui.results_tab import results_tab

def main():
    st.set_page_config(page_title="Yousef AI Army", page_icon="🤖", layout="wide")
    
    st.title('Yousef AI Army')
    st.markdown("This program is an army of AI robots at your disposal.")

    col1, col2 = st.columns([5, 1])
    with col2:
        st.image('logo.png')

    tab1, tab2, tab3 = st.tabs(["Configuration", "Execution", "Results"])

    with tab1:
        config_params = configuration_tab()

    with tab2:
        execution_tab(*config_params)

    with tab3:
        results_tab()

if __name__ == "__main__":
    main()