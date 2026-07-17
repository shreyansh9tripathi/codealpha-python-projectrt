import random

def chatbot():
    print("Hi! I'm Bot of Python Programming.")
    print("Type 'exit' or 'bye' to end the conversation.\n")

    responses = {
        "hello": [
            "Hi there!",
            "Hello! How can I help you today?",
            "Hey! Nice to meet you."
        ],
        "how are you": [
            "I'm just a computer program, but I'm doing great!",
            "Doing well, thanks for asking!"
        ],
        "name": [
            "I am a simple Python chatbot.",
            "You can call me PyBot."
        ],
        "help": [
            "I can answer basic greetings, tell you my name, and help you exit."
        ],
        "bye": [
            "Goodbye!",
            "Bye! Have a wonderful day!"
        ]
    }

    while True:
        user = input("You: ").strip().lower()

        if user in ["bye", "exit"]:
            print("Bot:", random.choice(responses["bye"]))
            break

        elif user in ["hi", "hello"]:
            print("Bot:", random.choice(responses["hello"]))

        elif user == "how are you":
            print("Bot:", random.choice(responses["how are you"]))

        elif user == "name":
            print("Bot:", random.choice(responses["name"]))

        elif user == "help":
            print("Bot:", random.choice(responses["help"]))

        else:
            print("Bot: I can't understand you. Please rephrase.")

# Run the chatbot
chatbot()