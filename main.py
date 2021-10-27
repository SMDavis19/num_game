# Imports
import random

# Opening prompt
print("Hello and welcome to my game!")
play = "Are you ready to play"
user = input(play)

if user == "No":
    print("Maybe next time")
elif user == "Yes":
    print("Lets begin! Im thinking of a number between 1-20")

# Machine's RGN (randomly generated number)
machine = random.randrange(21)

# Use's Choice
user_num = int("")

# Results
if user_num == machine:
    print("Well done you choice the same number!")
else:
    print("Im correct number was...")
    print(machine)
