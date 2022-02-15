import random

#Step 1
word_list = ["ardvark", "baboon", "camel"]

#1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word
chosen_word = word_list[random.randint(0, 2)]

#2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase
user_guess =  input("Guess a letter and see if it's in the chosen word. ")
user_guess = user_guess.lower()

#3 - Check if the letter the user guessed is one of the letters of the chosen_word
for i in range(0, len(chosen_word)):
    if user_guess == chosen_word[i]:
        guess = True
        break
    else:
        guess = False

if guess == True:
    print("Congradulations. The letter you guessed was in the chosen word")
else:
    print("Sorry. The letter you guessed was not in the chosen word")