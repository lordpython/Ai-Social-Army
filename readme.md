# Social Ai Army

This program is an army of AI robots at your disposal, implemented using the CrewAI framework and Streamlit for the user interface.

## Description

Yousef AI Army is a flexible and powerful tool that allows you to create and manage a team of AI agents to perform various tasks. The system is built with a modular architecture, allowing for easy configuration and execution of AI-driven tasks.

## Features

- **Configurable AI Agents**: Define up to three AI agents with custom roles, backstories, and goals.
- **Multiple LLM Support**: Compatible with Groq, OpenAI, and Anthropic language models.
- **Interactive UI**: Built with Streamlit for easy configuration and execution.
- **Task Execution**: Execute tasks using the CrewAI framework with hierarchical process management.
- **Results Management**: View and download execution results in CSV format.
- **Logging**: Built-in logging for tracking execution progress and debugging.

## Installation

1. Clone the repository:

   ```
   git clone https://github.com/your-username/yousef-ai-army.git
   cd social-ai-army
   ```
2. Install the required dependencies:

   ```
   pip install -r requirements.txt
   ```

## Usage

1. Run the Streamlit app:

   ```
   streamlit run app.py
   ```
2. Open your web browser and navigate to the provided local URL (usually `http://localhost:8501`).
3. Use the Configuration tab to set up your AI agents, API keys, and model preferences.
4. Switch to the Execution tab to input task variables and start the AI process.
5. View the results and logs in the Results tab.

## Configuration

The `config.json` file stores your configuration settings. You can modify this file directly or use the UI to update the settings.

## Project Structure

- `app.py`: Main entry point for the Streamlit application.
- `src/`: Contains the core functionality of the project.
  - `agents/`: Agent-related modules.
  - `config/`: Configuration management.
  - `tasks/`: Task creation and management.
  - `ui/`: Streamlit UI components.
  - `utils/`: Utility functions and classes.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

[Specify your license here]

## Acknowledgements

- [CrewAI](https://github.com/joaomdmoura/crewAI)
- [Streamlit](https://streamlit.io/)
- [LangChain](https://github.com/hwchase17/langchain)
