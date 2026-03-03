# Create a string
# a = "Hello, World!"

# Search for "World" in the string
# if a.find("World") != -1:

    # Replace "World" with "Reader"
    # b = a.replace("World", "Reader")

    # # Display the results
    # print(a)
    # print("... was replaced with ...")
    # print(b)

# Create our string
# title = "Python QuickStart Guide"

# Display it all uppercase
# print(title.upper())

# Display it all lowercase
# print(title.lower())

# Create our string
#tongue_twister = "She sells seashells by the seashore."

# Count the number of 's' in tongue_twister and display it
# 

# A simple string
# fox = "The quick brown fox jumps over the lazy dog."

# Split the string
# fox_list = fox.split()

# Display the resulting list
# print(fox_list)

# An (obviously) fake ID number
# id = "123-45-6789"

# Split id by a dash character
# id_segments = id.split("-")

# Display it
# print(id_segments)

# New glossary terms
# glossary = "delimiter, module, package, class, object"

# Split by comma then a space
# glossary_list = glossary.split(", ")

# Display it
# print(glossary_list)

# Our glossary terms
# glossary = ['delimiter', 'module', 'package', 'class', 'object']

# The new joined string
# glossary_string = ", ".join(glossary)

# Display it 
# print(glossary_string)

# Ask user for a value
# value = input("Please enter a value: ")

# Check if every character is a number
# "3102" - True
# "4111123412341234" - True
# "04/22/2022" - False
# "1600 Pennsylvania Avenue" - False
# if value.isnumeric():
#     print("It's a number.")

# Check if every character is a letter
# Spaces, punctuation, and numbers don't count
# "Yes" - True
# "Yes " - False
# "Yes 3" - False
# "Yes!" - False
# if value.isalpha():
#     print("It is filled with alphabet characters only")

# Check if the string is alphanumeric (i.e., letters and numbers)
# "1600 Pennsylvania Avenue" - False
# "Washington, D.C." - False
# "Washington DC" - False
# "Washington" - True
# 

# Import the regular expression engine
# import re

# Define our content
# text = "Hello, World!"

# Is "Hello" in our string?
# if re.search("hello", text, re.IGNORECASE):
#     print("hello is in the string")
# else:
#     print("hello isn't in the string.")

# Import the regular expression engine
# import re

# Define our content
# text = "The quick gray fox jumped over the lazy dog!"

# Find
# match = re.search("(gray|grey)", text, re.IGNORECASE)

# Print the match
# print(match.group(0))