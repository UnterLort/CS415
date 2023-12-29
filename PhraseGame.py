# @Kyle Stewart @PhraseGame.py version 1
# Import the draw_scoreboard function from the DrawScoreboard module
from DrawScoreboard import draw_scoreboard


# Function to display the guessed letters separated by commas
def display_guessed_letters(guessed_letters):
    return ", ".join(guessed_letters)


# Function to display the secret phrase with guessed letters and dashes
def display_secret_phrase(secret_phrase, guessed_letters):
    guessed_phrase = ""
    for char in secret_phrase:
        if char.lower() in guessed_letters or char == " " or char == "'":
            guessed_phrase += char
        else:
            guessed_phrase += "-"
    return guessed_phrase


# Function to play the game
def play_game(secret_phrase, total_guesses):
    guessed_letters = []
    guessed_left = total_guesses

    while True:
        # Print the scoreboard
        print(draw_scoreboard(total_guesses, total_guesses - guessed_left))
        # Print the current state of the game
        print(f"Secret Phrase: {display_secret_phrase(secret_phrase, guessed_letters)}")
        print(f"Guessed Letters: {display_guessed_letters(guessed_letters)}")

        # Prompt the user for a guess
        guess = input("Enter a letter to guess or \"!\" to end the game: ")

        if guess == "!":
            print("Game ended.")
            break

        if guess in guessed_letters:
            print("You already guessed that letter.")

        elif guess in secret_phrase.lower():
            # Add the correct guess to the guessed_letters list
            guessed_letters.append(guess)
            # Check if all the letters in the secret phrase have been guessed
            if display_secret_phrase(secret_phrase, guessed_letters) == secret_phrase:
                print("=" * 40)
                print("You won! The phrase was:", secret_phrase)
                print("=" * 40)
                break
            else:
                # Print the updated scoreboard and a message for a correct guess
                print(draw_scoreboard(total_guesses, total_guesses - guessed_left))
                print("Correct guess!")

        else:
            # Lower the number of guesses left
            guessed_left -= 1
            # Add the incorrect guess to the guessed_letters list
            guessed_letters.append(guess)
            print("No, " + guess + " is not in the phrase")
            # Print the updated scoreboard
            print(draw_scoreboard(total_guesses, total_guesses - guessed_left))

            if guessed_left == 0:
                print("=" * 40)
                print("Game over! You ran out of guesses.")
                print("The phrase was:", secret_phrase)
                print("=" * 40)
                break


# Call the play_game function with the secret phrase and a total number of guesses
play_game(secret_phrase="Python", total_guesses=5)
