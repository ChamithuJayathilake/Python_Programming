clas = input("Enter the cabin class (LUX, A, B, or C): ")

if clas == "LUX":
    print("Upper-deck cabin with a balcony.")
elif clas == "A":
    print("Above the car deck, equipped with a window.")
elif clas == "B":
    print("Windowless cabin above the car deck.")
elif clas == "C":
    print("Windowless cabin below the car deck.")
else:
    print("Invalid cabin class.")
