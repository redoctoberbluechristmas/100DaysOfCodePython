#These were my original answers, keeping for posterity but not recommended.

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(input_text, shift_amount, code_direction):

    output_text = ""

    for char in input_text:
        if char == ' ':
            output_text += ' '
        
        if code_direction == "encode":
            target_index = alphabet.index(char) + shift_amount
            if target_index > len(alphabet) - 1:
                target_index = target_index - len(alphabet)
            output_text += alphabet[target_index]
        
        else:
            target_index = alphabet.index(char) - shift_amount
            if target_index < 0:
                target_index = target_index + len(alphabet)
            output_text += alphabet[target_index]
    
    print(f"The {code_direction}d text is:\n{output_text}")

# def caesar(input_text, shift_amount, code_direction):

#     if code_direction == "encode":
#         encrypt(plain_text=input_text, cipher_shift=shift_amount)
#     else:
#         decrypt(cipher_text=input_text, reverse_shift=shift_amount)

# def encrypt(plain_text, cipher_shift):

#     cipher_text = ""

#     for char in plain_text:
#         if char == ' ':
#             cipher_text += ' '
#         else:
#             target_index = alphabet.index(char) + cipher_shift
#             if target_index > len(alphabet) - 1:
#                 target_index = target_index - len(alphabet)
#             cipher_text += ''.join(alphabet[target_index])
    
#     print(f"The encoded text is:\n{cipher_text}")

# def decrypt(cipher_text, reverse_shift):
    
#     plain_text = ""

#     for char in cipher_text:
#         if char == ' ':
#             plain_text += ' '
#         else:
#             target_index = alphabet.index(char) - reverse_shift
#             if target_index < 0:
#                 target_index = target_index + len(alphabet)
#             plain_text += ''.join(alphabet[target_index])

#     print(f"The plain text is:\n{plain_text}")