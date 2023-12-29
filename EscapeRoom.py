# @Kyle Stewart @EscapeRoom.py version 2

def down():
    # if 1 is picked by the user game ends if the user picks 2 they win
    if button == 1:
        print("A trap door opens underneath your feet and you fall. GAME OVER")
    elif button == 2:
        print("The door opens. You're free. YOU WIN!")
    else:
        print("You hurt your finger pressing a button that doesn't exist. GAME OVER")
        # If the user does not pick one of the following buttons above the game ends


def up():
    # if the amount of cookies are 2 to 5 they go to the next step if not the game ends
    if eat < 2:
        print("Your friends eat all the rest. You get too hungry and have to quit. GAME OVER")
    elif eat > 5:
        print("You get a stomach ache and can't search any more. GAME OVER")
    else:
        print(
            "You notice a secret keypad under the cookie plate. Enter the weight of the remaining cookies in ounces, "
            "if each one weighs 1.5 ounces.")
        weight = float(input())
        # The user will have to put in the right weight that would be the amount of cookies left from 7.5 to 12 ounces
        float(eat)
        leftW = 1.5 * (10 - eat)
        # This makes the does the math to calculate the amount of ounces that the remaining cookies would weigh
        if weight == leftW:
            print("A secret door opens for you to exit. YOU WIN!")
        else:
            print("Incorrect. GAME OVER")
            # If the user does not pick the right weight the game ends


print("You are in a room with a door and stairs. Which way will you go?")
where = str(input())
# This starts off the escape room by asking the user where they want to go after the print statement

# An if statement will trigger with 3 options depending on the users input
if where == "door":
    print("There are 2 buttons on the door. Which do you press?")
    button = int(input())  # This will move the user to the door path of the escape room
    down()
elif where == "stairs":
    print("There are 10 cookies on a plate. How many do you eat?")
    eat = int(input())  # This will move the user to the stairs path of the escape room
    up()
else:
    print("That's not a valid direction. You trip and fall. GAME OVER")
    # If the user does not pick one of the following directions above the game ends
