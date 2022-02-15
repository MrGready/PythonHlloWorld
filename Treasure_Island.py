import random

#Create a list of letter options
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
           'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
           'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
           'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

#Create a list of number options
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

#Create a list of symobl options
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '+', '_', '=']

#Create a greeting for your program
print("Welcome to the PyPassword Generator")

#Ask user how many letters they want their password to be
password_letter_count = int(input("How many letters would you like in your password? "))

#Ask user how many numbers they want their password to be
password_number_count = int(input("How many numbers would you like in your password? "))

#Ask user how many symbols they want their password to be
password_symbol_count = int(input("How many symbols would you like in your password? "))

passwword_length = password_letter_count + password_number_count + password_symbol_count

new_password = ""

#for x in passwword_length:
for i in range(0, password_letter_count):
        rand_letter = random.randint(0, len(letters)-1)
        new_password += letters[rand_letter]

for i in range(0, password_number_count):
        rand_number = random.randint(0, len(numbers)-1)
        new_password += numbers[rand_number]
        
for i in range(0, password_symbol_count):
        rand_symbol = random.randint(0, len(symbols)-1)
        new_password += symbols[rand_symbol]
        
print(new_password)
print(''.join(random.sample(new_password, len(new_password))))