"""Solutions to 6.3.1 Examples of Normal Distributions"""

# author: Thomas Haslwanter, date: Feb-2021

# Import standard packages
import numpy as np
from scipy import stats

# Example 1
nd = stats.norm(175, 6)
p = nd.cdf(184) - nd.cdf(183)
print(f'The chance that a randomly selected man is 183 cm tall is {p*100:.1f}%')

# Example 2

# Example 3
