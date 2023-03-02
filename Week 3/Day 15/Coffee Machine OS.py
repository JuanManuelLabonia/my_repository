import main_menu


ingredients = main_menu.resources
money = 0


def coffe_choice_ingredients(choice):
    """Takes the user choice and returns in a bool whether if the order could be placed or there are not enough ingredients"""
    global ingredients
    feedback = ""
    for i in main_menu.MENU[choice]["ingredients"]:
        if main_menu.MENU[choice]["ingredients"][i] <= ingredients[i]:
            ingredients[i] -= main_menu.MENU[choice]["ingredients"][i]
            feedback = True
        else:
            feedback = False    
    return feedback


def coffe_missing_ingredients(choice):
    """Takes the user choice and returns in a which ingredient is missing"""
    global ingredients
    for i in main_menu.MENU[choice]["ingredients"]:
        if (main_menu.MENU[choice]["ingredients"][i] <= ingredients[i]) == False:
            return i


def check_payment(choice):
    """Checks if the user payed correctly"""
    global money
    cost = main_menu.MENU[choice]["cost"]
    print(f"The cost of your {choice} is ${cost}")
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    result = round(quarters*0.25 + nickles*0.05 + dimes*0.1 + pennies*0.01, 2)
    if result >= cost:
        if cost == result:
            money += cost
            print(f"Here is your {choice}. Enjoy!\nThe machine now has ${round(money, 2)}")
        elif result > cost:
            change = result - cost
            money += cost
            print(f"Here is your {choice}. Enjoy!\nYour change is ${round(change, 2)}")
    else:
        left = cost - result
        print(f"You've got {round(left, 2)} left. Money refunded.")
        print(f"The cost of your {choice} is ${cost}")

    

keep_working = True
while keep_working:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if choice == "report":
        print(f"Water: {ingredients['water']}ml\nMilk: {ingredients['milk']}ml\nCoffee: {ingredients['coffee']}g\nMoney: ${money}")
    elif choice == "espresso" or choice == "latte" or choice == "cappuccino":
        if coffe_choice_ingredients(choice):
            check_payment(choice)
        else:
            print(f"Not enough {coffe_missing_ingredients(choice)}. Please refill")
    elif choice == "refill":
        ingredients = {
                "water": 300,
                "milk": 200,
                "coffee": 100,}
        print("Refilled successfully")
    elif choice == "off":
        print("Goodbye folks.")
        keep_working = False





