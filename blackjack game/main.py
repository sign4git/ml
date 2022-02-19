from replit import clear
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
import random
import art

while input("Do you want to continue? (answer y or n) ")=='y':
  clear()
  print(art.logo)
  busted=False
  dealer=[]
  user=[]
  game_stand=True
  dealer.append(random.choice(cards))
  user.append(random.choice(cards))
  current_card=random.choice(cards)
  if (current_card+sum(user))>21 and current_card==11:
    current_card=1
  user.append(current_card)
  print(f"user cards {user}. Current Score {sum(user)}")
  print(f"Computer's first card {sum(dealer)}")
  if sum(user)!=21:
    while busted==False and input("type y to draw another card n to pass: ")=='y':
      current_card=random.choice(cards)
      if (current_card+sum(user))>21 and current_card==11:
        current_card=1
      user.append(current_card)
      if sum(user)>21:
        print(f"user cards {user}. Current Score {sum(user)}")
        print(f"Computer's score {dealer}. Current Score {sum(dealer)}")
        print("Busted You Lose")
        busted=True
        game_stand=False
      print(f"user cards {user}. Current Score {sum(user)}")
      
  while game_stand:
    current_card=random.choice(cards)
    if (current_card+sum(dealer))>21 and current_card==11:
      current_card=1
    dealer.append(current_card)
    if sum(dealer)!=21:
      while sum(dealer)<17:
        current_card=random.choice(cards)
        if (current_card+sum(dealer))>21 and current_card==11:
          current_card=1
        dealer.append(current_card)
      if sum(dealer)>21:
        print(f"user cards {user}. Current Score {sum(user)}")
        print(f"Computer's score {dealer}. Current Score {sum(dealer)}")
        print("You Win")
        busted=True
        game_stand=False
    if busted==False:
      print(f"user cards {user}. Current Score {sum(user)}")
      print(f"Computer's score {dealer}. Current Score {sum(dealer)}")
      if sum(user)==sum(dealer):
        print("Draw")
      elif sum(user)>sum(dealer):
        print("You Win")
      else:
        print("You Lose")
      game_stand=False

