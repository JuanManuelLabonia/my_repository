from Art import logo
import os
import platform
import random

def clean():
    """Cleans the terminal"""
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

def random_num():
    """Chooses a random number between 1 and 100"""
    num = random.randint(1,100)
    return num

def game_start():
    """Cleans all and makes a pretty presentation to improve UX/UI"""
    clean()
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of an integer number between 1 and 100")
    difficulty = input("Please choose whether you wanna play easy 'e' or difficult 'd': ")
    if difficulty == "e":
        print("You have 10 attempts remaining to guess the number.")
        return 10
    elif difficulty == "d":
        print("You have 5 attempts remaining to guess the number.")
        return 5
    else: 
        game_start()


def game_logic():   
    """This function does the step by step of the game, looping in itself while player has lives"""   
    num = random_num()
    lives = game_start()
    while lives >= 1:
        Guess = int(input("Make a guess: "))
        if Guess == num:
            print("You've guessed it!")
            lives = -1
          
        elif lives == 1:
            print(f"You've lost, the number was {num}")
            lives = -1
            
        elif Guess > num:
            clean()
            print(logo)
            print("Too high, please try again")
            lives -= 1
            print(f"You have {lives} attempts remaining to guess the number.")

        elif Guess < num:
            clean()
            print(logo)
            print("Too low, please try again")
            lives -= 1
            print(f"You have {lives} attempts remaining to guess the number.")
    
game_logic()
    
def restart():
    """Restarts the game if the user wants it"""
    another_game = input("Wanna play another? Please type 'y' or 'n'. ")
    if another_game == "y":
        game_logic()
        restart()        

restart()
    
    
