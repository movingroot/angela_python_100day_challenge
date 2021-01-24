from replit import clear

import art
print(art.logo)
print("Welcome to the secret auction program.")

##### function #####
def bid_loop(_bidders) :
  name = input("What is your name? : ")
  bid = input("What is your bid? : ")

  _bidders[name] = int(bid[1:])

  others = input("Are there any other bidders? Type 'yes' or 'no' : ").lower()
  if others == "yes" :
    clear()
    bid_loop(_bidders)
  else :
    clear()
    winner = max(_bidders, key=_bidders.get)
    win_bid = max(_bidders.values())
    print(f"The winner is {winner} with a bid of ${win_bid}")

##### run #####
bidders = {}
bid_loop(bidders)
