import json
import re

class PromptEvaluator:
    """Lightweight evaluator for testing LLM prompt output formats and safety constraints."""
    
    def __init__(self, target_format="json"):
        self.target_format = target_format

    def is_valid_json(self, response_text: str) -> bool:
        """Checks if the LLM output is valid JSON."""
        try:
            json.loads(response_text)
            return True
        except ValueError:
            return False

    def count_tokens_approx(self, text: str) -> int:
        """Rough token estimation helper based on word count."""
        return int(len(re.findall(r'\w+', text)) * 1.3)

if __name__ == "__main__":
    evaluator = PromptEvaluator()
    sample_output = '{"status": "success", "tokens": 42}'
    print(f"Valid JSON: {evaluator.is_valid_json(sample_output)}")
    print(f"Approx Tokens: {evaluator.count_tokens_approx(sample_output)}")
