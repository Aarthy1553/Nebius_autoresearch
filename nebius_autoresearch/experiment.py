from client import generate_response

def run_experiment(system_prompt):
    """
    Runs the experiment by using the proposed system prompt to explain vector databases.
    """
    test_prompt = f"{system_prompt}\n\nExplain vector databases. Respond in under 120 words."
    return generate_response(test_prompt)
