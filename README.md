# Prompt Eval Kit

A lightweight Python library designed to test, evaluate, and validate structured LLM prompt outputs for developer applications.

## Features
- **JSON Validation:** Easily verify whether LLM outputs match expected JSON formats.
- **Token Estimation:** Approximate token counts for prompt budgeting.

## Installation
Clone the repository and integrate it directly into your project workflows.

```bash
git clone https://github.com/zouhairharmouzi-u/prompt-eval-kit.git
## Quickstart
```python
from evaluator import PromptEvaluator

evaluator = PromptEvaluator()
is_valid = evaluator.is_valid_json('{"result": "ok"}')
print(is_valid)
```
