""" Demonstration of the package "lifelines"

Based on the demo-code by Cam Davidson-Pilon (http://lifelines.readthedocs.org) 
"""

# author: Thomas Haslwanter, date: 2021-01-11

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
    
    
def main():
    # Generate some dummy data
    np.set_printoptions(precision=2)
    N = 20
    study_duration = 12
    
    # Note: a constant dropout rate is equivalent to an exponential distribution!
    subsciption_list = [ [exponential(18), exponential(3)][uniform()<0.5] \
            for i in range(N) ]
    actual_subscriptiontimes = np.array(subsciption_list)
    observed_subscriptiontimes = np.minimum(actual_subscriptiontimes,study_duration)
    observed= actual_subscriptiontimes < study_duration
    
    # Show the data
    setFonts(18)
    plt.xlim(0,24)
    plt.vlines(12, 0, 30, lw=2, linestyles="--")
    plt.xlabel('time')
    plt.title('Subscription Times, at $t=12$  months')
    plot_lifetimes(observed_subscriptiontimes, event_observed=observed)
    plt.show()
    
    print(f'Observed subscription time at time {study_duration:d}', \
            observed_subscriptiontimes)
    
    
if __name__ == '__main__':
    main()