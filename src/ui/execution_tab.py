import streamlit as st
from src.agents.agent_factory import create_agent
from src.tasks.task_factory import create_task
from src.utils.llm_initializer import initialize_llm
from src.utils.stream_to_streamlit import StreamToStreamlit
from crewai import Crew, Process
import sys
import logging
from datetime import datetime
import pandas as pd

def execution_tab(api, api_key, temp, model, agent_1_role, agent_1_backstory, agent_1_goal, agent_2_role, agent_2_backstory, agent_2_goal, agent_3_role, agent_3_backstory, agent_3_goal):
    st.header("Execution")
    
    var_1 = st.text_input("Variable 1:", key="var_1", help="Enter the first variable for the task")
    var_2 = st.text_input("Variable 2:", key="var_2", help="Enter the second variable for the task")
    var_3 = st.text_input("Variable 3:", key="var_3", help="Enter the third variable for the task")

    if st.button("Start Execution", disabled=not (api_key and any([var_1, var_2, var_3]))):
        with st.spinner("Generating..."):
            try:
                llm = initialize_llm(api, api_key, model, temp)
                if not llm:
                    st.warning("Failed to initialize LLM. Please check your API key and selected model.")
                    return

                agents = []
                tasks = []

                for i, (role, backstory, goal) in enumerate([(agent_1_role, agent_1_backstory, agent_1_goal),
                                                             (agent_2_role, agent_2_backstory, agent_2_goal),
                                                             (agent_3_role, agent_3_backstory, agent_3_goal)], 1):
                    if role and backstory and goal:
                        agent = create_agent(role, backstory, goal, llm)
                        agents.append(agent)
                        task = create_task(
                            description=f"Task for Agent {i}:\n---\nVARIABLE 1: {var_1}\nVARIABLE 2: {var_2}\nVARIABLE 3: {var_3}",
                            expected_output="A detailed output based on the agent's role and given variables.",
                            agent=agent,
                            context=tasks if tasks else None
                        )
                        tasks.append(task)

                if not agents or not tasks:
                    st.warning("No valid agents or tasks created. Please check your agent configurations.")
                    return

                crew = Crew(
                    agents=agents,
                    tasks=tasks,
                    verbose=2,
                    process=Process.hierarchical,
                    manager_llm=llm
                )

                output_expander = st.expander("Output", expanded=True)
                original_stdout = sys.stdout
                sys.stdout = StreamToStreamlit(output_expander)
                
                result = ""
                result_container = output_expander.empty()
                for delta in crew.kickoff():
                    result += delta
                    result_container.markdown(result)
                
                # Save results to a CSV file
                results_df = pd.DataFrame({
                    'Timestamp': [datetime.now()],
                    'API': [api],
                    'Model': [model],
                    'Temperature': [temp],
                    'Variable 1': [var_1],
                    'Variable 2': [var_2],
                    'Variable 3': [var_3],
                    'Result': [result]
                })
                results_df.to_csv('results.csv', mode='a', header=not pd.io.common.file_exists('results.csv'), index=False)
                
                logging.info("CrewAI process completed successfully")
                st.success("Process completed successfully!")

            except Exception as e:
                logging.error(f"An error occurred during execution: {str(e)}")
                st.error(f"An error occurred during execution: {str(e)}")
            finally:
                sys.stdout = original_stdout