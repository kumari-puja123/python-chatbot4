print("Namaste! Welcome to My Chatbot ")
print("You can ask me basic questions.")
print("Type 'bye' to exit the chatbot.")

# Chatbot responses
responses = {
    "hello": "Hi! Welcome. How can I help you?",
    "hi": "Hello! How are you?",
    "how are you": "I am fine. Thank you!",
    "who are you": "I am a simple AI chatbot.",
    "what is python": "Python is a programming language.",
    "motivate me": "Keep going! You are doing great. ",
    "thank you": "You are welcome!",
    "bye": "Goodbye! Have a nice day!"
}

# Main chatbot loop
while True:

    # Take input from user
    user_input = input("You: ").lower()

    # Check if user wants to exit
    if user_input == "bye":
        print("Bot:", responses["bye"])
        break

    # Check whether question is available
    if user_input in responses:
        print("Bot:", responses[user_input])

    else:
        print("Bot: Sorry, I don't understand this question.")