import os

def create_react_app(project_name="myapp"):
    os.system(f"npx create vite@latest {project_name}")
    return f"React app '{project_name}' created."


def list_files():
    return "\n".join(os.listdir())