from models.llm import ask_coder
from tools.file_tools import read_file

def code_generate(prompt, f, filename):
    system_prompt = f""" 
    You are an AI coder. 
    Return ONLY valid JSON. 
    No explanation.
    
    STRICT RULES: 
    - Return ONLY JSON 
    - Do NOT explain anything 
    - Do NOT add text before or after JSON 
    - Output must start with '{' and end with '}' 
    - No markdown 

    IMPORTANT:
    - Escape all double quotes inside "content" using \"
    - Escape all backslashes using \\
    - Ensure valid JSON string
    - Never use index.html unless requested

    JSON format:
    {{
        "code": "..."
    }}

    User request: {prompt}
    """
    if f:
        system_prompt += f"""
    you need to edit this code based on the prompt
    json format:
    code:
    """ + str(read_file(filename))
    response = ask_coder(system_prompt)
    return response
