# Assignment 5 Problem 3: Calculate post-retirement account balance with expenses
# September 22, 2022
# John Smith

def finallyRetired(saved, v_rate, expensed):
    """
    Calculate remaining balance in retirement after fixed withdrawals.
    
    Arguments:
    saved -- initial retirement savings
    v_rate -- list of annual growth rates after retirement
    expensed -- annual amount withdrawn
    
    Returns:
    List of account balance at the end of each year.
    """
    balances = [saved]

    for rate in v_rate:
        balance = balances[-1] * (1 + rate) - expensed
        balances.append(balance)
    
    return balances[1:]  # Exclude initial balance

# Example usage
print(finallyRetired(200000, [0.05, 0.04, 0.03, 0.02], 15000))

