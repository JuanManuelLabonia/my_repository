from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee = Menu()
can_make_coffee = CoffeeMaker()

money = MoneyMachine()


is_on = True
while is_on:
    choice = input(f"What coffee do you wanna drink? ({coffee.get_items()}): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        can_make_coffee.report() 
        money.report()
    elif coffee.find_drink(choice) != None:
        drink = coffee.find_drink(choice)
        if can_make_coffee.is_resource_sufficient(drink) and money.make_payment(drink.cost):
                can_make_coffee.make_coffee(drink)