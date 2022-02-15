alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 
            'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")

text = input("Type your message:\n").lower()

shift = int(input("Type the shift number:\n"))

def caesar(direction, x, y):
    encoded_list = []
    decoded_list = []
    
    for i in range(0, len(x)):
        for a in range(0, len(alphabet)):
            if x[i] == alphabet[a]:    
                if direction == "encode":
                    while (a + y) > 26:
                        y = (a + y)%26
                    print(a + y)
                    #encoded_list.append(alphabet[a + y])
                elif direction == "decode":
                    decoded_list.append(alphabet[a - y])
    if x[i] != alphabet[a]:
        if direction == "encode":
            encoded_list.append(x[i])
        elif direction == "decode":
            decoded_list.append(x[i])
                    
    if direction == "encode":
        encoded_word = ''.join(encoded_list)
        print("The encoded message is " + encoded_word)
    elif direction == "decode":
        decoded_word = ''.join(decoded_list)
        print("The decoded message is " + decoded_word)

caesar(direction, text, shift)

go_again = input("Do you want to restart the cipher program, yes or no? ").lower()

def play_again():
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")

    text = input("Type your message:\n").lower()

    shift = int(input("Type the shift number:\n"))
    
    caesar(direction, text, shift)
    
if go_again == "yes":
    play_again()