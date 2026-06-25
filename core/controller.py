from prompt.code_prompt import code_generate
from prompt.decide_prompt import decide_and_generate
from prompt.reply_prompt import reply_generation
from tools.file_tools import create_file,edit_file
from tools.project_tools import  create_react_app, list_files
from core.parser import clean_json,parse_response
import json

def handle_prompt(prompt):

    raw = clean_json(decide_and_generate(prompt))
    data = parse_response(raw)
    action = data.get("action")

    if action == "create_file":
        content = json.loads(clean_json(code_generate(prompt,False,data["filename"])))
        return create_file(data["filename"],content["code"])

    elif action == "edit_file":
        content = json.loads(clean_json(code_generate(prompt,True,data["filename"])))
        return edit_file(data["filename"], content["code"])

    elif action == "create_react_app":
        return create_react_app()

    elif action == "list_files":
        return list_files()

    else:
        return reply_generation(prompt)
