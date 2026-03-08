from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
Item = Menu()
maker = CoffeeMaker()
profit = MoneyMachine()
machine_staus = True
while machine_staus:
    function = input(f"What do you want to order {Item.get_items()}  : ").lower()
    if function == "off":
        machine_staus = False
    elif function == "report":
        maker.report()
        profit.report()
    else:
        drink = Item.find_drink(function)
        enough_resource = maker.is_resource_sufficient(drink=drink)
        if enough_resource:
            money = profit.make_payment(drink.cost)
            if money:
                maker.make_coffee(drink)



