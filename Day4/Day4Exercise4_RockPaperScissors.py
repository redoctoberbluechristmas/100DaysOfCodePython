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


if(player_choice == 0):
  if(computer_choice == 0):
    print("Tie.")
  elif(computer_choice == 1):
    print("Computer wins.")
  else:
    print("Player wins.")


if(player_choice == 1):
  if(computer_choice == 0):
    print("Player wins.")
  elif(computer_choice == 1):
    print("Tie.")
  else:
    print("Computer wins.")


if (player_choice == 2):
  if(computer_choice == 0):
    print("Computer wins.")
  elif(computer_choice == 1):
    print("Player wins.")
  else:
    print("Tie.")