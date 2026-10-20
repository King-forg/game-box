# Naughts and crosses game

import random


WINNING_LINES = (
    ((0, 0), (0, 1), (0, 2)),
    ((1, 0), (1, 1), (1, 2)),
    ((2, 0), (2, 1), (2, 2)),
    ((0, 0), (1, 0), (2, 0)),
    ((0, 1), (1, 1), (2, 1)),
    ((0, 2), (1, 2), (2, 2)),
    ((0, 0), (1, 1), (2, 2)),
    ((0, 2), (1, 1), (2, 0)),
)

grid = []


def new_grid():
    global grid
    grid = [["#" for _ in range(3)] for _ in range(3)]


def display_grid():
    for row in grid:
        print(" ".join(row))


def start(players):
    if players == 1:
        singleplayer()
    elif players == 2:
        multiplayer()
    else:
        print("Please select 1 or 2 players.")


def singleplayer():
    new_grid()
    print("Welcome to naughts and crosses.")
    difficulty = choose_difficulty()
    player_turn = random.choice((1, 2))

    while True:
        display_grid()
        if player_turn == 1:
            print("Your turn...")
            x, y = read_move()
            place(1, x, y)
        else:
            print("Computer is thinking...")
            x, y = bot_move(difficulty)
            place(2, x, y)

        if wintest() or istie():
            if not has_winner("X") and not has_winner("O"):
                print("It's a tie!")
            return
        player_turn = 2 if player_turn == 1 else 1


def multiplayer():
    new_grid()
    print("Welcome to naughts and crosses.")
    player_turn = random.choice((1, 2))
    print(f"Player {player_turn} starts first")

    while True:
        display_grid()
        print(f"Player {player_turn}'s turn...")
        x, y = read_move()
        place(player_turn, x, y)
        if wintest() or istie():
            if not has_winner("X") and not has_winner("O"):
                print("It's a tie!")
            return
        player_turn = 2 if player_turn == 1 else 1


def choose_difficulty():
    while True:
        difficulty = input("Choose difficulty: 1-Easy, 2-Medium, 3-Hard\n").strip().lower()
        if difficulty in ("1", "easy"):
            return "easy"
        if difficulty in ("2", "medium"):
            return "medium"
        if difficulty in ("3", "hard"):
            return "hard"
        print("Please choose easy, medium, or hard.")


def read_move():
    while True:
        try:
            x = int(input("Please select the row (1-3).\n"))
            y = int(input("Please select the column (1-3).\n"))
        except ValueError:
            print("Please enter numbers from 1 to 3.")
            continue
        if place(1, x, y, preview=True):
            return x, y
        print("Please choose an available square.")


def place(player, x, y, preview=False):
    if player not in (1, 2) or not (1 <= x <= 3 and 1 <= y <= 3):
        return False
    row = x - 1
    column = y - 1
    if grid[row][column] != "#":
        return False
    if preview:
        return True
    grid[row][column] = "X" if player == 1 else "O"
    print(f"Successfully taken coordinate ({x},{y})")
    return True


def available_moves():
    return [
        (row, column)
        for row in range(3)
        for column in range(3)
        if grid[row][column] == "#"
    ]


def bot_move(difficulty):
    moves = available_moves()
    if difficulty == "easy":
        row, column = random.choice(moves)
        return row + 1, column + 1

    winning = find_tactical_move("O")
    if winning:
        return winning
    blocking = find_tactical_move("X")
    if blocking:
        return blocking
    if difficulty == "hard":
        row, column = minimax_move()
        return row + 1, column + 1
    row, column = random.choice(moves)
    return row + 1, column + 1


def find_tactical_move(marker):
    for row, column in available_moves():
        grid[row][column] = marker
        wins = has_winner(marker)
        grid[row][column] = "#"
        if wins:
            return row + 1, column + 1
    return None


def minimax_move():
    best_score = -float("inf")
    best_move = None
    cache = {}
    for row, column in available_moves():
        grid[row][column] = "O"
        score = minimax(False, cache)
        grid[row][column] = "#"
        if score > best_score:
            best_score = score
            best_move = (row, column)
    return best_move


def minimax(bot_turn, cache):
    state = tuple(tuple(row) for row in grid)
    cache_key = (state, bot_turn)
    if cache_key in cache:
        return cache[cache_key]

    if has_winner("O"):
        score = 1
    elif has_winner("X"):
        score = -1
    else:
        moves = available_moves()
        if not moves:
            score = 0
        else:
            scores = []
            marker = "O" if bot_turn else "X"
            for row, column in moves:
                grid[row][column] = marker
                scores.append(minimax(not bot_turn, cache))
                grid[row][column] = "#"
            score = max(scores) if bot_turn else min(scores)

    cache[cache_key] = score
    return score


def has_winner(marker):
    return any(
        all(grid[row][column] == marker for row, column in line)
        for line in WINNING_LINES
    )


def wintest():
    for marker in ("X", "O"):
        if has_winner(marker):
            print("Player 1 wins!" if marker == "X" else "Player 2 wins!")
            display_grid()
            return True
    return False


def istie():
    return not available_moves()
