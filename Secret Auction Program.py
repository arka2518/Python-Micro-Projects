print("Welcome to Secret Auction Program")

bidders = {}
def Auction():
    more_bidders = True
    while more_bidders:
        name = input("What is your Name: ")
        bid = int(input("What is your bid: Rs"))
        bidders[name] = bid
    
        x = input("Are there any other bidders [yes or no]: ").lower()
        if x == "yes":
            print("\n" * 2)
            continue
        else:
            more_bidders = False

    highest_bid = 0
    winner = ""
    for bidder in bidders:
        current_bid = bidders[bidder]
        if current_bid > highest_bid:
            highest_bid = current_bid
            winner = bidder
    print(bidders)
    print(f"The Winner of our Auction is {winner}\nwho has won with the highest bid of Rs{highest_bid}")

Auction()



    
    