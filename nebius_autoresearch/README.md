# AutoResearch for Prompt Engineering

A simple, autonomous research agent that iteratively optimizes system prompts using an LLM-driven experiment loop. Inspired by Andrej Karpathy's [AutoResearch](https://github.com/karpathy/autoresearch).

## 🚀 What is this?

This project demonstrates the core concept of **autonomous research**: using an AI agent to propose ideas, run experiments, evaluate results, and learn from history—all without human intervention.

Instead of optimizing neural network code (like the original AutoResearch), this demo optimizes **system prompts**. The goal is to find the perfect prompt that makes an LLM explain complex topics (like Vector Databases) to a 5-year-old.

## 🔄 How it Works

The system runs a continuous loop of **Idea → Experiment → Evaluation**:

1.  **Agent (`agent.py`)**: Analyzes the research goal and previous results. It "thinks" about what to try next and proposes a new system prompt.
2.  **Experiment (`experiment.py`)**: Runs the proposed prompt against a test case (e.g., "Explain Vector Databases").
3.  **Scorer (`scorer.py`)**: Evaluates the output based on specific criteria (brevity, keywords, clarity) and assigns a score (0.0 - 1.0).
4.  **Logger (`main.py`)**: Saves the result to `results.json` so the agent can learn from it in the next iteration.

## 🛠️ File Structure

*   **`main.py`**: The orchestrator that runs the research loop.
*   **`program.md`**: Defines the research goal (e.g., "Explain Vector DBs to a 5-year-old").
*   **`agent.py`**: The "Researcher" — uses Nebius Token Factory to generate new prompt ideas.
*   **`experiment.py`**: The "Lab" — executes the prompt to generate a response.
*   **`scorer.py`**: The "Judge" — deterministically scores the response.
*   **`client.py`**: A reusable API client for Nebius Token Factory.
*   **`results.json`**: A log of all experiments, scores, and prompts.

## ⚡ Quick Start

1.  **Set up your API Key**:
    Ensure you have your Nebius API key set in your environment:
    ```bash
    export NEBIUS_API_KEY="your_api_key_here"
    ```

2.  **Run the Researcher**:
    ```bash
    python main.py
    ```

3.  **Watch it Learn**:
    The script will run 5 iterations, printing the agent's thought process and the experiment results. At the end, it will display the best prompt found.

## 📝 Example Output

```text
--- Iteration 1/5 ---
🤖 Agent is thinking...
[Agent Thought]: The previous attempt was too technical. I will try a LEGO analogy.
Proposed Prompt: You are a helpful teacher who explains things using LEGO blocks...

Pg Running experiment...
Response Length: 115 chars
Score: 1.0/1.0
✅ Result saved.
```

## License

MIT
