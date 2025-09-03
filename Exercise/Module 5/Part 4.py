# Initialize an empty list to store city names
cities = []

# Use a for loop to ask for the names of 5 cities
for i in range(5):
    cities.append(input("Enter the name of a city: "))

# Print a blank line before listing the cities
print("\n\nThe cities you entered:")
for city in cities:
    print(city)