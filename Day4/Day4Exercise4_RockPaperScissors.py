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

import random

player_choice = input("What do you choose? Rock, paper, or scissors?  ").lower()

print(player_choice)

if player_choice.startswith("r"):
  player_choice = 0
  print("You chose rock.")
  print(rock)
elif player_choice.startswith("p"):
  player_choice = 1
  print("You chose paper.")
  print(paper)
elif player_choice.startswith("s"):
  player_choice = 2
  print("You chose scissors.")
  print(scissors)
else:
  print("Please make a valid choice.")
  exit()

computer_choice = random.randint(0, 2)

if(computer_choice == 0):
  print("The computer chose rock.")
  print(rock)
elif(computer_choice == 1):
  print("The computer chose paper.")
  print(paper)
else:
  print("The computer chose scissors.")
  print(scissors)


if player_choice == 0 and computer_choice == 2:
  print("You win!")
elif player_choice > computer_choice:
  print("You win!")
elif player_choice == computer_choice:
  print("You tie.")
else:
  print("Computer wins.")