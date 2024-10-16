# Assignment 3 Problem 1: quantities of chicken nuggets that fit within available order quantities
# Date: [16th October, 2024]
# Developer: [ALEKHA]

def find_nugget_combinations(n):
    combinations = []
    for a in range(n // 6 + 1):
        for b in range(n // 9 + 1):
            for c in range(n // 22 + 1):
                if 6 * a + 9 * b + 22 * c == n:
                    combinations.append({'Six_piece': a, 'Nine_piece': b, 'Twenty_two_piece': c})
    return combinations

n = int(input("How many chicken nuggets would you like to order? "))
combinations = find_nugget_combinations(n)

if combinations:
    print(f"For an order size of {n}, choose from the following {len(combinations)} option(s):")
    for combo in combinations:
        print(combo)
else:
    print(f"Sorry, you cannot order {n} chicken nuggets.")
