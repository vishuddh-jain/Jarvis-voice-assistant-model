import ollama

def ask_ai(prompt):
    try:
        response = ollama.chat(
            model='phi',   # or 'phi'
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        return response['message']['content']
    except Exception as e:
        return "Sorry, I am having trouble connecting to AI."