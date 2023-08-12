from art import logo,vs
from game_data import data
import random
from replit import clear


def random_element():
  """Return a random element from the list"""
  element = random.choice(data)
  return element


def compare(guess,follower_in_a,follower_in_b):
  if follower_in_a > follower_in_b:
    if guess == "a":
      return True
    else:
      return False
  elif follower_in_b > follower_in_a:
    if guess == "b":
      return True
    else:
      return False


score = 0


choice_b = random_element()

game_continue = True

print(logo)
while game_continue:
  
  choice_a = choice_b
  
  choice_b = random_element()
  while choice_a == choice_b:
    choice_b = random_element()
    
  print(f'Compare A: {choice_a["name"]}, {choice_a["description"]}, from {choice_a["country"]}.')
  
  
  print(vs)
  
  print(f'Against B: {choice_b["name"]}, {choice_b["description"]}, from {choice_b["country"]}.')
  
  # follow count
  followon_a = choice_a["follower_count"]
  followon_b = choice_b["follower_count"]
  # print(choice_a["follower_count"])
  # print(choice_b["follower_count"])
  
  guess = input("Who has more followers? Type 'A' or 'B':").lower()

  clear()
  print(logo)
  if compare(guess,followon_a,followon_b):
    score+=1
    
    
    print(f"You're right! Current score: {score}.")
    
  else:
    
    print(f"Sorry, that's wrong. Final score: {score}.")
    game_continue = False
