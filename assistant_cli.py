from intents import get_intent
from actions import perform_action
from llm_handler import get_llm_response

print("🤖 Smart Assistant CLI (Codespaces version)")
print("Type 'exit' to quit.\n")

while True:
    user_input = input("You: ")
    
    if user_input.lower() == "exit":
        break
    
    intent = get_intent(user_input)
    
    if intent:
        response = perform_action(intent, user_input)
    else:
        response = get_llm_response(user_input)
    
    print("Assistant:", response)
    print("-" * 50)
