'''Demonstration of importing a Python module

author: ThH, date: May-2015'''

# Import standard packages
import numpy as np

# additional packages: this imports the function defined above
import L2_4_pythonFunction

# Generate test-data
testData = np.arange(-5, 10)

# Use a function from the imported module
out = L2_4_pythonFunction.incomeAndExpenses(testData)

# Show some results
print('You have earned {0:5.2f} EUR, and spent {1:5.2f} EUR.'.format(out[0], -out[1]))
