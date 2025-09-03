username = "python"
password = "rules"
i = 0

while i < 5:
    us = input("Enter username: ")
    pas = input("Enter password: ")

    if us == username and pas == password:
        print("Welcome")
        break
    else:
        i = i + 1
        if i == 5:
            print("Access denied")
            break
        else:
            print("Incorrect username or password. Please try again.")
