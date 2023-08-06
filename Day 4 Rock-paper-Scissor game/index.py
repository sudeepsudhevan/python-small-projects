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

#Write your code below this line 👇
import random
choice  = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

game_choice = [rock, paper, scissors]

if choice > 2 or choice < 0:
  print("wrong choice, please play by rule")
else:
  print(game_choice[choice])

# if choice == 0:
#   print(rock)
# elif choice == 1:
#   print(paper)
# elif choice == 2:
#   print(scissors)
# else:
#   print("wrong choice, please play by rule")
  
print("Computer chose:")

computer_choice = random.randint(0,2)

print(game_choice[computer_choice])

# if computer_choice == 0:
#   print(rock)
# elif computer_choice == 1:
#   print(paper)
# else:
#   print(scissors)

if choice == computer_choice:
  print("That is a draw!!")
elif (choice == 0 and computer_choice == 2) or (choice == 1 and computer_choice == 0) or (choice == 2 and computer_choice == 1):
  print("you win!")
else:
  print("you lose!")

