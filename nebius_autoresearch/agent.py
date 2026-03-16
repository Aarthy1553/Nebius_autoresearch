from typing import List, Dict, Any
from client import generate_response

def propose_experiment(history: List[Dict[str, Any]], goal: str) -> str:
    """
    Proposes a new system prompt based on the research goal and experiment history.
    
    Args:
        history: List of previous experiment results (dicts with 'prompt' and 'score').
        goal: The research goal string.
        
    Returns:
        str: The proposed system prompt for the next experiment.
    """
    # Format history for the prompt context
    if not history:
        history_text = "No previous experiments."
    else:
        # Use the last 3 experiments to provide context without overflowing context window
        recent_history = history[-3:]
        history_text = "\n".join([
            f"Attempt {i+1}:\n"
            f"Prompt: {r.get('prompt', 'Unknown')}\n"
            f"Score: {r.get('score', 0)}/10\n" 
            for i, r in enumerate(recent_history)
        ])
    
    system_instruction = (
        "You are an expert AI researcher optimizing a system prompt to achieve a specific goal.\n"
        "Analyze the previous attempts and their scores. Identify what worked and what didn't.\n"
        "Then, generate a NEW, improved system prompt that is likely to achieve a higher score.\n"
        "Do not repeat previous prompts. Be creative and precise.\n\n"
        "Format your response exactly as follows:\n"
        "THOUGHT: <your analysis and plan>\n"
        "PROMPT: <the actual system prompt text>"
    )
    
    user_message = (
        f"Research Goal:\n{goal}\n\n"
        f"Experiment History:\n{history_text}\n\n"
        "Based on the above, generate the next system prompt to test.\n"
        "Ensure you include your thought process before the prompt."
    )
    
    # Combine instructions
    full_prompt = f"{system_instruction}\n\n{user_message}"
    
    response = generate_response(full_prompt).strip()
    
    # Parse the response
    thought = ""
    prompt = response
    
    if "THOUGHT:" in response and "PROMPT:" in response:
        try:
            parts = response.split("PROMPT:", 1)
            thought_part = parts[0].split("THOUGHT:", 1)[1].strip()
            prompt_part = parts[1].strip()
            thought = thought_part
            prompt = prompt_part
        except IndexError:
            # Fallback if splitting fails
            pass
    elif "PROMPT:" in response:
        try:
            prompt = response.split("PROMPT:", 1)[1].strip()
        except IndexError:
            pass
            
    if thought:
        print(f"\n[Agent Thought]: {thought}")
        
    return prompt
