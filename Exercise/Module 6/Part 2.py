import random

def roll_dice(faces):
    return random.randint(1, faces)

def main():
    faces = int(input("How many faces does the die have? "))
    while True:
        result = roll_dice(faces)
        print(result)
        if result == faces:
            break

main()
