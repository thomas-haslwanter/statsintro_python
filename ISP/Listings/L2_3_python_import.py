""" Demonstration of importing a Python module """

# Import standard packages
import numpy as np

# additional packages: this imports the function defined above
import L2_2_python_module as py_func

# Generate test-data
testData = np.arange(-5, 10)

# Use a function from the imported module
out = py_func.income_and_expenses(testData)

# Show some results
print(f'You have earned {out[0]:5.2f} EUR, and spent {-out[1]:5.2f} EUR.')
