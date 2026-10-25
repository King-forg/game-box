import random
import time

def start(players):
    s1 = 0
    s2 = 0
    if players == 1:
        singleplayer(s1, s2)

def singleplayer(s1, s2):
    print("Starting rock paper scissors game....")
    time.sleep(0.4)
    print("Rules: Rock beats scissors, Scissors beats paper and paper beats rock.")
    time.sleep(0.2)
    print("Starting game...")
    playagain = ""
    game(s1, s2, playagain)

def game(s1, s2, playagain):
    print(f"The score for you is {s1}\nThe score for the bot is {s2}")
    time.sleep(0.7)
    print("Rock")
    time.sleep(0.3)
    print("Paper")
    time.sleep(0.3)
    print("Scissors")
    time.sleep(0.3)
    selection = input("Rock paper or scissors? (R/P/S)\n")
    selection = selection.lower()
    if selection == "quit":
        return
    while selection not in ("r","p","s","R","P","S"):
        selection = input("Rock paper or scissors? (R/P/S)\n")
        selection = selection.lower()
        if selection == "quit":
            return
    botselection = random.randint(1,3)
    if botselection == 1:
        botselection = "r"
    elif botselection == 2:
        botselection = "p"
    elif botselection == 3:
        botselection = "s"
    else:
        print("Internal error line 32")

    if selection == "r":
        fullname = "rock"
    elif selection == "p":
        fullname = "paper"
    elif selection == "s":
        fullname = "scissors"

    if botselection == "r":
        botfullname = "rock"
    elif botselection == "p":
        botfullname = "paper"
    elif botselection == "s":
        botfullname = "scissors"

    time.sleep(0.5)

    if selection == botselection: 
        print("Draw. Select again.")
        game(s1, s2, playagain)
    elif selection == "r" and botselection == "p":
        print(f"Bot wins!\nBot had {botfullname} and you had {fullname}")
        s2 = s2 + 1
    elif selection == "r" and botselection == "s":
        print(f"You win!\nBot had {botfullname} and you had {fullname}")
        s1 = s1 + 1
    elif selection == "p" and botselection == "r":
        print(f"You win!\nBot had {botfullname} and you had {fullname}")
        s1 = s1 + 1
    elif selection == "p" and botselection == "s":
        print(f"Bot wins!\nBot had {botfullname} and you had {fullname}")
        s2 = s2 + 1
    elif selection == "s" and botselection == "r":
        print(f"Bot wins!\nBot had {botfullname} and you had {fullname}")
        s2 = s2 + 1
    elif selection == "s" and botselection == "p":
        print(f"You win!\nBot had {botfullname} and you had {fullname}")
        s1 = s1 + 1
    else:
        print("Internal error line 64")
    time.sleep(0.8)
    print(f"The score for you is {s1}\nThe score for the bot is {s2}")
    time.sleep(0.5)
    if playagain == "":
        playagain = input("Would you like another round or end the game?\n y - Another round\n n - End game and quit\n r - keep repeating game non stop\n")
        playagain = playagain.lower()
    if playagain == "r":
        game(s1, s2, playagain)
    elif playagain == "y":
        print("Ok then doing another round!")
        time.sleep(2)
        game(s1, s2, playagain)
    elif playagain == "n":
        return
    