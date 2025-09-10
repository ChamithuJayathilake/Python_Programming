def filter_even_numbers(numbers):
    even_numbers = []
    for num in numbers:
        if num % 2 == 0:
            even_numbers.append(num)
    return even_numbers

def main():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    even_list = filter_even_numbers(numbers)
    print("Original list:", numbers)
    print("List with even numbers only:", even_list)

main()
