import random
import time
import os

score = 0

grid = [["" for _ in range(7)] for _ in range(6)]


def print_grid(board):
    print("  1   2   3   4   5   6   7")
    print("+---+---+---+---+---+---+---+")
    for row in board:
        print("| " + " | ".join(cell or " " for cell in row) + " |")
        print("+---+---+---+---+---+---+---+")

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def drop(c, player):
    if player == 1:
        token = "O"
    else:
        token = "X"
    if grid[0][c] != "":
        print("Full column... Retry")
        return False
    landing = 0
    for r in range(6):
        if grid[r][c] == "":
            landing = r
    for r in range(landing + 1):
        grid[r][c] = token
        clear_screen()
        print_grid(grid)
        time.sleep(0.12)
        if r != landing:
            grid[r][c] = ""
    return True

def place(col, player):
    validity = False
    while validity == False:
        if col == 1:
            validity = drop(0, player)
        elif col == 2:
            validity = drop(1, player)
        elif col == 3:
            validity = drop(2, player)
        elif col == 4:
            validity = drop(3, player)
        elif col == 5:
            validity = drop(4, player)
        elif col == 6:
            validity = drop(5, player)
        elif col == 7:
            validity = drop(6, player)   
        else:
            print("Invalid. Please retry")
        if validity == False:
            col = ask()

def ask():
    while True:
        try:
            return int(input("Where would you like to place a token?\n"))
        except ValueError:
            print("Invalid. Only numbers from 1-7 accepted.")

def checkwin(token):
    #across
    for r in range(6):
        for c in range(4):
            if grid[r][c] == token and grid [r][c+1] == token and grid[r][c+2] == token and grid[r][c+3] == token:
                return True
    #down
    for r in range(3):
        for c in range(7):
            if grid[r][c] == token and grid[r+1][c] == token and grid[r+2][c] == token and grid[r+3][c] == token:
                return True
    #diagonal down right
    for r in range(3):
        for c in range(4):
            if grid[r][c] == token and grid[r+1][c+1] == token and grid[r+2][c+2] == token and grid[r+3][c+3] == token:
                return True
    #diagonal down left
    for r in range(3):
        for c in range(3, 7):
            if grid[r][c] == token and grid[r+1][c-1] == token and grid[r+2][c-2] == token and grid[r+3][c-3] == token:
                return True
    return False

def board_full():
    for c in range(7):
        if grid[0][c] == "":
            return False
    return True

def p1go():
    print_grid(grid)
    print("Player 1... = O")
    selectp1 = ask()
    place(selectp1, 1)

def p2go():
    print_grid(grid)
    print("Player 2... = X")
    selectp2 = ask()
    place(selectp2, 2)

def computergo():
    print_grid(grid)
    print("Thinking.",end="\r")
    time.sleep(0.1)
    print("Thinking..",end="\r")
    time.sleep(0.1)
    print("Thinking...",end="\r")
    time.sleep(0.1)
    print("Thinking....")
    options = []
    for c in range(7):
        if grid[0][c] == "":
            options.append(c + 1)
    place(random.choice(options), 2)

def game(current, players):
    while True:
        if current == 1:
            p1go()
            token = "O"
        elif players == 1:
            computergo()
            token = "X"
        else:
            p2go()
            token = "X"

        if checkwin(token):
            clear_screen()
            print_grid(grid)
            if current == 2 and players == 1:
                print("Computer wins!")
                selection = input("Would you like to play again or return?\n y - Play again\n n - Return\n")
                if selection == "y":
                    continue
                else:
                    import main
                    main.selections()
            else:
                print("Player " + str(current) + " wins!")
                selection = input("Would you like to play again or return?\n y - Play again\n n - Return\n")
                if selection == "y":
                    continue
                else:
                    import main
                    main.selections()
            break

        if board_full():
            clear_screen()
            print_grid(grid)
            print("Its a draw!")
            selection = input("Would you like to play again or return?\n y - Play again\n n - Return\n")
            if selection == "y":
                continue
            else:
                import main
                main.selections()
            break

        if current == 1:
            current = 2
        else:
            current = 1

def multiplayer():
    starter = random.randint(1,2)
    if starter == 1:
        print("Player 1 starts")
    elif starter == 2:
        print("Player 2 starts")
    time.sleep(1)
    game(starter, 2)

def singleplayer():
    game(1, 1)
    
def start(players):
    print("Welcome to connect 4. The aim of the game is to get 4 of your tokens in a row.\n You are only allowed to place things in the columns and the fall down.")
    if players == 1 :
        singleplayer()
    elif players == 2:
        multiplayer()

start(int(input("1 or 2 players?\n")))