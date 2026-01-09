# my_agent Crew

MyAgent Crew (repository: https://github.com/rajeesing/my_agent) is a lightweight, ready-to-use template for building multi-agent AI systems using the popular open-source crewAI framework.
crewAI is a Python-based framework (from crewAIInc) that allows you to create teams ("crews") of specialized, role-playing AI agents powered by large language models (like OpenAI's GPT models). These agents can collaborate autonomously—delegating tasks, communicating, and working together—to solve complex problems more effectively than a single AI prompt ever could. It's great for tasks like research, content generation, automation, data analysis, or custom workflows.
Your project simplifies getting started with crewAI by providing a clean, modular scaffold where most of the configuration is done via easy-to-edit YAML files, reducing boilerplate code.

## Key Features

- Config-driven design: Define agents and tasks in YAML—no need to hardcode everything in Python.
- Multi-agent collaboration: Agents have roles, goals, backstories, and tools; they work sequentially or collaboratively.
- Customizable entry points: Add your own logic, tools, or inputs easily.
- Simple output: By default, it generates a Markdown report (e.g., report.md) based on agent research/work.
- Modern tooling: Uses uv for fast, reliable dependency management.

## Project Structure
Here's a quick overview of the main files and directories:

- src/my_agent/
  - config/
    - agents.yaml: Defines your agents (role, goal, backstory, allowed tools, etc.).
    - tasks.yaml: Outlines the tasks, which agent handles them, and expected outputs.

  - crew.py: Core logic where the "crew" is assembled—agents are loaded, tasks assigned, and custom tools integrated.
  - main.py: Entry point for providing custom inputs or arguments when running the crew.

- knowledge/: (Empty by default—likely for adding documents or data for RAG/retrieval if needed.)
- pyproject.toml: Project metadata and dependencies.
- .env: For storing secrets like your **OPENAI_API_KEY**.
- report.md: Example output file generated after a run.

## How to Set It Up and Run

1. Requirements: Python 3.10 to 3.13.
1. Install uv (if you don't have it): pip install uv.
1. Clone the repo and navigate into it.
1. Install dependencies: Run crewai install (this uses uv under the hood for speed).
1. Add your API key: Create a .env file with OPENAI_API_KEY=your_key_here.
1. Customize:
   - Edit agents.yaml and tasks.yaml for your use case.
   - Add custom tools or logic in crew.py.
   - Provide inputs in main.py if needed.

1. Run it: crewai run
The crew will kick off, agents will collaborate, and you'll get an output like report.md.

## Why This Template is Useful
If you've ever wanted to experiment with multi-agent systems but found the official crewAI examples overwhelming or too code-heavy, this project strips it down to essentials. It's perfect for quick prototyping—whether you're building a research team (e.g., one agent searches, another analyzes, a third writes), an automation pipeline, or something creative.
Since it's brand new (just created today!), it's a fresh starting point you can fork and build on. Feel free to star it, contribute, or open issues with ideas.
If you're sharing this on your blog, it's an excellent way to showcase how approachable multi-agent AI has become in 2026. Let me know if you'd like help with specific customizations or examples!
