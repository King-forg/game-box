# Main sequence

def selection():
    players = int(input("How many players? (1 or 2) \n"))
    selection = input("Select the game: \n"
        "1 - Naughts and Crosses \n")
    if selection == "1" or selection == "naughts and crosses":
        if players == 1 or players == 2:
            import naughtsandcrosses
            naughtsandcrosses.start(players)
        else:
            print("Error")
            selection()

def main():
    selection()

main()