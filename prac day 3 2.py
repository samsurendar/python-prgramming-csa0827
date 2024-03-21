from itertools import permutations

def find_combinations(digits):
    perms = permutations(digits)
    combinations = list(perms)
    return combinations

digits = [1, 2, 3]
combinations = find_combinations(digits)
print("Possible combinations:")
for combination in combinations:
    print(combination)
