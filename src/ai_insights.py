import os
from dotenv import load_dotenv
from google import genai



class AIInsights:
    DEFAULT_MODEL = "gemini-2.5-flash"

    SUMMARIZE_PROMPT = (
        "Given the following log statistics, provide a concise summary "
        "of the system's health and any potential issues. "
        "Response should be in English, 3-4 sentences. "
        "Use technical reasoning, propose potential fixes. "
        "No markdown, no preambles, no headers — straight to the point."
    )
    CATEGORIZE_PROMPT = (
        "Given the following log entries, categorize them into common themes or issues. "
        "Provide a list of categories with a brief description of each, and examples of log messages that fit each category. "
        "Response should be in English, concise, and structured for easy reading."
        "No markdown, no preambles, no headers — straight to the point."
        "Use technical reasoning, propose potential fixes. "
    )

    def __init__(self, api_key: str = None, model: str = None):
        load_dotenv()

        self.api_key = api_key or os.getenv('GEMINI_API_KEY')
        if not self.api_key:
            raise ValueError(
                "Brak GEMINI_API_KEY. Sprawdź plik .env lub przekaż api_key explicite."
            )

        self.model = model or self.DEFAULT_MODEL
        self.client = genai.Client(api_key=self.api_key)

    def _call_llm(self, prompt: str) -> str:
        response = self.client.models.generate_content(
            model=self.model,
            contents=prompt,
        )
        return response.text

    def _format_top(self, counter_dict: dict, n: int) -> str:
        if not counter_dict:
            return "(none)"
        items = sorted(counter_dict.items(), key=lambda x: -x[1])[:n]
        return ', '.join(f"{name} ({count})" for name, count in items)

    def _format_top_errors(self, top_errors: list) -> str:
        if not top_errors:
            return "  (none)"
        return '\n'.join(f"  * {msg} ({count}x)" for msg, count in top_errors)

    def summarize_logs(self, stats: dict) -> str:
        if not stats or stats.get('total', 0) == 0:
            return "No data available for analysis."

        data_section = self._build_data_section(stats)
        prompt = f"{self.SUMMARIZE_PROMPT}\n\nDATA:\n{data_section}"
        return self._call_llm(prompt)

    def _build_data_section(self, stats: dict) -> str:
        by_level = stats.get('by_level', {})
        errors_per_module = stats.get('errors_per_module', {})
        top_errors = stats.get('top_errors', [])

        return (
            f"Total logs: {stats.get('total', 0)}\n"
            f"Levels: INFO {by_level.get('INFO', 0)}, "
            f"WARN {by_level.get('WARN', 0)}, "
            f"ERROR {by_level.get('ERROR', 0)}\n"
            f"Top modules with errors: {self._format_top(errors_per_module, 3)}\n"
            f"Top error messages:\n{self._format_top_errors(top_errors)}"
        )
    def categorize_errors(self, stats: dict) -> str | None:
        if not stats or stats.get('total', 0) == 0:
            return None
        else:
            data_section = self._build_data_section(stats)
            prompt = f"{self.CATEGORIZE_PROMPT}\n\nDATA:\n{(data_section)}\n"
            return self._call_llm(prompt)