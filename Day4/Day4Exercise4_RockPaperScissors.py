rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
# Store a list of variables
game_images = [rock, paper, scissors]
import random

player_choice = input("What do you choose? Rock, paper, or scissors?  ").lower()

valid_choices = ["rock", "paper", "scissors"]

if player_choice not in valid_choices:
  print("Please enter a valid choice.")
else:
  print(f"You chose {player_choice}")
  player_choice = valid_choices.index(player_choice)
  print(game_images[player_choice])

  computer_choice = random.randint(0, 2)
  computer_choice_output = valid_choices[computer_choice]
  print(f"The computer chose {computer_choice_output}")
  print(game_images[computer_choice])

  if player_choice == 0 and computer_choice == 2:
    print("You win!")
  elif computer_choice == 0 and player_choice == 2:
    print("You lose!")
  elif player_choice > computer_choice:
    print("You win!")
  elif player_choice == computer_choice:
    print("You tie.")
  else:
    print("Computer wins.")