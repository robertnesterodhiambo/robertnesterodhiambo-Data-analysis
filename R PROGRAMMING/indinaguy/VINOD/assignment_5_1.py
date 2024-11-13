# Assignment 5 Problem 1: Use successive approximation to find the value of an investment
# September 22, 2022
# John Smith

def fixedInvestor(salary, p_rate, f_rate, years):
    """
    Calculate the value of a retirement investment with fixed contributions.
    
    Arguments:
    salary -- annual salary
    p_rate -- personal investment rate (percentage of salary)
    f_rate -- fixed growth rate of the retirement plan
    years -- number of years to calculate
    
    Returns:
    List of account balance at the end of each year.
    """
    balances = []
    employee_contrib = salary * p_rate
    employer_contrib = salary * 0.05 + min(employee_contrib, salary * 0.05)  # Employee and employer matching

    # Initial balance without growth
    balance = employee_contrib + employer_contrib
    balances.append(balance)

    # Annual compounding
    for year in range(1, years):
        balance += balance * f_rate  # Compound interest from previous balance
        balances.append(balance)

    return balances

# Example usage
print(fixedInvestor(50000, 0.05, 0.05, 5))

