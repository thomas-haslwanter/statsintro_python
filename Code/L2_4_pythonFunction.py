'''Demonstration of a Python Function

author: thomas haslwanter, date: May-2015
'''

# Import standard packages
import numpy as np

def incomeAndExpenses(data):
    '''Find the sum of the positive numbers, and the sum of the negative ones.'''
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
        
    (myIncome, myExpenses) = incomeAndExpenses(testData)
    print('You have earned {0:5.2f} EUR, and spent {1:5.2f} EUR.'.format(myIncome, -myExpenses))

