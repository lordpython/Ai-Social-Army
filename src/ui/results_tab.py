import streamlit as st
import pandas as pd

def results_tab():
    st.header("Results")
    
    try:
        results_df = pd.read_csv('results.csv')
        st.write("Here are the latest results from your CrewAI executions:")
        st.dataframe(results_df)
        
        if st.button("Download Results CSV"):
            csv = results_df.to_csv(index=False)
            st.download_button(
                label="Click here to download",
                data=csv,
                file_name="crewai_results.csv",
                mime="text/csv",
            )
    except FileNotFoundError:
        st.info("No results found. Run an execution to generate results.")
    
    st.subheader("Log Output")
    try:
        with open("app.log", "r") as log_file:
            st.code(log_file.read())
    except FileNotFoundError:
        st.info("No log file found. Run an execution to generate a log.")