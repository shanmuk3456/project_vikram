def clean_code(content):
    content = content.strip()
    content = content.replace("```html", "")
    content = content.replace("```javascript", "")
    content = content.replace("```js", "")
    content = content.replace("```", "")
    return content

def create_file(filename, content):
    with open(filename, "w", encoding="utf-8") as f:
        f.write(clean_code(content))
    return f"{filename} created successfully."

def read_file(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return f.read()
    
def edit_file(filename, content):
    with open(filename, "w", encoding="utf-8") as f:
        f.write(clean_code(content))
    return f"{filename} updated successfully."
    