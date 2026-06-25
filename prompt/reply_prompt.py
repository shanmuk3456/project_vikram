from models.llm import ask_responce

def reply_generation(prompt):
    system_prompt = f"""
    User request: {prompt}

"""
    response = ask_responce(system_prompt)
    return response