# Prompt Template Library

A framework-agnostic, extensible library for managing prompt templates using Markdown files.

## Features
- Supports Zero-Shot, Few-Shot, Chain-of-Thought (CoT), Meta Prompting, and any future frameworks.
- Templates are organized by framework in folders.
- CLI and Web UI for listing, viewing, and rendering templates.
- No code changes needed to add new frameworks—just add a folder and Markdown files.

## Directory Structure
```
templates/
  zero_shot/
    classification.md
  few_shot/
    qa.md
  cot/
    math_reasoning.md
  meta/
    prompt_generator.md
  ... (add more frameworks here)
cli.py
web.py
template_loader.py
README.md
requirements.txt
```

## Adding a New Framework
1. Create a new folder in `templates/` with the framework name.
2. Add Markdown files for your templates in that folder.
3. The CLI and Web UI will automatically detect and use them.

## Usage
- Use the CLI to list, view, and render templates.
- Use the Web UI to browse, edit, and render templates interactively.

---

## Requirements
- Python 3.8+
- See `requirements.txt` for dependencies. 