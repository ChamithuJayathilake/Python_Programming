def draw_spruce(size):
    print("A spruce is coming!")

    # Draw the tree branches
    for i in range(1, size + 1):
        spaces = " " * (size - i)
        stars = "*" * (2 * i - 1)
        print(spaces + stars)

    # Draw the tree trunk
    spaces_trunk = " " * (size - 1)
    print(spaces_trunk + "*")

draw_spruce(6)