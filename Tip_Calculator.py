#Create a greeting for your program
print("Welcome to Treasure Island")

#Give the user an objective
print("Your mission is to find the treasure")

#Give the user their first choice
c1 = input("Do you go left or right? ")

#Create ifel statement
if c1 == "right":
    print("Game Over")
elif c1 == "left":
        c2 = input("You come to a lake, do you swim across or wait for a boat? ")
        if c2 == "swim":
            print("Game Over")
        elif c2 == "wait":
                c3 = input("Three doors appear before you, one red, one blue, and one yellow. Which do you choose? ")
                if c3 == "red":
                    print("Game Over")
                elif c3 == "blue":
                    print("Game Over")
                elif c3 == "yellow":
                        print("You found the treasure. Congradulations")
                else:
                    print("You did not choose a door. Game Over")
        else:
            print("You did not choose to wait or swim. Game Over")
else:
    print("You did not choose left or right. Game Over")