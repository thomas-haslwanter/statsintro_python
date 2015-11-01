'''Solution for Exercise "Continuous Distribution Functions" '''

# author: Thomas Haslwanter, date: Oct-2015

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# T-distibution ---------------------------------------------------
# Enter the data
x = [52, 70, 65, 85, 62, 83, 59]
''' Note that "x" is a Python "list", not an array!
 Arrays come with the numpy package, and have to contain all elements of the same type.
 Lists can mix different types, e.g. "x = [1, 'a', 2]"
 '''

# Generate the t-distribution: note that the degrees of freedom is the
# length of the data minus 1.
# In Python, the length of an object x is given by "len(x)"
td = stats.t(len(x)-1)
alpha = 0.01

# From the t-distribution, you use the "PPF" function and multiply it with the standard error
tval = abs( td.ppf(alpha/2)*stats.sem(x) )
print('mean +/- 99%CI = {0:3.1f} +/- {1:3.1f}'.format(np.mean(x),tval))

# Chi2-distribution, with 3 DOF ------------------------------------------------
# Define the normal distribution
nd = stats.norm()

# Generate three sets of random variates from this distribution
numData = 1000
data1 = nd.rvs(numData)
data2 = nd.rvs(numData)
data3 = nd.rvs(numData)

# Show a histogram of the sum of the squares of these random data
plt.hist(data1**2+data2**2 +data3**2, 100)
plt.show()

# F-distribution --------------------------------------------------
apples1 = [110, 121, 143]
apples2 = [88, 93, 105, 124]
fval = np.std(apples1, ddof=1)/np.std(apples2, ddof=1)
fd = stats.distributions.f(len(apples1),len(apples2))
pval = fd.cdf(fval)
print('The p-value of the F-distribution = {0}.'.format(pval))
if pval>0.025 and pval<0.975:
    print('The variances are equal.')

