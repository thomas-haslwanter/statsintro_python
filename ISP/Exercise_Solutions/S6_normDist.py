""" Solution to Exercise "Normal Distribution" """

# author: Thomas Haslwanter, date: Feb-2021

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import pandas as pd
import seaborn as sns


# Generate a PDF, with a mean of 5 and a standard deviation of 3
nd = stats.norm(5,3)

# Generate 1000 data from this distribution
data = nd.rvs(1000)

# Standard error
se = np.std(data, ddof=1)/np.sqrt(1000)
print('The standard error is {0}'.format(se))

# Histogram
plt.hist(data)
plt.show()

# 95% confidence interval
print('95% Confidence interval: '+
      f'{nd.ppf(0.025):4.2f} - {nd.ppf(0.975):4.2f}')

# SD for hip implants
nd = stats.norm()
numSDs = nd.isf(0.0005)
tolerance = 1/numSDs
print(f'The required SD to fulfill both requirements = {tolerance:6.4f} mm')

