cards = ["","","","","","","","","","","","","","","","","","","","","","","","","","",""]

def start():
    global budget
    budget = int(input("Welcome to blackjack. Please state your budget."))
    proceed = input(f"Are you sure you want to set your budget at {budget}?")
    if proceed == "no":
        import main
        main.selections()
    else:
        print("")
    selection(1)

def selection(stage):
    if stage == 1:
        select = input("What would you like to do?" \
                    "--------------------------" \
                    "1 - Draw cards" \
                    "2 - Add budget" \
                    "3 - Subtract budget" \
                    "4 - Exit")
        if select == 1:
            drawcards()
        elif select == 2:
            budgets(add)
        elif select == 3:
            budgets(subt)
        elif select == 4:
            import main
            main.selections()
        else:
            print("Error, please retry")
            selection(1)
    elif stage == 2:
        print("What would you like to do?" \
              "--------------------------" \
             f" Budget: {budget}")
        for i in len(cards):
             print(f" Cards : {cards[i]}")
        print("-------------------------" \
              "1 - Stick" \
              "2 - Twist" \
              "3 - ")