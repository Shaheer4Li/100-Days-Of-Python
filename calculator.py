def add(n1,n2):
    return n1+n2
def sub(n1,n2):
    return n1-n2
def mul(n1,n2):
    return n1*n2
def div(n1,n2):
    return n1/n2
Calcultaion = {"+": add,
                "-": sub,
                "*": mul,
                "/": div
                }
def open():
    print(r''' 
        _____________________
        |  _________________  |   
        | | shaheer      0. | |
        | |_________________| |
        |  ___ ___ ___   ___  |
        | | 7 | 8 | 9 | | + | |
        | |___|___|___| |___| |
        | | 4 | 5 | 6 | | - | |
        | |___|___|___| |___| |
        | | 1 | 2 | 3 | | x | |
        | |___|___|___| |___| |
        | | . | 0 | = | | / | |
        | |___|___|___| |___| |
        |_____________________|
''')
    print("===============Welcome to Calculator program======================")
    First_number = float(input("Enter First Number = "))
    main(First_number)
def main (number):  
    sign = input("Enter Operator * , + , - , /  ")
    Second_number = float(input("Enter Second Number = "))
    if sign not in Calcultaion:
        print("syntax Error")
        main(number)
    number = Calcultaion[sign](number,Second_number)
    new_or_prev = input(f"For performing calculation on result {number} type yes or For starting new type anything rather than yes:   ").lower()
    if new_or_prev == "yes":
        main(number)
    else:
        print("\n"*20)
        open()

open()