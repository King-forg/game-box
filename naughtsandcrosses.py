#Naughts And Crosses game

import random

def start(players):
    if players == 1 or players == 2:
        print("Players = {players}")
    else:
        players = int(input("Number of players? (1/2)\n"))
    if players == 1:
        singleplayer()
    elif players == 2:
        multiplayer()
    else:
        print("Error")

def singleplayer():
    global grid
    print("Welcome to naughts and crosses.")
    grid = [[""],[""],[""]],[[""],[""],[""]],[[""],[""],[""]]
    for i in range(3):
        for j in range(3):
            grid[i][j] = "#"
    print("",grid[0][0],grid[0][1],grid[0][2],"\n",grid[1][0],grid[1][1],grid[1][2],"\n",grid[2][0],grid[2][1],grid[2][2])
    choice = random.randint(1,2)
    if choice == 1:
        print("You start first")
        singleplayerp1()
    elif choice == 2:
        print("Computer starts first")
        singleplayerp2()

def multiplayer():
    global grid
    print("Welcome to naughts and crosses.")
    grid = [[""],[""],[""]],[[""],[""],[""]],[[""],[""],[""]]
    for i in range(3):
        for j in range(3):
            grid[i][j] = "#"
    print("",grid[0][0],grid[0][1],grid[0][2],"\n",grid[1][0],grid[1][1],grid[1][2],"\n",grid[2][0],grid[2][1],grid[2][2])
    first = random.randint(1,2)
    if first == 1:
        print("Player 1 starts first")
        selectp1()
        loopp1()
    elif first == 2:
        print("Player 2 starts first")
        selectp2()
        loopp2()

def singleplayerp1():
    global grid
    print("",grid[0][0],grid[0][1],grid[0][2],"\n",grid[1][0],grid[1][1],grid[1][2],"\n",grid[2][0],grid[2][1],grid[2][2])
    selectionx = int(input("Please select first grid reference (1,3 of rows) \n"))
    selectiony = int(input("Please select second grid reference (1,3 of columns) \n"))
    placed = place(1, selectionx, selectiony)
    if placed == False:
        singleplayerp1()
    elif placed == True:
        if wintest():
            import main
            main.main()
        elif istie():
            import main
            print("It's a tie!")
            main.main()
        else:
            singleplayerp2()

def singleplayerp2():
    global grid
    print("",grid[0][0],grid[0][1],grid[0][2],"\n",grid[1][0],grid[1][1],grid[1][2],"\n",grid[2][0],grid[2][1],grid[2][2])
    print("Thinking...")
    print("Disclaimer: This is a very basic bot with no prediction yet. Purely just to get it working currently")
    selectionx = random.randint(1,3)
    selectiony = random.randint(1,3)
    placed = place(2, selectionx, selectiony)
    if placed == False:
        singleplayerp2()
    elif placed == True:
        if wintest():
            import main
            main.main()
        elif istie():
            import main
            print("It's a tie!")
            main.main()
        else:
            singleplayerp1()
    
    


def selectp1():
    print("Player 1's turn...")
    selectionx = int(input("Please select first grid reference (1,3 of rows) \n"))
    selectiony = int(input("Please select second grid reference (1,3 of columns) \n"))
    placed = place(1, selectionx, selectiony)
    if placed == False:
        selectp1()
    elif placed:
        won = wintest()
        if won or istie():
            import main
            if not won:
                print("It's a tie!")
            main.main()
        else:
            loopp1()
    

def selectp2():
    print("Player 2's turn...")
    selectionx = int(input("Please select first grid reference (1,3 of rows) \n"))
    selectiony = int(input("Please select second grid reference (1,3 of columns) \n"))
    placed = place(2, selectionx, selectiony)
    if placed == False:
        selectp2()
    elif placed:
        won = wintest()
        if won or istie():
            import main
            if not won:
                print("It's a tie!")
            main.main()
        else:
            loopp2()

def place(player, x, y):
    global grid
    if x == 1:
        if y == 1:
            coordinate1 = 0
            coordinate2 = 0
        elif y == 2:
            coordinate1 = 0
            coordinate2 = 1
        elif y == 3:
            coordinate1 = 0
            coordinate2 = 2
    elif x == 2:
        if y == 1:
            coordinate1 = 1
            coordinate2 = 0
        elif y == 2:
            coordinate1 = 1
            coordinate2 = 1
        elif y == 3:
            coordinate1 = 1
            coordinate2 = 2
    elif x == 3:
        if y == 1:
            coordinate1 = 2
            coordinate2 = 0
        elif y == 2:
            coordinate1 = 2
            coordinate2 = 1
        elif y == 3:
            coordinate1 = 2
            coordinate2 = 2

    if player == 1:
        if grid[coordinate1][coordinate2] == "O":
            print("That place is taken.")
            return False
        elif grid[coordinate1][coordinate2] == "X":
            print("That place is taken.")
            return False
        else:
            grid[coordinate1][coordinate2] = "X"
            print(f"Successfully taken coordinate ({x},{y})")
            return True

    elif player == 2:
        if grid[coordinate1][coordinate2] == "X":
            print("That place is taken.")
            return False
        elif grid[coordinate1][coordinate2]== "O":
            print("That place is taken.")
            return False
        else:
            grid[coordinate1][coordinate2] = "O"
            print(f"Successfully taken coordinate ({x},{y})")
            return True
    

def loopp1():
    global grid
    print("",grid[0][0],grid[0][1],grid[0][2],"\n",grid[1][0],grid[1][1],grid[1][2],"\n",grid[2][0],grid[2][1],grid[2][2])
    selectp2()

def loopp2():
    global grid
    print("",grid[0][0],grid[0][1],grid[0][2],"\n",grid[1][0],grid[1][1],grid[1][2],"\n",grid[2][0],grid[2][1],grid[2][2])
    selectp1()

def wintest():
    global grid
    winning_lines = (
        (grid[0][0], grid[0][1], grid[0][2]),
        (grid[1][0], grid[1][1], grid[1][2]),
        (grid[2][0], grid[2][1], grid[2][2]),
        (grid[0][0], grid[1][0], grid[2][0]),
        (grid[0][1], grid[1][1], grid[2][1]),
        (grid[0][2], grid[1][2], grid[2][2]),
        (grid[0][0], grid[1][1], grid[2][2]),
        (grid[0][2], grid[1][1], grid[2][0]),
    )

    for line in winning_lines:
        if line[0] != "#" and line[0] == line[1] == line[2]:
            print("Player 1 wins!" if line[0] == "X" else "Player 2 wins!")
            return True
    return False


def istie():
    global grid
    return all(cell != "#" for row in grid for cell in row)
