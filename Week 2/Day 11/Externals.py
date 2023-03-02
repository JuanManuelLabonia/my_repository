import random
import platform
import os
import time

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

deck = [1,2,3,4,5,6,7,8,9,10,10,10,10,
        1,2,3,4,5,6,7,8,9,10,10,10,10,
        1,2,3,4,5,6,7,8,9,10,10,10,10,
        1,2,3,4,5,6,7,8,9,10,10,10,10,
        1,2,3,4,5,6,7,8,9,10,10,10,10,
        1,2,3,4,5,6,7,8,9,10,10,10,10,
        1,2,3,4,5,6,7,8,9,10,10,10,10,
        1,2,3,4,5,6,7,8,9,10,10,10,10,        
        1,2,3,4,5,6,7,8,9,10,10,10,10,
        1,2,3,4,5,6,7,8,9,10,10,10,10,
        1,2,3,4,5,6,7,8,9,10,10,10,10,
        1,2,3,4,5,6,7,8,9,10,10,10,10,       
        1,2,3,4,5,6,7,8,9,10,10,10,10,
        1,2,3,4,5,6,7,8,9,10,10,10,10,
        1,2,3,4,5,6,7,8,9,10,10,10,10,
        1,2,3,4,5,6,7,8,9,10,10,10,10,       
        1,2,3,4,5,6,7,8,9,10,10,10,10,
        1,2,3,4,5,6,7,8,9,10,10,10,10,
        1,2,3,4,5,6,7,8,9,10,10,10,10,
        1,2,3,4,5,6,7,8,9,10,10,10,10,        
        1,2,3,4,5,6,7,8,9,10,10,10,10,
        1,2,3,4,5,6,7,8,9,10,10,10,10,
        1,2,3,4,5,6,7,8,9,10,10,10,10,
        1,2,3,4,5,6,7,8,9,10,10,10,10]


# User deck
hand = []
# Dealer deck
dealer = []
# Dealer deck just showing the first card
secret_dealer = []
# Stores True if user had ases, otherwise, stores False
hand_had_aces = False
# Stores True if Dealer had ases, otherwise, stores False
dealer_had_aces = False
# Stores player choice to play
stay_choice = ""


def start():
      """Gives the user a presentation befor playing"""
      print(logo)    
      first_deal()
      print (f"Dealer's hand: {secret_dealer} = {secret_dealer[0]}\nYour hand: {hand} = {hand_point_sum()}")


def loading_map():
      """This function is made up to simulate a loading part so as to improve UX/UI."""
      for i in range(1,random.randint(1, 4)):
            clean()
            print("Loading...")
            time.sleep(1.15)
            clean()
            print("Loading°..")
            time.sleep(1.15)
            clean()
            print("Loading.°.")
            time.sleep(1.15)
            clean()
            print("Loading..°")
            time.sleep(1.15)

def clean():
    """Cleans the terminal"""
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

def dealer_point_sum():
      """Sums all the dealer points in it's hand"""
      dealer_sum = 0
      for i in range(0, len(dealer)):
            dealer_sum += dealer[i]
      return dealer_sum
        
def hand_point_sum():
      """Sums all the points in the user hand"""
      hand_sum = 0
      for i in range(0, len(hand)):
            hand_sum += hand[i]
      return hand_sum


def change_1_for_10():
      """If user has an Ace, he can change it for 10 extra points according to the rules."""
      if 1 in hand:
            if hand_point_sum() + 10 <= 21:
                  hand.insert(hand.index(1), 11)
                  hand.remove(1)
                  print (f"You've got an ace! Your actual hand is: {hand}")
                  print (f"Dealer's hand: {secret_dealer} = {dealer_point_sum()}\nYour hand: {hand} = {hand_point_sum()}")
                  return True
                  
            elif 1 in dealer:
                  if dealer_point_sum() + 10 <= 21:
                        dealer.insert(dealer.index(1), 11)
                        dealer.remove(1)
                        clean()
                        print(logo)
                        print (f"Dealer got an ace! It's actual hand is {secret_dealer}")
                        if dealer[0] == 1:
                              secret_dealer.insert(0, 11)
                              secret_dealer.remove(1)
                        return True
            else:
                  return False
            
            
def change_10_for_1():
      """If either user or dealer had ases and got over 21, according to the rules, they can retake the As value they had before."""
      if 11 in hand and hand_had_aces == True:
            if hand_point_sum() + 11 > 21:
                  hand.insert(hand.index(11), 1)
                  hand.remove(11)
                  return False
            elif 10 in dealer and dealer_had_aces == True:
                  if dealer_point_sum() + 11 > 21:
                        dealer.insert(dealer.index(11), 1)
                        dealer.remove(11)
                        if dealer[0] == 1:
                              secret_dealer.remove(11)
                              secret_dealer.insert(0, 1)
                        return False
            else:
                  return False
            
            

def first_deal():
      """In order to not to change the probability deal. This function gives the first deal as if you were in a Casino."""
      hand.append(random.choice(deck))
      deck.remove(hand[-1])

      dealer.append(random.choice(deck))
      deck.remove(dealer[-1])

#The code below ensures user don't see the second card of the dealer while the dealer has two cards and doesn't change the probability.
      secret_dealer.append(dealer[-1])
      secret_dealer.append("x")    

      hand.append(random.choice(deck))
      deck.remove(hand[-1])

      dealer.append(random.choice(deck))
      deck.remove(dealer[-1])

def dealer_interaction():
      """Gives the dealer an interaction in order to play"""
      while dealer_point_sum() < hand_point_sum():
      
            if dealer_point_sum() <= 17 or dealer_point_sum() < hand_point_sum():
                  dealer.append(random.choice(deck))
                  deck.remove(dealer[-1])
                  change_1_for_10()
                  dealer_had_aces = change_1_for_10()
            elif dealer_point_sum() > 21 and dealer_had_aces == True:
                  change_10_for_1()
                  dealer_had_aces = change_10_for_1()

      return dealer_point_sum()

