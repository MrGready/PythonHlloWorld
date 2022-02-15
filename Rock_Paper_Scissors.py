import random

#Create a greeting for your program
print("Wolcome to Rock, Paper, Scissors, Shoot")

#Give the user the options they can choose from
user_choice = int(input("Rock, paper, or scissors. What do you choose? Type 0 for Rock, 1 for Paper, and 2 for Scissors"))

#Generate the computer's choice
comp_choice = random.randint(0,2)

choices = ["rock", "paper", "scissors"]

print("You chose " + choices[user_choice] + " and the computer chose " + choices[comp_choice])

if user_choice > 2 or user_choice < 0:
    print("You entered an invalid number. You lose")
elif user_choice == comp_choice:
    print("It's a draw")
elif user_choice == 0 and comp_choice == 1:
    print("You lose")
elif user_choice == 0 and comp_choice == 2:
    print("You win")
elif user_choice == 1 and comp_choice == 0:
    print("You win")
elif user_choice == 1 and comp_choice == 2:
    print("You lose")
elif user_choice == 2 and comp_choice == 0:
    print("You lose")
elif user_choice == 2 and comp_choice == 1:
    print("You win")
