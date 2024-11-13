# Assignment 5 Problem 2: Calculate variable growth rate retirement investment
# September 22, 2022
# John Smith

def variableInvestor(salary, p_rate, v_rate):
    """
    Calculate the value of a retirement investment with variable growth rates.
    
    Arguments:
    salary -- annual salary
    p_rate -- personal investment rate (percentage of salary)
    v_rate -- list of annual growth rates
    
    Returns:
    List of account balance at the end of each year.
    """
    balances = []
    employee_contrib = salary * p_rate
    employer_contrib = salary * 0.05 + min(employee_contrib, salary * 0.05)

    # Initial balance without growth
    balance = employee_contrib + employer_contrib
    balances.append(balance)

    # Apply each growth rate from the list
    for rate in v_rate[1:]:
        balance += balance * rate
        balances.append(balance)

    return balances

# Example usage
print(variableInvestor(50000, 0.05, [0, 0.05, 0.03, 0.04, 0.06]))

