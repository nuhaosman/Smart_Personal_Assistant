import openai  # OpenAI's Python SDK

# Replace this with your actual OpenAI API key
openai.api_key = "YOUR_OPENAI_API_KEY"

# Function to send a message to the LLM and return its response
def get_llm_response(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Choose GPT model (can upgrade to GPT-4)
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        # Return the assistant's reply
        return response.choices[0].message['content'].strip()
    
    except Exception as e:
        # Handle LLM errors gracefully
        return f"LLM error: {e}"
