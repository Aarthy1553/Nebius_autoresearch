from client import generate_response
import re

def score_response(response):
    """
    Scores the response using an LLM judge.
    Returns a score between 0.0 and 1.0.
    """
    
    judge_prompt = (
        "You are a strict judge evaluating an explanation of 'Vector Databases' written for a 5-year-old.\n"
        "Analyze the following explanation based on these criteria:\n"
        "1. Simplicity: Is the language appropriate for a 5-year-old? (No jargon)\n"
        "2. Analogy: Does it use a good analogy? (e.g., toy box, library)\n"
        "3. Accuracy: Is the analogy technically sound (even if simplified)?\n"
        "4. Engagement: Is it fun to read?\n\n"
        "Explanation to evaluate:\n"
        f"\"\"\"{response}\"\"\"\n\n"
        "Give a score between 0.0 and 1.0, where 1.0 is perfect and 0.0 is terrible.\n"
        "Output ONLY the number, nothing else."
    )
    
    try:
        score_text = generate_response(judge_prompt).strip()
        # Extract the first floating point number found
        match = re.search(r"0\.\d+|1\.0|0|1", score_text)
        if match:
            score = float(match.group())
            return max(0.0, min(1.0, score)) # Ensure within bounds
        else:
            print(f"Error parsing score from: {score_text}")
            return 0.0
    except Exception as e:
        print(f"Error in scorer: {e}")
        return 0.0
