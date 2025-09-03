# Ask the user for an integer
num = int(input("Enter an integer: "))

# Handle numbers less than 2
if num < 2:
    print(f"{num} is not a prime number.")
else:
    is_prime = True
    # Check divisibility from 2 up to the square root of num
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    # Print result
    if is_prime:
        print(f"{num} is a prime number.")
    else:
        print(f"{num} is not a prime number.")
