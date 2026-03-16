# AutoResearch Project

This repository contains two versions of the AutoResearch project:

1.  **[Original AutoResearch](./original_autoresearch)**:
    The original code by Andrej Karpathy, which focuses on autonomous research for optimizing neural network training hyperparameters.

2.  **[Nebius AutoResearch](./nebius_autoresearch)**:
    A modified version that uses Nebius AI Studio to optimize system prompts. This version demonstrates how to use an AI agent to iteratively improve prompts for a specific task.

## Structure

- `original_autoresearch/`: Contains `train.py`, `prepare.py`, and other files related to the original neural network optimization.
- `nebius_autoresearch/`: Contains `agent.py`, `experiment.py`, `scorer.py`, `main.py`, and other files for the prompt optimization task using Nebius API.

## Getting Started

To run the Nebius version:
1.  Navigate to `nebius_autoresearch`.
2.  Set up your `.env` file with `NEBIUS_API_KEY`.
3.  Run `python main.py`.

To run the Original version:
1.  Navigate to `original_autoresearch`.
2.  Follow the instructions in the original documentation (if available) or inspect `train.py`.
