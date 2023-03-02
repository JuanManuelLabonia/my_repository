import art
import platform
import os


print(art.logo)
print("Welcome to the secret auction program.")


def clean():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")


bidders = []
more_bidders = True
while more_bidders == True:
    name = input("What is your name?: ")
    bid = input("What is your bid?: $")
    bidders.append({name: bid})
    keep_bidding = input('Are there any other bidders? Type "yes" or  "no". ')
    if keep_bidding == "no":
        more_bidders = False
    else:
        clean()


highest_bid = ""
position = 0
key_value = ""
for position in range(0, len(bidders)):
    for key in bidders[position]:
        if bidders[position][key] > highest_bid:
            highest_bid = bidders[position][key]
            key_value = key


print(f"The winner is {key_value} with a bid of ${highest_bid}")
