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

# Import the regular expression engine
# import re 

# Define our content
# text = "Hello, World!"

# Is "Hello" in our string?
# if re.search("Hello", text):
#     print("Hello is in the string.")
# else:
#     print("Hello isn't in the string.")

# Import the regular expression engine
# import re

# Define our content
# text = "The quick gray fox jumped over the lazy dog!"

# Find
# match = re.search("(gray|grey)", text, re.IGNORECASE)

# Get start and end of match
# match_start = match.span()[0]
# match_end = match.span()[1]

# Replacement text
# replace_text = "grey"

# Replace gray with grey using the position from span
# new_text = text[:match_start] + replace_text + text[match_end:]

# Display results 
# print("Old text: " + text)
# print("New text: " + new_text)

# Import the regular expression engine
# import re

# Define our content
# text = "The quick brown fox jumped over the lazy dog!"

# Find
# match = re.search("(gray|grey)", text, re.IGNORECASE)

# Print the match
# print(match.group(0))

# Import the regular expression engine
# import re

# Define our content
# text = "This is the house. It has red red paint."

# Regular expression to find duplicate words
# Use prefix r before to treat as raw (unescaped) string
# regex = r"\b(\w+)\s+\1\b"

# Find any duplicate words
# matches = re.findall(regex, text, re.IGNORECASE)

# Print the duplicate words
# for match in matches:
    # print(match)

# Import the regular expression engine
# import re

# Define our content
# text = "Hello, World!"

# Does the string begin with the letter H?
# if re.search("^H", text):
#     print("The string begins with H.")
# else:
#     print("The string does not begin with H.")

# Import the regular expression engine
# import re

# Define our content
# text = "Hello, World!"

# Does the string end in an exclamation point?
# if re.search("\!$", text):
#     print("The string ends with an exclamation point.")
# else:
#     print("The string doesn't end with an exclamation point.")

# Import the regular expression engine
# import re

# Our string
# test = "Hello, World!"

# Match
# if re.match("e", test):
#     print("re.match says it has an e in it")

# Search
# if re.search("e", test):
#     print("re.search says it has an e in it")

# Import the regular expression engine
# import re

# Our string
# test = "The quick brown fox is fast!"

# Split by spaces using the \s metacharacter 
# Since we want to account for multiple spaces, we add +
# space_split = re.split("\s+", test)
# print(space_split)

# Split by word using the non-word metacharacter
# Since we want to account for multiple
# non-word characters, we add +
# word_split = re.split("\W+", test)
# print(word_split)

# Import the regular expression engine
# import re

# Our string
# test = "The quick brown fox is fast!"

# Substitute spaces for +
# plus_test = re.sub("\s+", "+", test)
# print(plus_test)  

# Define the name
# name = "Robert"

# Print a friendly message
# print("Hello, {}!".format(name))

# Define our greeting
greeting = "Hello, {name}! It's currently {temp} and the time is {time}."

# Print the message
print(greeting.format(name = "Robert", temp = "54F", time = "3:42PM"))

