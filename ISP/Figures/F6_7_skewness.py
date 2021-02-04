""" Example for Skewness and Kurtosis """

# author: Thomas Haslwanter, date: Feb-2021

# Import standard packages
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import os
import seaborn as sns

# Import formatting commands if directory "Utilities" is available
import os
import sys
sys.path.append(os.path.join('..', 'Code_Quantlets', 'Utilities'))
try:
    from ISP_mystyle import showData 
    
except ImportError:
# Ensure correct performance otherwise
    def showData(*options):
        plt.show()
        return

sns.set(context='notebook', style='ticks', palette='deep')


def skewness(ax):
    """Normal and skewed distribution"""
    
    t = np.linspace(-6, 10, 201) # generate the desired x-values
    normal = stats.norm.pdf(t, 1, 1.6)   
    chi2 = stats.chi2.pdf(t, 3)
    
    ax.plot(t, normal, '--', label='normal')
    ax.plot(t, chi2, label='positive skew')
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')
    ax.margins(0,0)
    ax.legend()
    
    
def kurtosis(ax):
    """ Distributions with different kurtosis"""
    
    # Generate the data
    t = np.linspace(-3, 3, 201) # generate the desired x-values
    platykurtic = stats.laplace.pdf(t)
    
    wigner = np.zeros(np.size(t))
    wignerIndex = np.abs(t) <= 1
    wigner[wignerIndex] = 2/np.pi * np.sqrt(1-t[wignerIndex]**2)
    
    ax.plot(t, platykurtic, label='kurtosis=3')
    ax.plot(t, wigner, '--', label='kurtosis=-1')
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')
    ax.margins(0,0)
    ax.legend()

    
if __name__=='__main__':
    # Make 2 plots, side-by-side
    fig, axs = plt.subplots(1,2)    
    
    # In the first plot demonstrate "skewness", in the second plot "kurtosis"
    skewness(axs[0])
    kurtosis(axs[1])    

    # Save and show
    outFile = 'Skewness.png'
    showData(outFile)
