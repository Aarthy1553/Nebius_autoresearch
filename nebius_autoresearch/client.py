import os
import json
import requests

def generate_response(prompt):
    """
    Sends a prompt to the Nebius Token Factory API and returns the response text.
    
    Uses the OpenAI-compatible API format.
    
    Args:
        prompt (str): The user prompt to send to the model.
        
    Returns:
        str: The text content of the model's response.
        
    Raises:
        ValueError: If NEBIUS_API_KEY is not set.
        requests.exceptions.RequestException: If the API call fails.
    """
    api_key = os.environ.get("NEBIUS_API_KEY")
    if not api_key:
        raise ValueError("NEBIUS_API_KEY environment variable not set")
        
    # Nebius Token Factory OpenAI-compatible endpoint
    url = "https://api.tokenfactory.nebius.com/v1/chat/completions"
    
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }
    
    payload = {
        "model": "meta-llama/Llama-3.3-70B-Instruct",
        "messages": [
            {"role": "user", "content": prompt}
        ],
        # Optional parameters for generation control
        "temperature": 0.7,
        "max_tokens": 4096
    }
    
    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        
        result = response.json()
        
        # Extract the content from the first choice
        if "choices" in result and len(result["choices"]) > 0:
            return result["choices"][0]["message"]["content"]
        else:
            return ""
            
    except requests.exceptions.RequestException as e:
        print(f"Error calling Nebius API: {e}")
        if hasattr(e.response, 'content'):
             print(f"Response content: {e.response.content.decode()}")
        raise
