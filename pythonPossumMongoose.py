# Filename: pythonPossumMongoose.py
# Written by: EBCheez
# Written on: A cold night in November, 2022
# Description: A twist on rock paper scissors


# semicolons? we don't need no stinkin' semicolons
import random

user_wins = 0
computer_wins = 0

options = ["python", "possum", "mongoose"]

while True:
    user_input = input("Type Python/Possum/Mongoose or Q to quit: ").lower()
    if user_input == 'q':
        break

    if user_input not in options:
        continue

    random_number = random.randint(0, 2)
    # python: 0, possum: 1, mongoose: 2
    computer_pick = options[random_number]
    print("Computer picked", computer_pick + ".")

    if user_input == "python" and computer_pick == "possum":
        print("You won!")
        user_wins += 1

    elif user_input == "possum" and computer_pick == "mongoose":
        print("You won!")
        user_wins += 1

    elif user_input == "mongoose" and computer_pick == "python":
        print("You won!")
        user_wins += 1

    else:
        print("You lost!")
        computer_wins +=1

print("You won", user_wins, "times.")
print("The gerbil in your computer won", computer_wins, "times.")
print("Hasta la vista, baby!")
