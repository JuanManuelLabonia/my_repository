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
# let the user choice
user_choice = input("What do you choose? Type 0 for ROCK, 1 for PAPER or 2 for SCISSORS. \n")

if int(user_choice) > 2 or int(user_choice) < 0:
    print("You typed an invalid number. You lose.")
# let the computer choice
elements = [rock, paper, scissors]
computer_choice = random.randint(0, 2)

final_move_USER = elements[int(user_choice)]
final_move_PC = elements[int(computer_choice)]

if final_move_USER == rock and final_move_PC == paper:
    print(f'{final_move_USER} \n Computer choose: \n {final_move_PC}')
    print("You lose")
    
elif final_move_PC == final_move_USER:
    print (f'{final_move_USER} \n Computer choose: \n {final_move_PC}')
    print("It's a draw")
    
elif final_move_USER == scissors and final_move_PC == rock:
    print(f'{final_move_USER} \n Computer choose: \n  {final_move_PC}')
    print("You lose")

elif final_move_USER == paper and final_move_PC == scissors:
    print(f'{final_move_USER} \n Computer choose: \n  {final_move_PC}')
    print("You lose")
else:
    print(f'{final_move_USER} \n Computer choose: \n  {final_move_PC}')
    print("You win")
    