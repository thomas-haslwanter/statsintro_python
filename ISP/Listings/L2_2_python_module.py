""" Demonstration of a Python Function """

# author:   Thomas Haslwanter
# date:     June-2020

# Import standard packages
import numpy as np
from typing import Tuple


def income_and_expenses(data : np.ndarray) -> Tuple[float, float]:
    """Find the sum of the positive numbers, and the sum of the negative ones.

    Parameters
    ----------
    data : numpy array (,n)
           Incoming and outgoing account transactions

    Returns
    -------
    income : Sum of the incoming transactions
    expenses : Sum of the outgoing account transactions
    """
    
    income = np.sum(data[data>0])
    expenses = np.sum(data[data<0])
    
    return (income, expenses)


if __name__=='__main__':
    testData = np.array([-5, 12, 3, -6, -4, 8])
    
    # If only real banks would be so nice ;)
    if testData[0] < 0:
        print('Your first transaction was a loss, and will be dropped.')
        testData = np.delete(testData, 0)
    else:
        print('Congratulations: Your first transaction was a gain!')
        
    (my_income, my_expenses) = income_and_expenses(testData)
    print(f'You have earned {my_income:5.2f} EUR, and spent {-my_expenses:5.2f} EUR.')

