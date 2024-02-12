from openai import OpenAI
client = OpenAI()

MODEL = "gpt-4-turbo-preview"

def chat_with_ai():
    print(f"You are now chatting with {MODEL}. Type '/exit' to end the conversation.")
    conversation = [{"role": "system", "content": "You are a helpful assistant."}]
    
    while True:
        user_input = input("You: ")
        conversation.append({"role": "user", "content": user_input}),
                
        # Check if the user wants to exit
        if user_input.strip().lower() == "/exit":
            print("Exiting the chat. Goodbye!")
            break
        
        try:

            response = client.chat.completions.create(
                model=MODEL,
                messages=conversation,
                stop=None,  # Adjust based on your specific needon
                max_tokens=150,
                temperature=1,  # Adjust to control the randomness. Default is 1
                top_p=1.0,
                frequency_penalty=0.0,
                presence_penalty=0.0,
                user="user_id"  # Optional: Replace with the user's ID for personalized responses
            )
            
            # Print the AI's response
            reply = response.choices[0].message.content
            print("AI: ", reply)
            conversation.append({"role": "assistant", "content": reply})
        
        except Exception as e:
            print(f"An error occurred: {e}")

# Start the chat
chat_with_ai()