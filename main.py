from chatbot import get_response

print("Bot: Hello! Type 'quit' to exit.")
while True:
    msg = input("You: ")
    if msg.lower() == 'quit':
        print("Bot: Goodbye!")
        break
    response = get_response(msg)
    print("Bot:", response)
