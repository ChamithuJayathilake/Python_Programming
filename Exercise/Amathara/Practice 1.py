race = input("What is your type (Elves, Ghost, Wizard): ").lower()

if race == "elves" or race == "ghost" or race == "wizard":
    age = int(input("What is your age: "))

    if race == "elves" and age > 100:
        print("You can buy Leaf Drinks and sparkling water")
    elif race == "elves" and age <= 100:
        print("You can buy sparkling water")
    elif race == "ghost":
        print("You can buy Leaf Drinks and dust cookies")
    elif race == "wizard" and age > 21:
        print("You can buy sparkling water and wine")
    else:
        print("You can buy sparkling water.")
else:
    print("Invalid Type.")
