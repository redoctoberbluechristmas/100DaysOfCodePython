alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
    ]

def caesar2(start_text, shift_amount, cipher_direction):
    output_text = ""
    for char in start_text:
        start_index = alphabet.index(char)
        if cipher_direction == "decode":
            shift_amount += -1
        end_index = start_index + shift_amount
        output_text += alphabet[end_index]
    print(f"The {cipher_direction}d text is {output_text}.")