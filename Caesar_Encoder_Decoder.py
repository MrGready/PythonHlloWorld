#from replit import clear

bid_dict = {}

key_list = []

bid_active = True

def auction_attendance():
    user = input("What is your name? ")
    bid = input("What is your bid? $")

    bid_dict[user] = bid
    
    key_list.append(user)
    
    cont = input("Are there any other users that wish to bid? yes or no\n").lower()
    
    if cont == "yes":
        bid_active is True
        #clear()
        auction_attendance()
    elif cont == "no":
        bid_active is False
        highest_bid(bid_dict)
        #print(cont)

def highest_bid(x):
    top_bid = bid_dict[key_list[0]]
    for key in x:
        if x[key] > top_bid:
            top_bid = x[key]
    print("The winning bid is $" + top_bid)
    
def run():
    if bid_active is True:
        auction_attendance()
        
run()