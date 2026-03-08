
menu = {"espresso": {"water": 320, "milk" : 25, "coffee": 18 , "price": 1.5}
        , "latte": {"water": 200, "milk" : 20, "coffee": 24 , "price": 3.2 }
        , "cappucino": {"water": 250, "milk" : 15, "coffee": 20 , "price": 4.3 }
        }
def coin():
    penny = int(input("How many pannies : "))
    nickles = int(input("How many nikcles : "))
    dimes = int(input("How many dimes : "))
    quarters = int(input("How many quarters : "))
    total = penny * 1 + nickles * 5+ dimes * 10 + quarters * 25
    return total/100
resources = {"water":1000, "milk" : 150, "coffee": 200}
profits =0
machine_status = True
while machine_status:
     function = input("Enter Your Command espresso/Latte/Cappucino/others  :   ").lower()
     if function == "off":
       machine_status = False
     elif function == "report":
         print(f"Water = {resources['water']}")
         print(f"Sugar = {resources['milk']}")
         print(f"Coffe = {resources['coffee']}")
         print(f"Money =   {profits}")
     elif function == "espresso" or function == "latte" or function == "cappucino":
         drink = menu[function]
         if drink["water"] > resources["water"] or drink["milk"] > resources["milk"] or drink["coffee"] > resources["coffee"]:
               print("insufficient Resources")
         else:
             inserted_coins = coin()
             if inserted_coins < drink["price"]:
                 print(f"Money you added is not enough here is you change {inserted_coins} 💲")
             else:
                 print(f"Here is your change {inserted_coins- drink['price']} 💲 💸")
                 profits += drink["price"]
                 resources["water"] -= drink["water"]
                 resources["milk"] -= drink["milk"]
                 resources["coffee"] -= drink["coffee"]
                 print(f"enjoy Your {function}  ☕")
             
