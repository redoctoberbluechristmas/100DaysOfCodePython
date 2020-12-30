alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
    ]

def caesar(start_text, shift_amount, cipher_direction):
    output_text = ""
    

    # Will divide the shift amount to fit into length of alphabet.
    shift_amount = shift_amount % 26
    
    if cipher_direction == "decode":
        shift_amount *= -1
    for char in start_text:
        start_index = alphabet.index(char)
        end_index = start_index + shift_amount
        output_text += alphabet[end_index]
    print(f"The {cipher_direction}d text is {output_text}.")