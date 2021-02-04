""" Solution to Exercise "Sample Standard Deviation" """

# author: Thomas Haslwanter, date: Feb-2021

import numpy as np

x = np.linspace(1, 10, 10)
std = np.std(x, ddof=1)
print(f'The standard deviation of the numbers from 1 to 10 is {std:4.2f}')
