#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
import random
import art
print(art.logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
num_list=list(range(1,101))
random_number=random.choice(num_list)
level=input("Choose difficulty level(Type 'easy' or 'hard'): ")
if level=="hard":
  attempts=5
elif level=="easy":
  attempts=10

while attempts>0:
  print(f"You have {attempts} attempts to guess the number.")
  guess=int(input("Make a guess: "))
  if guess==random_number:
    print(f"You got it! The answer was {random_number}")
    attempts=-1
  elif guess<random_number:
    print("Too Low.")
    attempts-=1
  else:
    print("Too High.")
    attempts-=1
    
if attempts==0:
  print("You ran out of guesses. You Lose")