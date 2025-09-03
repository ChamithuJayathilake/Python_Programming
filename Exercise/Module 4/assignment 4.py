import random

guess = random.randint(1, 10)

while True:
    num = int(input("Guess a number (1-10): "))

    if num == guess:
        print("Correct")
        break
    elif num < guess:
        print("Too low")
    else:
        print("Too high")

