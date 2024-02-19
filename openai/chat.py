from openai import OpenAI
client = OpenAI()

#### CONFIG ####
MODEL = "gpt-4-turbo-preview"
MAX_TOKENS = 200
TEMPERATURE = 1
TOP_P = 1.0
#### CONFIG ####

def exit_chat():
    print("Exiting the chat. Goodbye!")
    return True

def help_chat():
    print("Available commands:")
    print("/exit: Exit the chat.")
    print("/help: Display this help message.")
    # Add any other command descriptions here
    return False

# A dictionary mapping command strings to their corresponding functions
commands = {
    "/exit": exit_chat,
    "/help": help_chat,
    # Add other commands here
}

def process_input(user_input):
    command = user_input.strip().lower()
    if command in commands:
        return commands[command]()
    else:
        print("Unknown command. Type '/help' for a list of commands.")
        return False  


def chat_with_ai():
    print(f"You are now chatting with {MODEL}. Type '/help' for help and '/exit' to end the conversation.")
    conversation = [{"role": "system", "content": "You are a helpful assistant."}]
    
    while True:
        user_input = input("You: ")
        conversation.append({"role": "user", "content": user_input}),

        if (user_input.strip()[0] == "/"):
            exit_val = process_input(user_input)        
            if exit_val:
                break
        else:
            try:
                response = client.chat.completions.create(
                    model=MODEL,
                    messages=conversation,
                    stop=None,  # Adjust based on your specific needon
                    max_tokens=MAX_TOKENS,
                    temperature=TEMPERATURE,  # Adjust to control the randomness. Default is 1
                    top_p=TOP_P,
                    frequency_penalty=0.0,
                    presence_penalty=0.0,
                    user="user_id"  # Optional: Replace with the user's ID for personalized responses
                )
                
                # We append the response to provide context to conversations
                reply = response.choices[0].message.content
                print("AI: ", reply)
                conversation.append({"role": "assistant", "content": reply})
            
            except Exception as e:
                print(f"An error occurred: {e}")

# Start the chat
chat_with_ai()
