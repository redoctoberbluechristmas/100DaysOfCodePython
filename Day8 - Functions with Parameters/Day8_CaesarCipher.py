from cipherfunctions import encrypt, decrypt

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

if direction == "encode":
    encrypt(plain_text=text, cipher_shift=shift)
else:
    decrypt(cipher_text=text, reverse_shift=shift)