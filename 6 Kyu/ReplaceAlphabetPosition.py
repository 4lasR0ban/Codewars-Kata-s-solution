# Codewars Kyu 6

# Replace with alphabet position

# In this kata you are required to, given a string, replace every letter with its position in the alphabet.
# If anything in the text isn't a letter, ignore it and don't return it.
# "a" = 1, "b" = 2, etc.

from string import ascii_lowercase

letters = {letter: str(index) for index, letter in enumerate(ascii_lowercase, start=1)}

def alphabet_position(a):
    a = a.lower()
    number = [letters[character] for character in a if character in letters]
    return ' '.join(number)