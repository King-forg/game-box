import random
import os
import time
os.system('')

class Color:
    RESET = '\033[0m'
    BOLD = '\033[1m'

    CORRECT = '\033[42m'
    ALMOST = '\033[43m'
    ABSENT = '\033[90m'


def start(players):
    if players == 1:
        singleplayer()
    else:
        print("Only single player allowed")
        return

def generatedword():
    with open("words.txt") as f:
        return random.choice(f.read().split())

def singleplayer():
    correct = ["","","","",""]
    randomword = generatedword()
    word = randomword
    loop(word, correct)

def check(word, guess, correct):
    remaining = {}
    for i in range(5):
        if guess[i] == word[i]:
            correct[i] = 1
        else:
            correct[i] = 3
            remaining[word[i]] = remaining.get(word[i], 0) + 1
    for i in range(5):
        if correct[i] == 3 and remaining.get(guess[i], 0) > 0:
            correct[i] = 2
            remaining[guess[i]] -= 1
    return correct

def load_valid():
    with open("valid_words.txt") as f:
        return set(f.read().split())

def update_letters(letters, guess, results):
    for letter, r in zip(guess, results):
        if r < letters.get(letter,4):
            letters[letter] = r

def show_letters(letters):
    for row in ("qwertyuiop", "asdfghjkl", "zxcvbnm"):
        out = ""
        for l in row:
            status = letters.get(l)
            if status == 1:
                out = out + f"{Color.CORRECT} {l.upper()} {Color.RESET}"
            elif status == 2:
                out = out + f"{Color.ALMOST} {l.upper()} {Color.RESET}"
            elif status == 3:
                out = out + f"{Color.ABSENT} {l.upper()} {Color.RESET}"
            else:
                out = out + f" {l.upper()} "
        print(out)

def hint(hinttimes, word):
    if hinttimes == 0:
        print("Only 1 hint allowed")
    else:
        randint = random.randint(0,4)
        textrand = randint + 1
        print(f"The number {textrand} letter is {word[randint]}")

def won(end, began):
    timetaken = end - began
    timetaken = round(timetaken)
    print(f"You took {timetaken} seconds")
    import main
    main.selections()

def loss(end, began):
    timetaken = end - began
    timetaken = round(timetaken)
    print(f"You took {timetaken} seconds to lose the game")
    import main
    main.selections()

def loop(word, correct):
    print("Welcome to bordle\n")
    start = time.time()
    print("Guess the 5 letter word\n")
    print("_ _ _ _ _")
    VALID = load_valid()
    letters = {}
    hinttimes = 1
    for i in range(1,7):
        guess = input("Word: ")
        guess = guess.lower()
        while len(guess) != 5 or guess not in VALID:
            if guess.lower() == "hint":
                hint(hinttimes, word)
                hinttimes = 0
            elif len(guess) != 5:
                print("Must be 5 letters")
            else:
                print("Not in word list")
            guess = input("Word: ")
            guess = guess.lower()
        c1, c2, c3, c4, c5 = check(word, guess, correct)
        results = [c1, c2, c3, c4, c5]
        out = ""
        for letter, r in zip(guess, results):
            if r == 1:
                out = out + f"{Color.CORRECT} {letter.upper()} {Color.RESET}"
            elif r == 2:
                out = out + f"{Color.ALMOST} {letter.upper()} {Color.RESET}"
            else:
                out = out + f" {letter.upper()} "
        print(out)

        update_letters(letters, guess, results)
        show_letters(letters)

        if guess == word:
            print(f"{Color.CORRECT} {out} {Color.RESET}")
            end = time.time()
            won(end, start)
            return
    print(f"Out of guesses. Word was {word}")
    end = time.time()
    loss(end, start)
    return


            
start(1)