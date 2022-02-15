import random
from PyDictionary import PyDictionary as dictionary

#word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(dictionary)

lives = 6

#Test code
print(f'Pssst, the solution is {chosen_word}.')

#create blanks
display = []

for i in range(0, len(chosen_word)):
    display.append("_")

completed = False

while not completed:
    
    guess = input("Guess a letter: ").lower()

    #Check the guessed letter
    for i in range(0, len(chosen_word)):
        if guess == chosen_word[i]:
            display[i] = "" + guess + ""
        
    if guess not in chosen_word:
        lives -= 1
    
    if lives == 0:
        print("You Lose. Game Over")
        break
    
    print(display)
    print(lives)
    
    if "_" not in display:
        completed = True
        print("Congradulations. You Won!")