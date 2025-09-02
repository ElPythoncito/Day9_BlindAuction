from art import logo

print(logo)
users = {}
game_over = False


def bidders():
    name = input("What's your name? ")
    price = int(input("What's your bid? $"))
    users[name] = price

    another_user = input("Are there any other bidders? Type 'yes' or 'no': ").lower()
    print("\n" * 50)
    return another_user


# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added

while not game_over:
    again = bidders()

    if again == "yes":
        bidders()
    else:
        game_over = True

# TODO-4: Compare bids in dictionary
winner_user = ""
max_bid_user = 0

for user in users:
    bid_user = users[user]

    if bid_user > max_bid_user:
        max_bid_user = bid_user
        winner_user = user
    else:
        pass

print(f"The winner is {winner_user} with a bid of ${max_bid_user}🎊🎊🎊.")

input("\n\nType 'ENTER' to finish!!!")
