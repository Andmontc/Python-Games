import random

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

images = [rock, paper, scissors]
user = int(input("Select 0. for rock, 1. for paper, 2. for scissors\n"))
if user < 0 or user > 2:
    print('Invalid option, You loose')
else:
    print(f'You choose {images[user]}')
    pc = random.randint(0, 2)
    print(f'Computer choose {images[pc]}')
    if user == 0 and pc == 2:
        print('You win')
    elif user == 0 and pc == 1:
        print('You lose')
    elif user == 1 and pc == 0:
        print('You win')
    elif user == 1 and pc == 2:
        print('You lose')
    elif user == 2 and pc == 1:
        print('You win')
    elif user == 2 and pc == 0:
        print('You lose')
    else:
        print('It\'s a Draw')
