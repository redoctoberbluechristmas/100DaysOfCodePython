from cipherfunctions import caesar
#from roughcipherfunctions import caesar
from art import logo

print(logo)

should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    
    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
    #caesar(input_text=text, shift_amount=shift, code_direction=direction)
    
    will_continue = input("Type 'yes' if you want to go again. Otherwise type 'no'. ")
    
    if will_continue != "yes":
        print("Goodbye")
        should_continue = False