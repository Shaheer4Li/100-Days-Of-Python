import random
Numbers = [11,2,3,4,5,6,7,8,9,10,10,10,10]
def deal(array):
    card = random.choice(array)
    return card
def score_calculator(arr):
    if sum(arr) == 21 and len(arr) ==2:
        return 0
    if sum(arr) > 21 and 11 in arr:
        arr.remove(11)
        arr.append(1)
    return sum(arr)
def compare(scor1,scor2):
    if scor2 == 0 or scor1 >21:
        return("dealer won😥")
    elif scor1 == scor2:
        return("its a tie😥")
    elif scor1 == 0 or scor2 >21:
        return("You win😁")
    else:
        if scor1>scor2:
            return("you win😁")
        else:
            return("Dealer won😥")
def main(Numbers): 
    print(r'''7
┌─────────┐  ┌─────────┐  ┌─────────┐  ┌─────────┐
│ A       │  │ K       │  │ Q       │  │ J       │
│         │  │         │  │         │  │         │
│    ♠    │  │    ♥    │  │    ♦    │  │    ♣    │
│         │  │         │  │         │  │         │
│       A │  │       K │  │       Q │  │       J │
└─────────┘  └─────────┘  └─────────┘  └─────────┘

██████╗ ██╗      █████╗  ██████╗██╗  ██╗     ██╗ █████╗  ██████╗██╗  ██╗
██╔══██╗██║     ██╔══██╗██╔════╝██║ ██╔╝     ██║██╔══██╗██╔════╝██║ ██╔╝
██████╔╝██║     ███████║██║     █████╔╝      ██║███████║██║     █████╔╝ 
██╔══██╗██║     ██╔══██║██║     ██╔═██╗ ██   ██║██╔══██║██║     ██╔═██╗ 
██████╔╝███████╗██║  ██║╚██████╗██║  ██╗╚█████╔╝██║  ██║╚██████╗██║  ██╗
╚═════╝ ╚══════╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝ ╚════╝ ╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝''')           
    user_card = []
    computer_card =[]
    c_score = -1
    game_status = False
    for i in range(2):
        user_card.append(deal(Numbers))
        computer_card.append(deal(Numbers))

    while not game_status:
        u_score= score_calculator(user_card)
        c_score= score_calculator(computer_card)
        print(f"|Your Cards {user_card} and total Score is {u_score}")
        print(f"|Dealer's card {computer_card[0]} ")
        if u_score == 0 or c_score == 0 or u_score > 21 or c_score >21 :
            print(f"user Score is {u_score}")
            print(f"dealer Score is {c_score}")
            print(compare(u_score,c_score))
            game_status = True
            continue
        hitorstand = input("Press 'H' If you want to hit or Press 's' if you want to stand ").lower()
        
        if hitorstand == "h":
            user_card.append(deal(Numbers))
        else:
            game_status = True
    while c_score != 0 and c_score< 17:
        computer_card.append(deal(Numbers))
        c_score= score_calculator(computer_card)
    u_score= score_calculator(user_card)
    c_score= score_calculator(computer_card)
    print(f"|Your Cards {user_card} and total Score is {u_score}")
    print(f"|Dealer's card {computer_card} ")
    print(compare(u_score, c_score))
    Playornot = input("Do yo want to play again: if yes press 'y' else anything   ").lower()
    if Playornot == "y":
        main(Numbers)
    else: return
main(Numbers)
