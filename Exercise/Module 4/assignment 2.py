while True:
    inches = float(input("Enter length in inches (negative value to quit): "))

    if inches < 0:
        print("Program terminated.")
        break

    centimeters = inches * 2.54
    print(f"{inches} inches = {centimeters:.2f} cm")
