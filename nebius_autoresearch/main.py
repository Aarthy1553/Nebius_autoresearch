import json
import os
import uuid
import time
from datetime import datetime

# Import our modular components
from agent import propose_experiment
from experiment import run_experiment
from scorer import score_response

# Configuration
RESULTS_FILE = "results.json"
PROGRAM_FILE = "program.md"
ITERATIONS = 250

def load_history():
    """Load previous experiment results from JSON file."""
    if os.path.exists(RESULTS_FILE):
        with open(RESULTS_FILE, "r") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []
    return []

def save_history(history):
    """Save experiment results to JSON file."""
    with open(RESULTS_FILE, "w") as f:
        json.dump(history, f, indent=2)

def print_progress_report(history):
    """Print a summary of progress every 25 experiments."""
    if not history:
        return
        
    best_record = max(history, key=lambda x: x.get('score', 0))
    
    print("\n" + "="*27)
    print("===== Progress Report =====")
    print(f"Experiments completed: {len(history)}")
    print(f"Best score so far: {best_record.get('score', 0)}")
    print(f"Best prompt: {best_record.get('prompt')[:100]}...")
    print("="*27 + "\n")

def main():
    print(f"Starting AutoResearch Loop (Target: {ITERATIONS} iterations)")
    
    # 1. Read the Research Goal
    try:
        with open(PROGRAM_FILE, "r") as f:
            goal = f.read().strip()
        print(f"Goal: {goal[:50]}...")
    except FileNotFoundError:
        print(f"Error: {PROGRAM_FILE} not found.")
        return

    # 2. Load History
    history = load_history()
    start_iteration = len(history)
    print(f"Loaded {start_iteration} previous experiments.")

    if start_iteration >= ITERATIONS:
        print("Target iterations already reached.")
        print_progress_report(history)
        return

    # Main Research Loop
    for i in range(start_iteration, ITERATIONS):
        print("-" * 50)
        print(f"Experiment {i+1} / {ITERATIONS}")
        
        # Step 3: Agent proposes a new experiment (System Prompt)
        print("Agent reasoning...")
        # The agent function prints the thought process internally
        system_prompt = propose_experiment(history, goal)
        print(f"Proposed prompt: {system_prompt[:100]}...")

        # Step 4: Run the experiment (Generate Explanation)
        # print("Running experiment...") # Optional, user didn't ask for this line in example but implied
        response = run_experiment(system_prompt)
        
        # Step 5: Score the result
        score = score_response(response)
        print(f"Score: {score}")
        print("-" * 50)

        # Step 6: Log the result
        experiment_record = {
            "experiment_id": str(uuid.uuid4()),
            "timestamp": datetime.now().isoformat(),
            "prompt": system_prompt,
            "response": response,
            "score": score
        }
        
        history.append(experiment_record)
        save_history(history)
        
        # Progress Report every 25 experiments
        if (i + 1) % 25 == 0:
            print_progress_report(history)
            
        # Rate limiting
        time.sleep(1)

    # End of Loop: Report Final Results
    print("\n" + "="*25)
    print("===== Final Results =====")
    print("Best experiment found")
    
    if history:
        best_record = max(history, key=lambda x: x.get('score', 0))
        print(f"Prompt: {best_record.get('prompt')}")
        print(f"Score: {best_record.get('score', 0)}")
    else:
        print("No results found.")
    print("="*25)

if __name__ == "__main__":
    main()
