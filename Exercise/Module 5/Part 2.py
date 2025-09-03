numbers = []

while True:
    user_input = input("Enter a number: ")
    if user_input == "":
        break
    try:
        numbers.append(float(user_input))
    except ValueError:
        print("Please enter a valid number.")

# Sort numbers in descending order
numbers.sort(reverse=True)

# Print the five largest numbers
print("The greatest numbers in descending order:")
for num in numbers[:5]:
    print(num)
