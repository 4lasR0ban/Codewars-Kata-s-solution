# Codewars Kyu 6

# Build tower

# Build Tower by the following given argument:
# number of floors (integer and always greater than 0).

# Tower block is represented as *

    # Python: return a list;

def tower_builder(n_floors):
    return [('*' * i).center(n_floors * 2 - 1) for i in range(1, 2 * n_floors + 1, 2)]