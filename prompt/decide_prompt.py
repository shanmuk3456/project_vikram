from models.llm import ask_request
def decide_and_generate(prompt):

    system_prompt = f"""
    You are an AI system controller.

    Return ONLY valid JSON. No explanation.

    Actions:
    -
    - create_file
    - edit_file
    - create_react_app
    - list_files
    - general

    Rules:
    - If user wants new file → create_file
    - If user wants to modify file → edit_file
    - If user mentions file name → include it
    
    Filename rules:
    - If user asks for C → filename must end with .c (example: main.c)
    - If user asks for C++ → filename must end with .cpp
    - If user asks for HTML → filename must end with .html
    - If user asks for CSS → filename must end with .css
    - If user asks for JavaScript → filename must end with .js
    - If user provides a name → use it exactly with correct extension
    - If no name → use default based on type:
    - HTML → index.html
    - C → main.c
    - JS → script.js

    JSON format:
    {{
    "action": "...",
    "filename": "...",
    }}

    User request: {prompt}
    """
    response = ask_request(system_prompt)
    return response