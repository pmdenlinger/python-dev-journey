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
            try:
                s = input(display + " ")
            except EOFError:
                return ""
    else:
        try:
            s = input(display + " ")
        except EOFError:
            return ""
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
    for _ in range(x):
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

            if self.coffee_inventory <= 0:
                print("You're out of coffee. Please restock to keep playing.")
            # Get the weather
            temperature = self.weather

            # Display the cash and weather
            self.daily_stats(temperature)

            # Get price of a cup of coffee
            cup_price_input = prompt("What do you want to charge per cup of coffee?")
            if cup_price_input == "":
                print("\nNo input received. Exiting game.")
                break
            cup_price = convert_to_float(cup_price_input)

            # Get advertising spend
            print("You can buy advertising to help promote sales.")
            advertising_input = prompt("How much do you want to spend on advertising (0 for none)?", False)
            if advertising_input == "":
                print("\nNo input received. Exiting game.")
                break

            # Convert advertising into a float
            advertising = convert_to_float(advertising_input)

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
            self.increment_day()

            # Ask if the player wants to continue, restock, or quit
            print("Options: p = play again, r = restock, q = quit")
            next_action = prompt("Play again, restock, or quit? (p/r/q)", False)
            if next_action == "":
                print("\nNo input received. Exiting game.")
                break

            next_action = next_action.strip().lower()

            if next_action == "q":
                running = False
            elif next_action == "r":
                restock_input = prompt("How many cups would you like to restock?", False)
                if restock_input == "":
                    print("\nNo input received. Exiting game.")
                    break

                restock_amount = int(convert_to_float(restock_input))
                if restock_amount > 0:
                    self.coffee_inventory += restock_amount
                    print("Inventory restocked by " + str(restock_amount) + " cups.")
                else:
                    print("Restock amount must be greater than 0. Exiting game.")
                    running = False
            elif next_action == "p":
                if self.coffee_inventory <= 0:
                    print("You're out of coffee. Please restock next time. Game over!")
                    running = False
            else:
                print("Unrecognized option. Exiting game.")
                running = False

    def simulate(self, temperature, advertising, cup_price):
        # Find out how many cups were sold
        cups_sold = self.daily_sales(temperature, advertising)
        cups_sold = max(0, min(cups_sold, self.coffee_inventory))

        # Save the sales data for today
        self.sales.append({
            "day": self.day,
            "coffee_inv": self.coffee_inventory,
            "advertising": advertising,
            "temp": temperature,
            "cup_price": cup_price,
            "cups_sold": cups_sold
        })

        # We technically don't need this, but why make the next step
        # read from the sales list when we have the data right here
        return cups_sold

    # Faux temp distributions. We'll do this better
    # later with a bell curve, but for now a quick hack
    def make_temp_distribution(self):
        # This is not a good bell curve, but it will do for now
        # until we get to more advanced mathematics
        temps = []

        # First, find the average between TEMP_MIN and TEMP_MAX
        avg = (self.TEMP_MIN + self.TEMP_MAX) / 2
        # Find the distance between TEMP_MAX and the average
        max_dist_from_avg = self.TEMP_MAX - avg

        # Loop through all possible temperatures
        for i in range(self.TEMP_MIN, self.TEMP_MAX + 1):
            # How far away is the temperature from average?
            # abs() gives us the absolute value
            dist_from_avg = abs(avg - i)
            # How far away is the dist_from_avg from the maximum?
            # This will be lower for temps at the extremes
            dist_from_max_dist = max_dist_from_avg - dist_from_avg
            # If the value is zero, make it one
            if dist_from_max_dist == 0:
                dist_from_max_dist = 1
            # Append the output of x_of_y to temps
            for t in x_of_y(int(dist_from_max_dist), i):
                temps.append(t)
        return temps

    def increment_day(self):
        self.day += 1

    def daily_stats(self, temperature):
        print("You have $" + str(self.cash) + " cash on hand and the temperature is " + str(temperature) + ".")
        print("You have enough coffee on hand to make " + str(self.coffee_inventory) + " cups.\n")

    def day_header(self):
        print("\n-----| Day " + str(self.day) + " @ " + self.shop_name + " |-----")

    def daily_sales(self, temperature, advertising):
        return int((self.TEMP_MAX - temperature) * (advertising * 0.5))

    @property
    def weather(self):
        # Generate a random temperature between 20 and 90
        # We'll consider seasons later on, but this is good enough for now
        return random.choice(self.temps)

# Print welcome message
welcome()

# Get name and store name
t_name = prompt("What is your name?", True)
t_shop_name = prompt("What do you want to name your coffee shop?", True)

# Create the game object
game = CoffeeShopSimulator(t_name, t_shop_name)

# Run the game
game.run()





