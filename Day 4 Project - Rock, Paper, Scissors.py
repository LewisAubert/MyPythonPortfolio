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

# Write your code below this line 👇

import random

my_choice = int(input("Type 0 for Rock, 1 for Paper or 2 for Scissors\n"))
if my_choice >= 3 or my_choice < 0:
  print("You lose. Unlucky.")
elif my_choice == 0:
  print(rock)
elif my_choice == 1:
  print(paper)
elif my_choice == 2:
  print(scissors)

options = [rock, paper, scissors]

computer_choice = random.randint(0,2)
print(options[computer_choice])

if my_choice == computer_choice:
  print("It's a draw!")
elif my_choice == 0 and computer_choice == 2:
  print("You win!")
elif my_choice == 0 and computer_choice == 1:
  print("You lose!")
elif my_choice == 1 and computer_choice == 0:
  print("You win!")
elif my_choice == 1 and computer_choice == 2:
  print("You lose!")
elif my_choice == 2 and computer_choice == 0:
  print("You lose!")
elif my_choice == 2 and computer_choice == 1:
  print("You win!")
elif my_choice >= 3 or my_choice < 0:
  print("You lose. Unlucky.")