# Imports
import random
import sqlite3

# Machine's RGN (randomly generated number)
machine = random.randrange(11)

# GAME
def game ():
    print("Please enter your name.")
    name = input("")
    print(f"Hello, {name}! Welcome to my number guessing game. Are you ready to play?")
    response = input("")
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

game()

# Connection to DB (Database)
def database():
    from pymongo import MongoClient
    import pymongo
