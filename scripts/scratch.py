grocery_list = ["eggs", "milk", "cheese", "pasta"]

print("The first item on the list is " + grocery_list[0])
print("The second item on the list is " + grocery_list[1])

# Tuple is same as list but is immutable and runs faster. Instead of square brackets, it uses parentheses.
# Tuples are also more secure than lists because they cannot be altered.

planets = ("Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Nepture")
print(planets[3])

# Sets contain only unique values; copies are ignored. Sets are surrounded by curly brackets.
customers = {
    "James Smith", 
    "Andrea Richards", 
    "Sam Sharp", 
    "Brenda Longmire", 
    "Veronica March", 
    "Sylvia Smith",  
    "James Smith", 
    "Vanessa Bush", 
    "Steve Hammersmith", 
    "Brenda Longmire", 
    "Sylvia Smith", 
    "Steve Hammersmith", 
    "Walt Hawkins"
}
print(customers)

# Disctionaries are indexed lists of values which are indexed by key-:alue pairs.

customer1 = {
    "name": "James Smith",
    "age": 24,
    "phone": "555-555-1941",
    "email": "james@xyzinternet.net"
}

customer2 = {
    "name": "Andrea Richards",
    "age": "33",
    "phone": "555-555-4928",
    "email": "andrea@coffeeloversunite.us"
}
print(customer1["name"])

# Multidimensional Lists
# Daily high and low temperature
# (in Fahrenheit)

temps = [
    [66, 34],
    [57, 25],
    [49, 45]
]

today = (temps[0])
print(today)
print(today[0])
print(temps[2][1])

