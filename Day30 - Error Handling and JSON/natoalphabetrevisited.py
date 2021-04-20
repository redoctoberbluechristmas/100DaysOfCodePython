import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

data_dict = {row.letter:row.code for (index, row) in data.iterrows()}


def nato_alphabet():
    user_input = input("Enter a word: ").upper()

    try:
        output_list = [data_dict[i] for i in user_input]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        nato_alphabet()
    else:
        print(output_list)

nato_alphabet()