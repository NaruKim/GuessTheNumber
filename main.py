import art
import random

print(art.logo)

the_number=random.randint(1,100)
answer=False

difficulty=input("Welcome to Guess the number game.\nGuess the number between 1 to 100.\nType 'easy' or 'hard': ")

if difficulty=='easy':
  attempt=10
else:
  attempt=5

print(f"You have {attempt} attempts")
print(the_number)

while attempt>0 and answer==False:
  user=int(input("You guess: "))
  if user==the_number:
    answer=True
  elif user>the_number:
    print("Too high")
  else:
    print("Too low")
  attempt-=1
  if answer==False:
    print(f"You have {attempt} attempts")

if answer==True:
  print(f"The answer is {the_number}. You win")
else:
  print("You have no attempt. You lost")