import random


cards = [["", "", ""], ["", "", ""]]
budget = 0
bet = 0
basebet = 0


def getnum(text):
    while True:
        try:
            return int(input(text))
        except ValueError:
            print("Please enter a number")


def cardtotal(hand):
    total = sum(hand)
    aces = hand.count(11)
    while total > 21 and aces:
        total -= 10
        aces -= 1
    return total


def gettotal():
    values = []
    for card in cards:
        if card[1] == "":
            break
        values.append(card[2])
    return cardtotal(values)


def newcard():
    value = random.randint(2, 11)
    if value == 11:
        name = "Ace"
    elif value == 10:
        name = random.choice((10, "Jack", "Queen", "King"))
    else:
        name = value
    symbol = random.choice(("Clubs", "Diamonds", "Hearts", "Spades"))
    return name, symbol, value


def start():
    global budget
    global bet
    global basebet

    print("Disclaimer - This uses virtual money with no value. This does not promote gambling with real money.")
    budget = getnum("Welcome to blackjack. Please state your budget.\n")
    while budget < 0:
        print("Budget cannot be negative")
        budget = getnum("Welcome to blackjack. Please state your budget.\n")

    proceed = input(f"Are you sure you want to set your budget at {budget}? (y/n)\n").lower()
    if proceed in ("n", "no"):
        import main
        main.selections()
        return

    while True:
        bet = getnum("What would you like your bet to be?\n")
        if bet <= 0 or bet > budget:
            print("Retry")
        else:
            basebet = bet
            print(f"Bet set as {bet}")
            break
    selection(1)


def cardsdrawn():
    return sum(1 for card in cards if card[1] != "")


def drawcards():
    card1name, card1symbol, card1 = newcard()
    card2name, card2symbol, card2 = newcard()
    return card1name, card1symbol, card2name, card2symbol, card1, card2


def budgets(action):
    global budget
    if action == "+":
        addbudget = getnum("How much would you like to add?\n")
        budget += addbudget
    elif action == "-":
        takebudget = getnum("How much would you like to take?\n")
        budget -= takebudget
    if budget < 0:
        budget = 0


def resetcards():
    global budget
    global bet
    del cards[2:]
    for card in cards:
        card[0] = ""
        card[1] = ""
        card[2] = ""
    bet = basebet
    if bet > budget:
        bet = budget


def hit():
    return newcard()


def dealer_total():
    dealer_cards = [random.randint(2, 11), random.randint(2, 11)]
    while cardtotal(dealer_cards) < 17:
        dealer_cards.append(random.randint(2, 11))
    return cardtotal(dealer_cards)


def finish_round():
    resetcards()


def stand():
    global budget
    global bet

    playertot = gettotal()
    dealertot = dealer_total()
    print(f"Your total is {playertot}\nDealers total is {dealertot}")
    if playertot > 21:
        print("You lost!")
        print(f"You lose {bet}")
        budget -= bet
    elif dealertot > 21:
        print("Dealer lost!")
        print(f"You get {bet}")
        budget += bet
    elif playertot > dealertot:
        print("You win!")
        print(f"You get {bet}")
        budget += bet
    elif playertot < dealertot:
        print("You lose!")
        print(f"You lose {bet}")
        budget -= bet
    else:
        print("Tie!")
    if budget < 0:
        budget = 0
    finish_round()
    return


def doudown():
    global budget
    global bet
    if bet * 2 > budget:
        print("Not enough budget to double down")
        return
    bet *= 2
    cn, cs, c = hit()
    cards.append([cn, cs, c])
    print(f"You drew the {cn} of {cs}")
    stand()


def playhand(handnum, hand):
    cn, cs, c = hit()
    hand.append(c)
    print(f"Hand {handnum} drew the {cn} of {cs}")
    while cardtotal(hand) < 21:
        print(f"Hand {handnum} total: {cardtotal(hand)}")
        choice = getnum("1 - Hit\n2 - Stand \n")
        if choice == 1:
            cn, cs, c = hit()
            hand.append(c)
            print(f"Hand {handnum} drew the {cn} of {cs}")
        elif choice == 2:
            break
        else:
            print("Error, please retry")
    return cardtotal(hand)


def split():
    global budget
    global bet
    if cardsdrawn() != 2 or cards[0][2] != cards[1][2]:
        print("You can only split if your 2 cards have the same value....")
        return
    elif bet * 2 > budget:
        print("Not enough budget to split")
        return
    else:
        hand1tot = playhand(1, [cards[0][2]])
        hand2tot = playhand(2, [cards[1][2]])
        dealertot = dealer_total()
        print(f"Dealers total is {dealertot}")
        for total in (hand1tot, hand2tot):
            if total > 21:
                print(f"A hand of {total} lost! you lose {bet}")
                budget -= bet
            elif dealertot > 21:
                print(f"Dealer lost. A hand of {total} wins {bet}")
                budget += bet
            elif total > dealertot:
                print(f"A hand of {total} wins! you get {bet}")
                budget += bet
            elif total < dealertot:
                print(f"A hand of {total} lost. you lose {bet}")
                budget -= bet
            else:
                print(f"A hand of {total} tied.")
        if budget < 0:
            budget = 0
        finish_round()


def surrender():
    global budget
    global bet
    loss = bet // 2
    print(f"You surrendered and lost {loss}")
    budget -= loss
    if budget < 0:
        budget = 0
    finish_round()


def play_round():
    while True:
        print(
            "What would you like to do?\n"
            "--------------------------\n"
            f" Budget: {budget}"
        )
        for card in cards:
            if card[1] == "":
                break
            print(f" Cards : {card[0]} of {card[1]}")
        print(f" Total : {gettotal()}")
        print(
            "-------------------------\n"
            "1 - Hit\n"
            "2 - Stand\n"
            "3 - Double Down\n"
            "4 - Split\n"
            "5 - Surrender\n"
        )
        s2select = getnum("Selection (Num) : ")
        if s2select == 1:
            cn, cs, c = hit()
            cards.append([cn, cs, c])
            print(f"You drew the {cn} of {cs}")
            if gettotal() > 21:
                stand()
                return
        elif s2select == 2:
            stand()
            return
        elif s2select == 3:
            doudown()
            if cardsdrawn() == 0:
                return
        elif s2select == 4:
            split()
            if cardsdrawn() == 0:
                return
        elif s2select == 5:
            surrender()
            return
        else:
            print("Error")


def selection(stage):
    global budget
    global bet

    if stage == 1:
        while True:
            select = getnum(
                "What would you like to do?\n"
                "--------------------------\n"
                "1 - Draw cards\n"
                "2 - Add budget\n"
                "3 - Subtract budget\n"
                "4 - Exit\n"
            )
            if select == 1:
                if bet <= 0 or bet > budget:
                    print("Your bet must be greater than zero and no more than your budget.")
                    continue
                c1n, c1s, c2n, c2s, c1, c2 = drawcards()
                print(f"You drew:\n The {c1n} of {c1s} \n And the {c2n} of {c2s}!")
                cards[0] = [c1n, c1s, c1]
                cards[1] = [c2n, c2s, c2]
                if gettotal() == 21:
                    print("Blackjack!")
                    budget += bet
                    finish_round()
                else:
                    play_round()
                continue
            if select == 2:
                budgets("+")
                continue
            if select == 3:
                budgets("-")
                continue
            if select == 4:
                import main
                main.selections()
                return
            print("Error, please retry")
    elif stage == 2:
        play_round()
