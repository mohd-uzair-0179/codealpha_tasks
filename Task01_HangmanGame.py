###   PROJECT 1: HANGMAN GAME   ###

import random      # Used to randomly select a word from the list

# List of possible secret words
words = ["apple", "football", "paris", "lion", "asad"]

# Randomly choose one word and convert it to lowercase
word = random.choice(words).lower()

# Create a list of underscores (_) equal to the length of the secret word
display = ["_"] * len(word)

# Total number of incorrect guesses allowed
attempts = 6

# Stores all letters already guessed by the player
guessed = []

# Welcome Screen
print("=" * 55)
print(" " * 14 + "WELCOME TO THE HANGMAN GAME")
print("=" * 55)
print("\nThe Goal: Save the Man by guessing the Secret Word.")
print("\nRules:")
print(">> Guess one letter at a time.")
print(">> You have 6 wrong attempts.")
print(">> Guess all the letters to win.")
print("-" * 55)

# Ask the user whether to start the game
start = input("Enter S to Start Game: ").upper()

# Start the game only if the user enters S
if start == "S":

    # Continue playing until attempts become zero
    while attempts > 0:

        # Display the current progress of the word
        print("\nWord:", " ".join(display))
        print("Attempts Left:", attempts)

        # Take one letter as input from the user
        guess = input("Guess a Letter: ").lower()

        # Validate that only one alphabet letter is entered
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter only one letter.")
            continue

        # Check if the letter was already guessed
        if guess in guessed:
            print("You already guessed this letter.")
            continue

        # Store the guessed letter to prevent duplicate guesses
        guessed.append(guess)

        # Check whether the guessed letter exists in the secret word
        if guess in word:

            # Replace underscores with the correctly guessed letter
            for i in range(len(word)):
                if word[i] == guess:
                    display[i] = guess

            print("Correct Guess!")

        else:
            # Reduce attempts for an incorrect guess
            attempts -= 1
            print("Wrong Guess! Try Again.")

        # Check if the player has guessed the complete word
        if "_" not in display:
            print("\nCongratulations! You Won.")
            print("The Secret Word was:", word)
            break

        # Display Game Over message if no attempts are left
        if attempts == 0:
            print("\nGAME OVER! The Man is Hanged.")
            print("      _____")
            print("     |     |")
            print("     |     O")
            print("     |    /|\\")
            print("     |    / \\")
            print("  ___|___")
            print("\nThe Secret Word was:", word)

# If the user does not press S
else:
    print("Game Ended!")
