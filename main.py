# Imports
import random

# Machine's RGN (randomly generated number)
machine = random.randrange(11)

response = input("")
# GAME
def game ():
    print("Hello and welcome to my game! are you ready to play?")
    #response = input("")
    if response == "yes":
        print("Lets begin!")
    else:
        print("Okay, come back when you are ready to play!")
        exit()
    print("Pick a number between 1 and 10")
    num = int(input(""))
    if num == machine:
        print("WOW! great guess, you are correct the right number was: " + str(machine))
    else:
        print("Nope, the number was:" + str(machine) )

def re_run():
    print("Want to play again?")
    if response == "yes":
        game()
    else:
        print("thanks for playing!")
        exit()
game()