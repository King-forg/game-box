# Main sequence

def selections():
    while True:
        try:
            players = int(input("How many players?\n"))
        except ValueError:
            print("Please enter 1 or 2.")
            continue

        selection = input(
            "Select the game: \n"
            "Num    Name\n"
            "1 - Naughts and Crosses\n"
            "2 - Higher or lower\n"
            "3 - 21\n"
            "4 - Blackjack\n"
        ).strip().lower()

        if selection in ("1", "naughts and crosses"):
            if players in (1, 2):
                import naughtsandcrosses
                naughtsandcrosses.start(players)
            else:
                print("Naughts and crosses supports 1 or 2 players.")
        elif selection in ("2", "higher or lower"):
            if players == 1:
                import higherorlower
                higherorlower.main()
            else:
                print("Higher or lower supports 1 player.")
        elif selection in ("3", "21"):
            if players <= 2:
                import twentyone
                twentyone.start(players)
            else:
                print("21 only supports 1 or 2 players")
        elif selection in ("4", "blackjack"):
                    if players <= 4:
                        import blackjack
                        blackjack.start()
                    else:
                        print("Blackjack only supports up to 4 players")
        else:
            print("Please select game 1 or 2.")

def main():
    selections()

if __name__ == "__main__":
    main()