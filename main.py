# Imports
import random

# Machine's RGN (randomly generated number)
machine = random.randrange(11)

# GAME
def game ():
    print("Hello and welcome to my game! are you ready to play?")
    response = input("")
    if response == "yes":
        print("Lets begin!")
    else:
        print("Okay, come back when you are ready to play!")

    print("Pick a number between 1 and 10")
    num = int(input(""))
    if num == machine:
        print("WOW! great guess, you are correct the right number was: " + str(machine))
    else:
        print("Nope, the number was:" + str(machine) )

game()