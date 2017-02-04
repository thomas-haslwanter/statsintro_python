''' Demonstration of the package "lifelines"
Based on the demo-code in http://lifelines.readthedocs.org, by Cam Davidson-Pilon
'''

# Copyright(c) 2015, Thomas Haslwanter. All rights reserved, under the CC BY-SA 4.0 International License

# Import standard packages
import numpy as np
import matplotlib.pyplot as plt
from numpy.random import uniform, exponential
import os

# additional packages
from lifelines.plotting import plot_lifetimes
import sys
sys.path.append(os.path.join('..', '..', 'Utilities'))

try:
# Import formatting commands if directory "Utilities" is available
    from ISP_mystyle import setFonts
    
except ImportError:
# Ensure correct performance otherwise
    def setFonts(*options):
        return
    
# Generate some dummy data
np.set_printoptions(precision=2)
N = 20
study_duration = 12

# Note: a constant dropout rate is equivalent to an exponential distribution!
actual_subscriptiontimes = np.array([[exponential(18), exponential(3)][uniform()<0.5] for i in range(N)])
observed_subscriptiontimes = np.minimum(actual_subscriptiontimes,study_duration)
observed= actual_subscriptiontimes < study_duration

# Show the data
setFonts(18)
plt.xlim(0,24)
plt.vlines(12, 0, 30, lw=2, linestyles="--")
plt.xlabel('time')
plt.title('Subscription Times, at $t=12$  months')
plot_lifetimes(observed_subscriptiontimes, event_observed=observed)

print("Observed subscription time at time %d:\n"%(study_duration), observed_subscriptiontimes)
