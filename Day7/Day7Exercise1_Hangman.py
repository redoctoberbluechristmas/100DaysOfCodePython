import random
import hangman_art
import hangman_wordlist


print(hangman_art.logo)

chosen_word = list(random.choice(hangman_wordlist.word_list))

blanks_list = []
for letter in chosen_word:
    blanks_list += "_"

lives = 6

previous_guesses = []

end_of_game = False

while not end_of_game:
    guess = input("Please guess a letter. ").lower()

    if guess in previous_guesses:
        print(f"You already chose that.\nSo far, you have chosen: {', '.join(previous_guesses)}.")
        print(f"{' '.join(blanks_list)}")

    else:
        for i in range(len(chosen_word)):
            letter = chosen_word[i]
            if letter == guess:
                blanks_list[i] = letter
                previous_guesses += guess

        if guess not in chosen_word:
            lives -= 1
            previous_guesses += guess
            print(f"Your choice, {guess}, is not in the word.\nSo far, you have chosen: {', '.join(previous_guesses)}")
            print(f"You have {lives} lives left")

        print(hangman_art.stages[lives])

        # blanks_list_string = ""

        # for i in blanks_list:
        #     blanks_list_string += f" {i} "

        # print(f"The current panel is:\n {blanks_list_string}")

        print(f"The current panel is:\n {' '.join(blanks_list) }")

        if '_' not in blanks_list:
            end_of_game = True
            print("You win.")

        if lives == 0:
            end_of_game = True
            print("You lose.")
            print(f"The word was {chosen_word}")