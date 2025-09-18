import random


def dice_roll(sides):
    return random.randint(1, sides)

sides = int(input("Input the number of Slides "))

dice_roll(sides)

while True:
    result = dice_roll(sides)

    if result == sides:
        break
    else:
        print(result)
