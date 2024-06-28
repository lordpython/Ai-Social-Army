import re

class StreamToStreamlit:
    def __init__(self, expander):
        self.expander = expander
        self.buffer = []
        self.colors = ['red', 'green', 'blue', 'orange']
        self.color_index = 0
        self.agent_colors = {}

    def write(self, data):
        cleaned_data = self._clean_ansi_codes(data)
        self._process_task_info(cleaned_data)
        colored_data = self._apply_colors(cleaned_data)
        self._update_buffer(colored_data)

    def _clean_ansi_codes(self, data):
        return re.sub(r'\x1B\[[0-9;]*[mK]', '', data)

    def _process_task_info(self, cleaned_data):
        task_patterns = [
            r'\"task\"\s*:\s*\"(.*?)\"',
            r'task\s*:\s*([^\n]*)'
        ]
        for pattern in task_patterns:
            match = re.search(pattern, cleaned_data, re.IGNORECASE)
            if match:
                task_value = match.group(1).strip()
                self.expander.info(f":robot_face: {task_value}")
                break

    def _apply_colors(self, cleaned_data):
        color_phrases = {
            "Entering new CrewAgentExecutor chain": self._get_next_color,
            "Market Research Analyst": lambda: self._get_agent_color("Market Research Analyst"),
            "Business Development Consultant": lambda: self._get_agent_color("Business Development Consultant"),
            "Technology Expert": lambda: self._get_agent_color("Technology Expert"),
            "Finished chain.": self._get_current_color
        }

        for phrase, color_func in color_phrases.items():
            if phrase in cleaned_data:
                color = color_func()
                cleaned_data = cleaned_data.replace(phrase, f":{color}[{phrase}]")

        return cleaned_data

    def _get_next_color(self):
        self.color_index = (self.color_index + 1) % len(self.colors)
        return self.colors[self.color_index]

    def _get_current_color(self):
        return self.colors[self.color_index]

    def _get_agent_color(self, agent_name):
        if agent_name not in self.agent_colors:
            self.agent_colors[agent_name] = self._get_next_color()
        return self.agent_colors[agent_name]

    def _update_buffer(self, colored_data):
        self.buffer.append(colored_data)
        if "\n" in colored_data:
            self.expander.markdown(''.join(self.buffer), unsafe_allow_html=True)
            self.buffer = []