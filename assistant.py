import tkinter as tk
from intents import get_intent       # Intent recognition logic
from actions import perform_action   # Executes system tasks
from llm_handler import get_llm_response  # Calls the LLM for general questions

# Function triggered when the user submits a command
def handle_input():
    user_input = input_field.get()  # Get text from the input field
    log_text.insert(tk.END, f"You: {user_input}\n")  # Log user input
    
    intent = get_intent(user_input)  # Identify the intent of the command
    
    if intent:
        result = perform_action(intent, user_input)  # Perform system task
    else:
        result = get_llm_response(user_input)  # If no known intent, use LLM
    
    log_text.insert(tk.END, f"Assistant: {result}\n\n")  # Show result/response
    input_field.delete(0, tk.END)  # Clear the input field

# GUI setup using Tkinter
app = tk.Tk()
app.title("Smart Assistant")
app.geometry("600x400")

# Input field where user types the command
input_field = tk.Entry(app, font=("Arial", 14))
input_field.pack(fill=tk.X, padx=10, pady=10)

# Button to submit command
submit_btn = tk.Button(app, text="Ask", command=handle_input)
submit_btn.pack()

# Area to display assistant responses and logs
log_text = tk.Text(app, wrap=tk.WORD)
log_text.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

# Start the GUI event loop
app.mainloop()
