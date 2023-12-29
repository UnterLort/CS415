# @Kyle Stewart @DrawScoreboard.py version 1
# Define the draw_scoreboard function with two parameters:
# total_guesses and incorrect_guesses
def draw_scoreboard(total_guesses, incorrect_guesses):
    # Makes an empty string to store the scoreboard
    scoreboard: str = ""

    # If total is greater than 0 run the following
    if total_guesses > 0:
        # scoreboard adds the following print * total
        scoreboard += "+" + "-----+" * total_guesses
        # new lines
        scoreboard += "\n"
        # scoreboard adds the following print * incorrect
        scoreboard += "|\\\ //" * incorrect_guesses
        # scoreboard adds the following print * (total - incorrect)
        scoreboard += "|     " * (total_guesses - incorrect_guesses)
        # These will be repeated 3 times
        scoreboard += "|\n"
        scoreboard += "| \\v/ " * incorrect_guesses
        scoreboard += "|     " * (total_guesses - incorrect_guesses)
        scoreboard += "|\n"
        scoreboard += "| /.\\ " * incorrect_guesses
        scoreboard += "|     " * (total_guesses - incorrect_guesses)
        scoreboard += "|\n"
        scoreboard += "|// \\\\" * incorrect_guesses
        scoreboard += "|     " * (total_guesses - incorrect_guesses)
        scoreboard += "|\n"
        # scoreboard adds the following print * total
        scoreboard += "+" + "-----+" * total_guesses
    # Return the scoreboard string
    return scoreboard


if __name__ == "__main__":
    # Prompts the user for the total number of guesses
    print("Enter number of guesses allowed between 1 and 11")
    total_guesses = int(input())
    # Prompts the user for the total number of incorrect guesses
    print("Enter number of incorrect guesses")
    incorrect_guesses = int(input())

    # Calls the draw_scoreboard with the user imputed values
    scoreboard = draw_scoreboard(total_guesses, incorrect_guesses)
    # Prints the scoreboard
    print(scoreboard)
    print("")
    # Prints a new line after the scoreboard
