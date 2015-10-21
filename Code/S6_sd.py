''' Solution to Exercise "Sample Standard Deviation" '''

# author: Thomas Haslwanter, date: Sept-2015

import numpy as np

x = np.arange(1,11)
print('The standard deviation of the numbers from 1 to 10 is {0:4.2f}'.format(np.std(x, ddof=1)))
