import random

# Ask the user how many random points to generate
N = int(input("Enter the number of random points: "))

n = 0       # Counter for points inside the circle
i = 0       # Counter for total points generated

while i < N:
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)

    if x**2 + y**2 < 1:
        n += 1

    i += 1

# Approximate pi
pi_approx = 4 * n / N

# Print the result
print(f"Approximation of pi: {pi_approx}")
