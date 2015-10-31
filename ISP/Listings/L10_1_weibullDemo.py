''' Example of fitting the Weibull modulus. '''

# author: Thomas Haslwanter, date: Jun-2015

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
print('The fitted Weibull modulus is {0:5.2f}, compared to the exact value of 1.5 .'.format(fitPars[0]))