# Main sequence

def selections():
    while True:
        print("Welcome to the game box!")
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
            "3 - 21 (Nim)\n"
            "4 - Blackjack\n"
            "5 - Connect 4\n"
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
                    if players == 1:
                        import blackjack
                        blackjack.start()
                    else:
                        print("Blackjack only supports 1 player")
        elif selection in ("5", "connect 4"):
                    if players <= 2:
                        import connect4
                        connect4.start(players)
                    else:
                         print("Connect 4 only supports up to 2 players")
        else:
            print("Please select game 1 or 2.")

def main():
    selections()

if __name__ == "__main__":
    main()