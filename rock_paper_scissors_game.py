import random

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
print("Welcome to Rock, Paper, Scissors Game")
player_move = int(input("What do you choose? Type 0 for Rock, 1 for Paper of 2 for Scissors: "))
computer_move = random.randint(0, 2)
print("You Choose")
if player_move == 0:
    print(rock)
elif player_move == 1:
    print(paper)
elif player_move == 2:
    print(scissors)
else:
    print("Invalid Input")

print("Computer choose: ")

if computer_move == 0:
    print(rock)
elif computer_move == 1:
    print(paper)
elif computer_move == 2:
    print(scissors)
else:
    print("Invalid Input")
if player_move == computer_move:
    print("Tie")
elif player_move == 0 and computer_move == 1:
    print("You Lose")
elif player_move == 0 and computer_move == 2:
    print("You win")
elif player_move == 1 and computer_move == 0:
    print("You win")
elif player_move == 1 and computer_move == 2:
    print("You lose")
elif player_move == 2 and computer_move == 0:
    print("You lose")
elif player_move == 2 and computer_move == 1:
    print("You win")