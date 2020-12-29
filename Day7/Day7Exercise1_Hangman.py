import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list = ["aardvark", "baboon", "camel"]
chosen_word = list(random.choice(word_list))

blanks_list = []
for i in range(len(chosen_word)):
    blanks_list += "_"

### Prompt player for letter ###

end_of_game = False

lives = 6

while not end_of_game:
    guess = input("Please guess a letter. ").lower()

    for i in range(len(chosen_word)):
        #letter = value at chosen_word[0], letter = value at chosen_word[1], etc.
        letter = chosen_word[i]
        if letter == guess:
            blanks_list[i] = letter

    if guess not in chosen_word:
        lives -= 1
        print(f"You have {lives} lives left")

    print(stages[lives])

    blanks_list_string = ""

    # for i in blanks_list:
    #     blanks_list_string += f" {i} "

    # print(f"The current panel is:\n {blanks_list_string}")

    print(f"{' '.join(blanks_list)}")

    if '_' not in blanks_list:
        end_of_game = True
        print("You win.")

    if lives == 0:
        end_of_game = True
        print("You lose.")