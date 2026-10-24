import time
import random

totalvalue = 0

def singleplayer():
    global totalvalue
    global difficulty
    difficulty = input("Please select difficulty for computer. \n" \
    "1 - Easy" \
    "2 - Medium" \
    "3 - Hard")
    if difficulty == "1" or difficulty.lower == "easy":
        print("Easy difficulty selected.")
        difficulty = 1
    elif difficulty == "2" or difficulty.lower == "medium":
        print("Medium difficulty selected")
        difficulty = 2
    elif difficulty == "3" or difficulty.lower == "hard":
        print("Hard difficulty selected")
        difficulty = 3
    starplay = random.randint(1,2)
    if starplay == 1:
        print("Player 1 starts first")
        p1botgo()
    elif starplay == 2:
        print("Player 2 (Bot) starts first")
        p2botgo(difficulty)

def p1botgo():
    global totalvalue
    print(f"The current number is {totalvalue}")
    numsel = int(input("Which number would you like to choose? (1,2,3)\n"))
    if numsel > 3:
        print("Invalid number")
        p1botgo()
    elif numsel < 1:
        print("Invalid number")
        p1botgo()
    for i in range(numsel):
        totalvalue = totalvalue + 1
        print(totalvalue)
        if totalvalue == 21:
            print("Player 1 has lost! They got to 21. ")
            import main
            main.selections()
    p2botgo(difficulty)

def p2botgo(difficulty):
    global totalvalue
    print("Thinking.", end="\r")
    if difficulty == 1:
        if totalvalue > 15:
            numsel = 3
        elif totalvalue == 16:
            numsel = 1
        elif totalvalue == 17:
            numsel = 3
        elif totalvalue == 18:
            numsel = random.randint(1,2)
        elif totalvalue == 19:
            numsel = 1
        elif totalvalue == 20:
            numsel = 1
        else:
            print("Error. Defaulting to 1")
            numsel = 1
    elif difficulty == 2:
        if totalvalue > 15:
            numsel = 3
        elif totalvalue == 16:
            numsel = 2
        elif totalvalue == 17:
            numsel = 3
        elif totalvalue == 18:
            numsel = 2
        elif totalvalue == 19:
            numsel = 1
        elif totalvalue == 20:
            numsel = 1
    elif difficulty == 3:
        if totalvalue == 0:
            numsel = random.randint(1,3)
        elif totalvalue == 1:
            numsel = random.randint(1,3)
        elif totalvalue == 2:
            numsel = 3
        elif totalvalue == 3:
            numsel = 2
        elif totalvalue == 4:
            numsel = 1
        elif totalvalue == 5:
            numsel = random.randint(1,3)
        elif totalvalue == 6:
            numsel = 3
        elif totalvalue == 7:
            numsel = 2
        elif totalvalue == 8:
            numsel = 1
        elif totalvalue == 9:
            numsel = random.randint(1,3)
        elif totalvalue == 10:
            numsel = 3
        elif totalvalue == 11:
            numsel = 2
        elif totalvalue == 12:
            numsel = 1
        elif totalvalue == 13:
            numsel = random.randint(1,3)
        elif totalvalue == 14:
            numsel = 3
        elif totalvalue == 15:
            numsel = 2
        elif totalvalue == 16:
            numsel = 1
        elif totalvalue == 17:
            numsel = random.randint(1,3)
        elif totalvalue == 18:
            numsel = 3
        elif totalvalue == 19:
            numsel = 2
        elif totalvalue == 20:
            numsel = 1
        elif totalvalue == 21:
            numsel = 1
    print("Thinking..", end="\r")
    time.sleep(0.5)
    print("Thinking...", end="\r")
    print("Thinking....")
    for i in range(numsel):
            totalvalue = totalvalue + 1
            print(totalvalue)
            if totalvalue == 21:
                print("Player 2 has lost! They got to 21. ")
                import main
                main.selections()
    p1botgo()

def multiplayer():
    print("Multiplayer selected")
    starplay = random.randint(1,2)
    if starplay == 1:
        print("Player 1 starts first")
        p1go()
    elif starplay == 2:
        print("Player 2 starts first")
        p2go()

def p1go():
    global totalvalue
    print("Player 1's go...")
    print(f"The current number is {totalvalue}")
    numsel = int(input("Which number would you like to choose? (1,2,3)\n"))
    if numsel > 3:
        print("Invalid number")
        p1go()
    elif numsel < 1:
        print("Invalid number")
        p1go()
    for i in range(numsel):
        totalvalue = totalvalue + 1
        print(totalvalue)
        if totalvalue == 21:
            print("Player 1 has lost! They got to 21. ")
            import main
            main.selections()
    p2go()

def p2go():
    global totalvalue
    print("Player 2's go...")
    print(f"The current number is {totalvalue}")
    numsel = int(input("Which number would you like to choose? (1,2,3)\n"))
    if numsel > 3:
        print("Invalid number")
        p1botgo()
    elif numsel < 1:
        print("Invalid number")
        p1botgo()
    for i in range(numsel):
        totalvalue = totalvalue + 1
        print(totalvalue)
        if totalvalue == 21:
            print("Player 2 has lost! They got to 21. ")
            import main
            main.selections()
    p1go()

def start(players):
    print("Welcome to 21 (Nim). The aim of the game is to not be the one to get to 21.\nYou choose a number to increment between 1 2 or 3.")
    if players == 1:
        singleplayer()
    elif players == 2:
        multiplayer()
    else:
        print("error")    