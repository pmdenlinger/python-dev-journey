# Define the world class
# class World:
    # Define our greeting
    # greeting = "Hello, World!"

    # Run this whenever the object is created
    # def __init__(self):
        # Print the greeting
        # print(self.greeting)

# Use the class World to create a world object named w
# w = World()
# 
# Define a new class
# class Customer: 
#     def __init__(self, name, city):
#         self.name = name
#         self.city = city

#     def greet(self):
#         print("Hello, " + self.name + "!")

# Create three objects based on the Customer class
# c1 = Customer("Sarah", "Atlanta")
# c2 = Customer("Robert", "Florence")
# c3 = Customer("Thomas", "Denver")

# Add the customer objects to a list
# customers = [c1, c2, c3]

# Iterate through list, greet, then display information
# for c in customers:
#     c.greet()
#     print(c.name + " lives in " + c.city + ".")

# Define the World class
# class World:
    # Define our greeting
    # greeting = "Hello, World!"

# print(World.greeting)    

# This variable exists in the main scope
# name = "Sarah"

# Define a new class with a class variable called name
# class Customer:
#     name = "Robert"

# Create a new customer so that __init__ is called
# customer = Customer()

# Display the nmae in the main scope
# print(customer.name)

# This variable exists in the main scope
# name = "Sarah"

# Define a new class with a class variable called name
# class Customer:
#     def __init__(self, name):
#         self.name = name

# Create a new customer so that __init__ is called
# customer = Customer("Robert")

# Display the name in the main scope
# 

# Define a new class
# class Customer:
#     # Define the init method, using name and city as arguments
#                 def __init__(self, name, city):
#                         self.name = name
#                         self.city = city

# Create three objects based on the Customer class
# The name and city are passed to __init__
# c1 = Customer("Sarah", "Atlanta")
# c2 = Customer("Robert", "Florence")
# c3 = Customer("Thomas", "Denver")

# Define a new class
# class Customer:
#     def __init__(self, name, city):
#         self.name = name
#         self.city = city

#     def __enter__(self):
#         print("Entering scope")
        # Run code upon entering scope of with statement
        # return self

    # def __exit__(self, exc_type, exc_value, traceback):
    #     print("Leaving scope.")
    #     # Run code upon leaving scope of with statement

    # def greet(self):
    #     print("Hello, " + self.name + "!")

# Use with to create a scope
# with Customer("Robert", "Florence") as robert:
    # robert.greet()    

# class World:
#         def __init__(self):
#                 print("I'm alive!")
#         def __del__(self):
#                 print("I'm gone!") 

# earth = World()
# del(earth)  
# 

# Convert kilometers to miles

# class Converter:
#     def __init__(self, km):
#         self.km = km
#     def to_miles(self):
#         return self.km / 1.609
        
    # Convert three kilometers to miles
# distance1 = Converter(3)
# print(distance1.to_miles)

# Use properties instead of instance variables

# class Distance:
#     def __init__(self, km):
#         self._km = km
#     @property
#     def km(self):
#         return self._km
#     @property
#     def miles(self):
#         return self._km / 1.609
    
# distance2 = Distance(3)
# print(str(distance2.km))
# print(str(distance2.miles))    

# class Distance:
#     def __init__(self, km):
#         self._km = km

#     @property
#     def km(self):
#         return self._km

#     @km.setter
#     def km(self, value):
#         self._km = value

#     @property 
#     def miles(self):
#         return self._km / 1.609

#     @miles.setter
#     def miles(self, value):
#         self._km = value * 1.609

# distance2 = Distance(3)
# print("3 kilometers is " + str(distance2.miles) + " miles.")
# distance2.miles = 3
# print(str(distance2.miles) + " miles is " + str(distance2.km) + " kilometers.")                


                         
