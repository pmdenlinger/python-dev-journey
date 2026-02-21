# ClydeBank Coffee Shop Simulator 4000
# Copyright 2026 (C) ClydeBank Media, All Rights Reserved.

# Import the random module
import random

def welcome():
    print("ClydeBank Coffee Simulator 4000, Version 2.00")
    print("Copyright (C) 2026 ClydeBank Media, All Rights Reserved.\n")
    print("Let's collect some information before we start the game.\n")

def prompt(display="Please input a string", require=True):
    if require:
        s = False
        while not s:
            s = input(display + " ")
    else:
        s = input(display + " ")
    return s

def convert_to_float(s):
    # If conversion fails, assign it to 0
    try:
        f = float(s)
    except ValueError:
        f = 0
    return f

def x_of_y(x, y):
    num_list = []
    # Return a list of x numbers of y
    for i in range(x):
        num_list.append(y)
        return num_list
    
class CoffeeShopSimulator:

    # Minimum and maximum temperatures
    TEMP_MIN = 20
    TEMP_MAX = 90

    def __init__(self, player_name, shop_name):

        # Set player and coffee shop names
        self.player_name = player_name
        self.shop_name = shop_name

        # Current day number
        self.day = 1

        #Cash on hand at start
        self.cash = 100.00

        # Inventory at start
        self.coffee_inventory = 100

        # Sales list
        self.sales = []

        # Possible temperatures
        self.temps = self.make_temp_distribution()

    def run(self):
        print("\nOk, let's get started. Have fun!")  

        # The main game loop
        running = True
        while running:
        # Display the day and add a "fancy" text effect
        self.day_header()
        # print("\n-----| Day " + str(day) + " @ " + shop_name + " |-----")

        # Get the weather
        temperature = self.weather

        # Display the cash and weather
        self.daily_stats(temperature)

        # Get price of a cup of coffee
        cup_price = float(
            prompt("What do you want to charge per cup of coffee?"))
        
        # Get advertising spend
        print("You can buy advertising to help promote sales.")
        advertising = prompt("How much do you want to spend on advertising (0 for none)?",  False)

        # Convert advertising into a float
        advertising = convert_to_float(advertising)

        # Deduct advertising from cash on hand
        self.cash -= advertising

        # Simulate today's sales
        cups_sold = self.simulate(temperature, advertising, cup_price)
        gross_profit = cups_sold * cup_price

        # Display the results
        print("You sold " + str(cups_sold) + " cups of coffee today.")
        print("You made $" + str(gross_profit) + ".")

        # Add the profit to our coffers
        self.cash += gross_profit

        # Subtract inventory
        self.coffee_inventory -= cups_sold

        # Before we loop around, add a day
        day += 1  


# Current day number 
day = 1

# Starting cash on hand
cash = 100.00

# Coffee on hand (cups)
coffee = 100





def daily_stats(cash_on_hand, weather_temp, coffee_inventory):
    print("You have $" + str(cash_on_hand) + " cash on hand and the temperature is " + str(weather_temp) + ".")
    print("You have enough coffee on hand to make " + str(coffee_inventory) + " cups.\n") 





# Print welcome message
welcome()

# Get name and store name
name = prompt("What is your name?", True)
shop_name = prompt("What do you want to name your coffee shop?", True)





