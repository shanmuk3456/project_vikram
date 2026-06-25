import re
import json

def clean_json(response):
    response = response.strip()
    response = response.replace("```json", "").replace("```", "")
    return response


def parse_response(response):
    try:
        match = re.search(r'\{.*\}', response, re.DOTALL)
        json_str = match.group(0)
        return json.loads(json_str)

    except Exception as e:
        print("⚠️ JSON parsing failed:", e)
        try:
            fixed = response.replace('\\"', '"').replace('\\', '\\\\')
            match = re.search(r'\{.*\}', fixed, re.DOTALL)
            if match:
                return json.loads(match.group(0))
        except:
            pass
        return {"action": "general", "content": response}
