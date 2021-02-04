""" Example of fitting the Weibull modulus. """

# author: Thomas Haslwanter, date: [xxx]-2021

# Import standard packages
import matplotlib.pyplot as plt
import scipy as sp
from scipy import stats

# Generate some sample data, with a Weibull modulus of 1.5
WeibullDist = stats.weibull_min(1.5)
data = WeibullDist.rvs(500)

# Now fit the parameter
fitPars = stats.weibull_min.fit(data)

# Note: fitPars contains (WeibullModulus, Location, Scale)
print(f'The fitted Weibull modulus is {fitPars[0]:5.2f},' +
      ' compared to the exact value of 1.5 .')