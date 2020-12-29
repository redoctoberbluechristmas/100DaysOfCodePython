from cipherfunctions import caesar

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

caesar(input_text=text, shift_amount=shift, code_direction=direction)