from art import logo

print(logo)

bids = {}
bidding_finish = False


def find_the_higgest_bidder(bidding_record):
    higest_bid = 0
    winner = ""
    # bidding record = ("Angela": 123, "James"; 1000)
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > higest_bid:
            higest_bid = bid_amount
            winner = bidder

    print(f"The winner is {winner} with a bid of {higest_bid}")


while not bidding_finish:
    name = input("what is your name?")
    price = int(input("what is your bid? $"))
    bids[name] = price
    should_continue = input("Are there any other bidders? Type 'yes', 'no'")
    if should_continue == "no":
        bidding_finish = True
        find_the_higgest_bidder(bids)
