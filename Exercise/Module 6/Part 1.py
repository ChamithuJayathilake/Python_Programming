import random

def roll_dice():
    return random.randint(1, 6)

def main():
    while True:
        result = roll_dice()
        if result == 6:
            break
        else:
            print(result)

main()
