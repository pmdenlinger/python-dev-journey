# Define the ask function
# def ask(prompt):
#     return input(prompt + " ")

# # Use the ask function to find out how many cups we want
# question = ask("How many cups do you want?")
# print(question)

# def ask(prompt):
#     return input(prompt + " ")

# Use the ask function to find out how many cups we want
# print(ask("How many cups do you want?"))

# Define the function full_name
# def full_name(first, middle, last, display):
#     name = first + " " + middle + " " + last
#     if display:
#         print(name)
#     return name
# Use our newly created function
# full_name("Robert", "w", "Oliver", True)
# complete_name = full_name("Robert", "W", "Oliver", False)
# print(complete_name)

# def ask(prompt="Please enter a value: "):
#     return input(prompt + " ")

# a = ask()
# print(a)

# b = ask()
# b = ask("What do you want for b?")

# When setting default values for parameters, the default values must run first before the input values.

# For keyword arguments, the sequence for the default values does not matter. They are useful when a function takes more than two parameters # and it's difficult to remember the order. They are also useful when the function will expand later with more arguments, instead of making # # multiple edits to the code. There is no performace penalty for running the code. If a function uses keyword arguments, they should be # # # # supplied for each function.

def full_name(first, middle, last, display = False):
    name = first + " " + middle + " " + last
    if display:
        print(name)
    return(name)

# print(full_name(first = "Robert", middle = "W", last = "Oliver"))
print(full_name(last = "Oliver", first = "Robert", middle = "W"))