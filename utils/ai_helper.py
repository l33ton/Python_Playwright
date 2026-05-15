import ollama

def get_ai_diagnostic(error_message, current_url, ids_and_names):
    prompt = f"""
    You are a diagnostic tool. DO NOT write greetings or "Let's dive in". 
    ONLY output the REASON and the FIX.

    CONTEXT:
    - Error Message: {error_message}
    - Current URL: {current_url}
    - Interactive Elements (JSON): {ids_and_names}
  
    STRICT ANALYSIS RULES:
    1. ACT AS A DETECTIVE. Compare the failed locator from the Error Message with the provided JSON list of elements.
    2. FIND THE TYPO: If you see "#loginpassword" and the JSON has "#login-password", point it out specifically.
    3. DON'T BE VAGUE: Do not say "check for typos". Say "You missed a dash" or "You have an extra 's'".
    4. PROVIDE CODE: Give me a single line of Python code that fixes the issue.

    OUTPUT FORMAT:
    - REASON: (Concise explanation)
    - FIX: (The exact Python line of code. No 'await', no Selenium!)
    """

    try:
        response = ollama.chat(
            model='llama3',
            messages=[{'role': 'user', 'content': prompt}],
            options={
                'temperature': 0,
                'num_predict': 100,
                'num_ctx': 2048,
                'top_p': 0.9
            }
        )
        return response['message']['content']
    except Exception as e:
        return f"Ollama Error: {str(e)}"