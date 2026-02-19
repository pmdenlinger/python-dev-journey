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

def ask(prompt="Please enter a value: "):
    return input(prompt + " ")

a = ask()
print(a)

b = ask()
b = ask("What do you want for b?")