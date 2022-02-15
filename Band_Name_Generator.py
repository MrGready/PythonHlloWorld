#Create a greeting for your program
print("Welcome to Tip Calculator")

#Ask how much the bill is and store in float
bill = float(input("What was the total bill? $"))

#Ask user how much of tip they wish to leave
tip_percentage = int(input("How much of a tip do you want to leave? 10%, 15%, or 20%? "))

#Multiple the bill by 1/100th of the tip they want to leave
tip_amount = float(bill * (tip_percentage)/100)

#Format the tip amount
new_tip_amount = format(tip_amount, '.2f')

#Print the tip amount
print("Your tip should be $" + new_tip_amount)