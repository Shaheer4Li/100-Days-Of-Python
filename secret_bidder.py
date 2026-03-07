def highest_check(Bidding_dictionary):
    highest = 0
    winner =""
    for bidder in Bidding_dictionary:
        current_bid = Bidding_dictionary[bidder]
        if current_bid > highest:
            highest = current_bid
            winner = bidder
    print(f"Hisgest Bid has been made by {winner} of Amount {highest}$")



bids = {}
To_continue = True

print(r'''

                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\
                         `'-------'`
                       .-------------.
                      /_______________\


''')
print("==================Welcome To ecret Biddder================")
while To_continue:
    name = input("Enter bidder's Name   ")
    bid = int(input("Enter Bid Aount : $"))
    bids[name]=bid
    status = input("Are there anymore bidder : (yes/no)  ").lower()
    if status == "no":
        To_continue = False
        highest_check(bids)
    elif status =="yes":
        To_continue = True
    else: 
        
        print("enter Right Value yes or no next time")
        status = input("Are there anymore bidder : (yes/no)  ").lower()





    