alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt(plain_text, cipher_shift):

    cipher_text = ""

    for char in plain_text:
        if char == ' ':
            cipher_text += ' '
        else:
            target_index = alphabet.index(char) + cipher_shift
            if target_index > 25:
                target_index = target_index - 26
            cipher_text += ''.join(alphabet[target_index])
    
    print(f"The encoded text is:\n{cipher_text}")

def decrypt(cipher_text, reverse_shift):
    
    plain_text = ""

    for char in cipher_text:
        if char == ' ':
            plain_text += ' '
        else:
            target_index = alphabet.index(char) - reverse_shift
            if target_index < 0:
                target_index = target_index + 26
            plain_text += ''.join(alphabet[target_index])

    print(f"The plain text is:\n{plain_text}")