# Assignment 3 Problem 2: Find the closest feasible nugget quantity
# Date: [16th October, 2024]
# Developer: [ALEKHA]

# Function to find all possible nugget combinations
def find_nugget_combinations(n):
    combinations = []
    for a in range(n // 6 + 1):
        for b in range(n // 9 + 1):
            for c in range(n // 22 + 1):
                if 6 * a + 9 * b + 22 * c == n:
                    combinations.append({'Six_piece': a, 'Nine_piece': b, 'Twenty_two_piece': c})
    return combinations

# Function to find the closest feasible nugget quantity
def find_closest_nugget_quantity(n):
    while n > 0:
        combinations = find_nugget_combinations(n)
        if combinations:
            return n, combinations
        n -= 1
    return None, []

# Main logic
n = int(input("How many chicken nuggets would you like to order? "))
combinations = find_nugget_combinations(n)

if combinations:
    print(f"For an order size of {n}, choose from the following {len(combinations)} option(s):")
    for combo in combinations:
        print(combo)
else:
    print(f"Sorry, you cannot order {n} chicken nuggets.")
    closest_n, closest_combinations = find_closest_nugget_quantity(n)
    if closest_combinations:
        print(f"The closest feasible number of nuggets is {closest_n}. Here are your options:")
        for combo in closest_combinations:
            print(combo)
