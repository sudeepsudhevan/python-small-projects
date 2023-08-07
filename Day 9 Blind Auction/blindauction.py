from replit import clear
#HINT: You can call clear() to clear the output in the console.
def find_highest_bidder(bidding_record):
  # bidding_record = {'sudeep': 100, 'da': 230}
  highest_bid = 0
  winner = ""
  print(bidding_record)
  for bidder in bidding_record:
    bid_amount = bidding_record[bidder]
    if bid_amount > highest_bid:
      highest_bid = bid_amount
      winner = bidder
  

  print(f"The winner is {winner} with a bid of ${highest_bid}.")
    
  
from art import logo
print(logo)

print("Welcome to the secret auction program.")

bid_again = True
bids = {}
while bid_again:
  
  name = input("What is your name?: ")
  price = int(input("What's your bid?: $"))
  bids[name] = price
  # print(bids)
  
  type = input("Are there any other bidders? Type 'yes' or 'no'.\n")
  
  if type == 'no':
    bid_again = False
    find_highest_bidder(bids)
  elif type == 'yes':
    clear()
