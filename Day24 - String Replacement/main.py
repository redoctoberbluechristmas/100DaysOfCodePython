
PLACEHOLDER = "[name]"

with open("Input/Names/invited_names.txt", mode="r") as names_file:
    names = names_file.readlines()


with open("Input/Letters/starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()
    for name in names:
        name = name.strip('\n')
        new_letter = letter_contents.replace(PLACEHOLDER, name)
        with open(f"Output/ReadyToSend/{name}.txt", mode="w") as out_file:
            out_file.write(new_letter)
        #with open(f"Output/ReadyToSend/{name}.txt", mode="w") as out_file:
            #out_file.write(letter_contents.replace(PLACEHOLDER, name))
