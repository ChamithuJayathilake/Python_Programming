import random

# Ask the user how many dice to roll
num_dice = int(input("How many dice to roll: "))

# Initialize sum
total = 0

# Roll each die and add to total
for _ in range(num_dice):
    roll = random.randint(1, 6)  # Dice roll between 1 and 6
    total += roll

# Print the result
print("Sum of the dice:", total)
