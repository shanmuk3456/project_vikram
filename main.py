from core.controller import handle_prompt

if __name__ == "__main__":
    while True:
        user_input = input("\nYou: ")

        if user_input.lower() == "exit":
            break

        result = handle_prompt(user_input)
        print("\nAI:", result)