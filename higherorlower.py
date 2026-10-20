import random
import time

def loop1(players):
    for i in range(players):
        while True:
            try:
                start = int(input("Please select the start number. \n"))
                end = int(input("Please select the end number. \n"))
            except ValueError:
                print("Please enter whole numbers.")
                continue
            if start <= end:
                break
            print("The end number must be at least the start number.")
        number = random.randint(start, end)
        print(f"I have picked a number from {start} to {end}")

        won = False
        while not won:
            try:
                selectednumber = int(input("Please select a number between them. \n"))
            except ValueError:
                print("Please enter a whole number.")
                continue
            if selectednumber > end:
                print("Invalid number - Please reselect.")
            elif selectednumber < start:
                print("Invalid number - Please reselect.")
            elif selectednumber > number:
                print("You are.....", end="\r")
                time.sleep(0.1)
                print("You are......", end="\r")
                time.sleep(0.1)
                print("You are.......", end="\r")
                time.sleep(0.1)
                print("You are........", end="\r")
                time.sleep(0.1)
                print("You are.........", end="\r")
                time.sleep(0.1)
                print("\n Higher!!!!")
            elif selectednumber < number:
                print("You are.....", end="\r")
                time.sleep(0.1)
                print("You are......", end="\r")
                time.sleep(0.1)
                print("You are.......", end="\r")
                time.sleep(0.1)
                print("You are........", end="\r")
                time.sleep(0.1)
                print("You are.........", end="\r")
                time.sleep(0.1)
                print("\n Lower!!!!")
            else:
                print("\n You won!!!!! \n")
                won = True

def main():
    while True:
        try:
            turns = int(input("How many turns would you like?\n"))
        except ValueError:
            print("Please enter a whole number.")
            continue
        if turns > 0:
            loop1(turns)
            return
        print("Please enter at least 1 turn.")
