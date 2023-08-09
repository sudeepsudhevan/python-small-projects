import random
from art import logo
from replit import clear


def calculate_score(cards):
  """Take a list of cards and return the score calculated from card"""
  if sum(cards) == 21 and len(cards) == 2:
    return 0
  if 11 in cards and sum(cards) > 21:
    cards.remove(11)
    cards.append(1)
  return sum(cards)
# print(calculate_score([11,3,8]))

def deal_card():
  """Return a random card"""
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card

def compare(user_score, computer_score):
  """Check the result by comparing user_score and computer_score"""
  if (user_score == 0 and computer_score == 0):
    return "you lose"
  elif computer_score == 0:
    return "Lose, opponent has Blackjack 😱"
  elif user_score == 0:
    return "Win with a Blackjack 😎"
  elif (user_score == computer_score):
    return "it's a draw 🤪🤭"
  elif user_score > 21:
    return "You went over. You lose 😤"  
  elif computer_score > 21:
    return "Opponent went over. You win 😁"
  elif user_score > computer_score:
    return "you win 😆"
  else:
    return "you lose 😤"


def play_game():
  print(logo)
  user_choice = []
  computer_choice = []
  is_game_over = False


  for _ in range(2):
    user_choice.append(deal_card())
    computer_choice.append(deal_card())
  
  
  
  while not is_game_over:
  
    user_score = calculate_score(user_choice)
    computer_score = calculate_score(computer_choice)
    
    print(f"  Your cards: {user_choice}, current score: {user_score}")
    print(f"  Computer's first card: {computer_choice[0]}")
    
    if user_score == 0 or computer_score == 0 or user_score > 21:
      is_game_over = True
    else:
      type = input("Type 'y' to get another card, type 'n' to pass: ")
      if type == "y":
         user_choice.append(deal_card())  
      else:
        is_game_over = True
        
        
  while computer_score < 17 and computer_score !=0:
    computer_choice.append(deal_card())
    computer_score = calculate_score(computer_choice)
  
  print(f"Your final hand: {user_choice}, final score: {user_score}")
  print(f"  Computer's final hand: {computer_choice}, final score: {computer_score}")
    
  print(compare(user_score,computer_score))  

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
  clear()
  play_game()
