alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

def encrypt(text, shift):

    text = list(text)

    # Look up input letter in alphabet list, get index
    
    cipher_text = ""

    for char in text:
        if char == ' ':
            cipher_text += ' '
        else:
            target_index = alphabet.index(char) + shift
            cipher_text += ''.join(alphabet[target_index])
    
    print(cipher_text)

encrypt(text, shift)
    