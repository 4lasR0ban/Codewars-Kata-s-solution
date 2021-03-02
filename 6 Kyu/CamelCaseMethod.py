# Codewars Kyu 6

# CamelCase method

# Write simple .camelCase method (camel_case function in PHP, CamelCase in C# or camelCase in Java) for strings. All words must have their first letter capitalized without spaces.

def camel_case(string):
    return string.title().replace(" ", "")