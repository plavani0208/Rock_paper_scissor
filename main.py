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
import random
choice = [rock, paper , scissors]

user = input("What do you choose? Type 0 for rock, 1 for paper or 2 for scissors.\n ")
user = int(user)

if(user == 0):
  print(choice[0])
elif (user == 1):
  print(choice[1])
else:
  print(choice[2])

res = random.randint(0,2)
print(f"Computer chose:\n {choice[res]}")

if(user==0 and res == 2):
  print("You win!🤑")
elif res==0 and user == 2:
  print("You lose!")
elif res == 1 and user == 2:
  print("You win!")
elif(res > user):
  print("You lose!🥺")
elif(user==res):
  print("Draw!🥵")
else:
  print("Error!You entered invalid number!Try again 😥")

