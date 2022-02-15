MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5
    },
    "latte": {
        "ingredients" : {
            "water":200,
            "milk":150,
            "coffee": 24,
            },
            "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0}
    }

operational = True
water = 300
milk = 200
coffee = 100
m = 0.0
money = "{:.2f}".format(m)

def in_stock(x, c):
    global operational
    global m
    
    if "water" in MENU.get(x, {}).get("ingredients", {}):
        if water < MENU.get(x, {}).get("ingredients", {}).get("water"):
            print("Sorry there is not enough water")
            operational = False
    if "milk" in MENU.get(x, {}).get("ingredients", {}):
        if milk < MENU.get(x, {}).get("ingredients", {}).get("milk"):
            print("Sorry there is not enough milk")
            operational = False
    if "coffee" in MENU.get(x, {}).get("ingredients", {}):
        if coffee < MENU.get(x, {}).get("ingredients", {}).get("coffee"):
            print("Sorry there is not enough coffee")
            operational = False
    if m < MENU.get(x, {}).get("cost"):
        print("Sorry that's not enough money. Money has been refunded")
    elif operational is False:
        m -= c
        print("We have refunded your order")
    else:   
        change = c - MENU.get(drink, {}).get("cost", {})
        print("Here is your change: " + "{:.2f}".format(change) + "\nHave a nice day")

def update(x):
    global water
    global milk
    global coffee
    
    if "water" in MENU.get(x, {}).get("ingredients", {}):
        water -= MENU.get(x, {}).get("ingredients", {}).get("water", {})
    if "milk" in MENU.get(x, {}).get("ingredients", {}):
        milk -= MENU.get(x, {}).get("ingredients", {}).get("milk", {})
    if "coffee" in MENU.get(x, {}).get("ingredients", {}):
        coffee -= MENU.get(x, {}).get("ingredients", {}).get("coffee", {})
    
while operational == True:
    
    current_total = 0.0
    
    drink = input("What drink would you like? (espresso/latte/cappucino): ")
    
    if drink == "report":
        print("Water: " + str(water) + "ml\nMilk: " + str(milk) + "ml\nCoffee: " + str(coffee) + "g\nMoney: $" + str(money))
    
    if drink == "espresso" or drink == "latte" or drink == "cappuccino":
        print("Please insert coin.")
        quarters = input("How many quarters?: ")
        m += float(quarters) * 0.25
        current_total += float(quarters) * 0.25
        dimes = input("How many dimes?: ")
        m += float(dimes) * 0.1
        current_total += float(dimes) * 0.1
        nickels = input("How many nickels?: ")
        m += float(nickels) * 0.05
        current_total += float(nickels) * 0.05
        pennies = input("How many pennies?: ")
        m += float(pennies) * 0.01
        current_total += float(nickels) * 0.01
        
        in_stock(drink, current_total)
        
        update(drink)