def win_lose():
      """Tells if the dealer won or lost against the user"""
      dealer_interaction()
      if hand_point_sum() == 21:
            dealer_interaction()
            if dealer_point_sum() == 21:
                  clean()
                  print(logo)
                  print (f"Dealer's hand: {dealer} = {dealer_point_sum()}\nYour hand: {hand} = {hand_point_sum()}")
                  print("Draw. Both, user and Dealer got 21")
                  restart()
            else:
                  clean()
                  print(logo)
                  print (f"Dealer's hand: {dealer} = {dealer_point_sum()}\nYour hand: {hand} = {hand_point_sum()}")
                  print("You've won!")
                  restart()
      elif stay_choice == "s":
            if hand_point_sum() > dealer_point_sum():
                        clean()
                        print(logo)
                        print (f"Dealer's hand: {dealer} = {dealer_point_sum()}\nYour hand: {hand} = {hand_point_sum()}")
                        print("You've won!")
                        restart()
            elif dealer_point_sum() > hand_point_sum() and dealer_point_sum() <= 21:
                  clean()
                  print(logo)
                  print (f"Dealer's hand: {dealer} = {dealer_point_sum()}\nYour hand: {hand} = {hand_point_sum()}")
                  print ("Dealer wins.")
                  restart()
            elif dealer_point_sum() > 21:
                  clean()
                  print(logo)
                  print (f"Dealer's hand: {dealer} = {dealer_point_sum()}\nYour hand: {hand} = {hand_point_sum()}")
                  print("You've won!")
                  restart()
            elif dealer_point_sum() == hand_point_sum():
                  clean()
                  print(logo)
                  print (f"Dealer's hand: {dealer} = {dealer_point_sum()}\nYour hand: {hand} = {hand_point_sum()}")
                  print(f"Draw. Both, user and Dealer got {dealer_point_sum()}")
                  restart()
            else:
                  return False

def recursivity():
      """The hole game development. It's in a function so as to ease the calling of it."""
      stay = False
      while not stay:
            hand_had_aces = False
            dealer_had_aces = False
            hand_had_aces = change_1_for_10()
            dealer_had_aces = change_1_for_10()
            if hand_had_aces == True or dealer_had_aces == True:
                  print (f"Dealer's hand: {secret_dealer} = {secret_dealer[0]}\nYour hand: {hand} = {hand_point_sum()}")
            stay_choice = input("Choose 's' to stand or 'h' to hit another card. ")
            if stay_choice != "s" and stay_choice != "h":
                  stay = False
            elif stay_choice == "h":
                  hand.append(random.choice(deck))
                  deck.remove(hand[-1])
                  hand_had_ases = change_1_for_10()
                  clean()
                  print(logo)
                  print (f"Dealer's hand: {secret_dealer} = {secret_dealer[0]}\nYour hand: {hand} = {hand_point_sum()}")
                  if hand_point_sum() > 21:
                              clean()
                              print(logo)
                              print (f"Dealer's hand: {dealer} = {dealer_point_sum()}\nYour hand: {hand} = {hand_point_sum()}")
                              print("Busted. You've lost.")
                              stay = True
                              restart()
                              stay = win_lose()
                  stay = win_lose()
            elif stay_choice == "s":
                  clean()
                  print(logo)
                  print (f"Dealer's hand: {dealer} = {dealer_point_sum()}\nYour hand: {hand} = {hand_point_sum()}")
                  dealer_interaction()
                  if hand_had_aces == True and hand_point_sum() > 21:
                        hand_had_aces = change_10_for_1()
                        if hand_had_aces:
                              change_10_for_1()
                              recursivity()
                        elif hand_point_sum() > 21:
                              clean()
                              print(logo)
                              print (f"Dealer's hand: {dealer} = {dealer_point_sum()}\nYour hand: {hand} = {hand_point_sum()}")
                              print("Busted. You've lost.")
                              stay = True   
                  elif dealer_point_sum() > hand_point_sum() and dealer_point_sum() <= 21:
                        clean()
                        print(logo)
                        print (f"Dealer's hand: {dealer} = {dealer_point_sum()}\nYour hand: {hand} = {hand_point_sum()}")
                        print ("Dealer wins.")
                        stay = True
                  elif hand_point_sum() == dealer_point_sum():
                        clean()
                        print(logo)
                        print (f"Dealer's hand: {dealer} = {dealer_point_sum()}\nYour hand: {hand} = {hand_point_sum()}")
                        print(f"Draw. Both, user and Dealer got {dealer_point_sum()}")
                        stay = True
                  else:
                        clean()
                        print(logo)
                        print (f"Dealer's hand: {dealer} = {dealer_point_sum()}\nYour hand: {hand} = {hand_point_sum()}")
                        print("You've won!")
                        stay = True

def restart():
      """Gives the user the oportunity to play again without having to quit the game."""
      wanna_restart = False
      while not wanna_restart:
            restart_question = input("Wanna play another? Please type 'y' or 'n'. ")
            if restart_question == "y":
                  clean()
            # hand = []
                  for i in range(0, len(hand)):
                        hand.pop()
                  for i in range(0, len(dealer)):
                        dealer.pop()
                  for i in range(0, len(secret_dealer)):
                        secret_dealer.pop()
                  start()
                  return False
                        
            elif restart_question == "n":
                  clean()
                  print(logo)
                  print("\t\t\tDon't worry, maybe later.")
                  return False
            else:
                  wanna_restart = True