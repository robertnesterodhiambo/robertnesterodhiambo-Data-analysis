# Assignment 5 Problem 4: Calculate maximum sustainable retirement withdrawal
# September 22, 2022
# John Smith
from assignment_5_2 import variableInvestor
from assignment_5_3 import finallyRetired

def maximumExpensed(salary, p_rate, workRate, retiredRate, epsilon):
    """
    Calculate maximum annual expense post-retirement to deplete savings close to zero.
    
    Arguments:
    salary -- annual salary
    p_rate -- personal investment rate
    workRate -- list of annual growth rates while working
    retiredRate -- list of annual growth rates while retired
    epsilon -- acceptable small value for zero balance
    
    Returns:
    Maximum annual expense
    """
    # Step 1: Calculate savings at retirement
    saved_at_retirement = variableInvestor(salary, p_rate, workRate)[-1]
    
    # Step 2: Binary search for maximum sustainable expense
    low, high = 0, saved_at_retirement
    expense = (high + low) / 2

    while high - low > epsilon:
        balances = finallyRetired(saved_at_retirement, retiredRate, expense)
        final_balance = balances[-1]

        if final_balance < 0:
            high = expense  # Overdrawn; reduce expense
        else:
            low = expense  # Increase expense

        expense = (high + low) / 2
        print(f"Trying expense: {expense:.2f}, remaining balance: {final_balance:.2f}")

    return expense

# Example usage
print(maximumExpensed(50000, 0.05, [0.05, 0.04, 0.03], [0.04, 0.03, 0.02], 0.01))

