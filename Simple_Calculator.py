import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def start():
    user = []
    comp = []
    hit_me = ""
    user_total = 0
    comp_total = 0
    
    user.append(cards[random.randrange(0, len(cards))])
    user.append(cards[random.randrange(0, len(cards))])
    
    comp.append(cards[random.randrange(0, len(cards))])
    comp.append(cards[random.randrange(0, len(cards))])
    
    #print(user)
    #print(comp)
    
    card_game(user, comp)
    
    
    
def card_game(x, y):
    user_total = sum(x)
    comp_total = sum(y)
    hit_me = ""
    
    if user_total == 21:
        print(x)
        print("Congradulations, you have 21. You Win")
    elif comp_total == 21:
        print(x)
        print("Sorry, the computer has 21. You Lose")
    elif user_total > 21:
        for i in range(len(x)):
            if x[i] == 11:
                x[i] = 1
        user_total = sum(x)
        if user_total > 21:
            print(x)
            print("You bust. Sorry, You Lose")
    if user_total < 21:
        print(x)
        hit_me = input("Do you want to get another card? yes or no\n").lower()  
    if hit_me == "yes":
        x.append(cards[random.randrange(0, len(cards))])
        card_game(x, y)
    elif hit_me == "no":
        comp_draw(y)
        
    if user_total > comp_total:
        print("Congradulations, congradulations. You Won")
    elif user_total < comp_total:
        print("Sorry, dealer wins")
    elif user_total == comp_total:
        print("You and the dealer had the same total. It's a tie")        
    return hit_me

def comp_draw(a):
    comp_total = sum(a)
    
    while comp_total < 16:
        a.append(cards[random.randrange(0, len(cards))])
        
        comp_total = sum(a)
        
        if comp_total == 21:
            print("Sorry, the computer has 21. You Lose")
        elif comp_total > 21:
            for i in range(len(a)):
                if a[i] == 11:
                    a[i] = 1
            print("The computer went bust. You Win")
        elif comp_total < 21:
            return comp_total

start()