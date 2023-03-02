import art
import game_data
import random
import os
import platform

def clean():
    """Cleans the terminal"""
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

a = random.choice(game_data.data)

def choose_b(a):
    """Chooses B and ensures it's different from the A chosen."""
    b = random.choice(game_data.data)
    while b["name"] == a:
        b = random.choice(game_data.data)
    return b

def extract_info_from_dict(dict):
    """Cleans the dictionary and prepares it for a more comfortable manipulation"""
    info_extracted_from_dict = []
    for position_of_info in dict:
        info_extracted_from_dict.append(dict[position_of_info])
    return info_extracted_from_dict
    
def compare(a, b):
    """Compares between A and B"""
    if a > b:
        return "A"
    else:
        return "B"
    
    
def main_game():
    global a
    extracted_a = extract_info_from_dict(a)
    extracted_b = extract_info_from_dict(choose_b(extracted_a[0]))
    game_continues = True
    score = 0
    print(art.logo)
    while game_continues:
        print(f"\nCompare A: {extracted_a[0]}, a {extracted_a[2]}, from {extracted_a[3]}.")
        print(art.vs)
        print(f"\nAgainst B: {extracted_b[0]}, a {extracted_b[2]}, from {extracted_b[3]}.")
        answer = compare(extracted_a[1],extracted_b[1]).lower()
        choice = input("\nWho has more followers? Type 'A' or 'B': ").lower()
        if choice == answer:
            score += 1
            clean()
            print(art.logo)
            print(f"You're rigth! Current score: {score}")
            extracted_a = extracted_b
            extracted_b = extract_info_from_dict(choose_b(extracted_a[0]))
        else:
            clean()
            print(art.logo)
            print(f"Sorry, that's wrong. Final score: {score}")
            game_continues = False
            
main_game()