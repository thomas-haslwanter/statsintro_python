'''Solutions to 6.3.1 Examples of Normal Distributions'''

# author: Thomas Haslwanter, date: Oct-2015

# Import standard packages
import numpy as np
from scipy import stats

# Example 1
nd = stats.norm(175, 6)
p = nd.cdf(184) - nd.cdf(183)
print('The probability that a randomly selected man is 183 cm tall is {0:.1f}% .'.format(p*100))

# Example 2

# Example 3
