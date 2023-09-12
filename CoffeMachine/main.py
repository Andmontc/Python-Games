from coffee_maker import CoffeeMaker
from Menu import Menu
from money_machine import MoneyMachine


mmachine = MoneyMachine()
menu = Menu()
cmaker = CoffeeMaker()

is_on = True

while is_on:
    options = menu.get_items()
    choice = input(f"What would you like? {options} or Report to see the report/Off to turn off: ")
    if choice == "Off":
        is_on = False
    elif choice == "Report":
        cmaker.report()
        mmachine.report()
    else:
        drink = menu.find_drink(choice)
        if cmaker.is_resource_sufficient(drink) and mmachine.make_payment(drink.cost):
            cmaker.make_coffee(drink)
       