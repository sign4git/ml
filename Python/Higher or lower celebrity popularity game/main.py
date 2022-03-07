import art
import game_data
import random
from replit import clear

score=0

def about_celebrities(celebrity_a,celebrity_b,score):
  clear()
  print(art.logo)
  if(score!=0):
    print(f"You're right. Current Score is {score}")
  print(f"Compare A: {celebrity_a['name']}, a {celebrity_a['description']}, from {celebrity_a['country']}")
  print(art.vs)
  print(f"Against B: {celebrity_b['name']}, a {celebrity_b['description']}, from {celebrity_b['country']}")


def get_random_celebrity(old_celebrity):
  duplicate_flag=True
  while duplicate_flag:
    celebrity=random.choice(game_data.data)
    if(not bool(old_celebrity)):
      celebrity=random.choice(game_data.data)
      return celebrity
    while duplicate_flag:
      celebrity=random.choice(game_data.data)
      if(old_celebrity["name"]!=celebrity["name"]):
        return celebrity
        
def compare_celebrities(celebrity_a,celebrity_b,score):
  while True:
    user_input=input("Who has more followers 'A' or 'B' : ")
    highest_follower=""
    if(celebrity_a["follower_count"]>celebrity_b["follower_count"]):
      highest_follower="A"
    else:
      highest_follower="B"
    if(user_input==highest_follower):
      score+=1
      clear()
      celebrity_a=celebrity_b
      celebrity_b=get_random_celebrity(celebrity_a)
      about_celebrities(celebrity_a,celebrity_b,score)
    else:
      print(f"Wrong Answer. Your final score is {score}")
      return

celebrity_a=get_random_celebrity({})
celebrity_b=get_random_celebrity(celebrity_a)
about_celebrities(celebrity_a, celebrity_b,score)
compare_celebrities(celebrity_a,celebrity_b,score)
