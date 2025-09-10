def sum_of_list(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

def main():
    numbers = [1, 2, 3, 4, 5]   # sum = 15
    result = sum_of_list(numbers)
    print("The sum of the numbers in the list is:", result)

main()
