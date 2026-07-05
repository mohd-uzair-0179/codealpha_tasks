###   PROJECT 4: BASIC CHATBOT   ###

# Function to process the user's input and generate a response
def chat_bot(chat):

    # Check the user's message and respond accordingly
    if chat == "hello" or chat == "hi":
        print("Flash: Hello Uzair! Nice to see you.")

    elif chat == "how are you":
        print("Flash: I'm doing great! How about you, Uzair?")

    elif chat == "what is your name":
        print("Flash: My name is Flash.")

    elif chat == "tell me a quote":
        print("Flash: Have faith in yourself. Small steps every day lead to big achievements.")

    elif chat == "what is my name":
        print("Flash: Your name is Uzair.")

    elif chat == "who made you":
        print("Flash: I was made using Python by Uzair.")

    elif chat == "what can you do":
        print("Flash: I can answer simple questions and chat with you.")

    elif chat == "thank you" or chat == "thanks":
        print("Flash: You're most welcome, Uzair!")

    elif chat == "good morning":
        print("Flash: Good morning, Uzair! Have a wonderful day.")

    elif chat == "good night":
        print("Flash: Good night, Uzair! Sweet dreams.")

    elif chat == "bye":
        print("Flash: Goodbye, Uzair! See you again.")

    # Default response for unrecognized input
    else:
        print("Flash: Sorry Uzair, I don't understand that.")


# Display chatbot welcome screen
print("=" * 50)
print(" " * 12 + "Welcome to Flash ChatBot")
print("=" * 50)
print("\nFlash: Hello Uzair!")
print("Flash: Type 'bye' whenever you want to leave.")

# Variable to store the user's message
chat = ""

# Keep chatting until the user types "bye"
while chat != "bye":

    # Take input from the user and convert it to lowercase
    chat = input("\nUzair: ").lower()

    # Call the chatbot function to generate a response
    chat_bot(chat)
