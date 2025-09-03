smallest = None
largest = None

while True:
    num = input("Enter a number (or press Enter to quit): ")
    if num == "":
        break

    num = float(num)

    if smallest is None or num < smallest:
        smallest = num
    if largest is None or num > largest:
        largest = num

if smallest is not None and largest is not None:
    print(f"Smallest number: {smallest}")
    print(f"Largest number: {largest}")
else:
    print("No numbers were entered.")
