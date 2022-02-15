import random

print("Welcome to the Number Guessing Game")
print("I'm thinking of a number between 1 and 100, think you can guess it?")
difficulty = input("Do you wish to play on 'easy' or 'hard' mode?\n")

number = random.randint(1, 100)

guesses_left = 0

if difficulty == "easy":
    guesses_left = 10
elif difficulty == "hard":
    guesses_left = 5
    
while guesses_left != 0:
    print("You have " + str(guesses_left) + " guesses left.")
    guess = input("What number will you guess? ")
    if int(guess) < number:
        print("That number is too low, try again.")
        guesses_left -= 1
    if int(guess) > number:
        print("That number is too high, try again.")
        guesses_left -= 1
    if int(guess) == number:
        print("That was the correct number. Congradulations, congradulations you won")
        break
    
if guesses_left == 0:
    print("Looks like your out of guesses, sorry")  