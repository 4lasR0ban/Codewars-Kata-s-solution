# Codewars Kyu 4

# Permutations

# In this kata you have to create all permutations of an input string and remove duplicates, if present. This means, you have to shuffle all letters from the input in all possible orders.

def permutations(string):
    result = set([string])
    if len(string) == 2:
        result.add(string[1] + string[0])

    elif len(string) > 2:
        for i, c in enumerate(string):
            for s in permutations(string[:i] + string[i + 1:]):
                result.add(c + s)

    return list(result)