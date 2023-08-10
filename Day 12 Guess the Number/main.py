from art import logo
import random

print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
actual_number = random.randint(1,100)

print(f"Pssst, the correct answer is {actual_number}")

difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

if difficulty == "easy":
  attempt = 10
else:
  attempt = 5

def compare(actual_number,guess_number,attempt):
  if actual_number == guess_number:
    print(f"You got it! The answer was {actual_number}.")
    return 0
  elif actual_number > guess_number:
    print("Too low")
    return attempt - 1
  else:
    print("Too high")
    return attempt - 1


while not attempt == 0:
  print(f"You have {attempt} attempts remaining to guess the number.")
  guess_number = int(input("Make a guess: "))
  attempt = compare(actual_number,guess_number,attempt)
  if attempt != 0:
    print("Guess Again")


if attempt == 0 and guess_number != actual_number:
  print("You've run out of guesses, you lose.")
