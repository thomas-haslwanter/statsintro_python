''' Example for Skewness and Kurtosis

'''

# author: Thomas Haslwanter, date: Nov-2014

# Import standard packages
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import os
import seaborn as sns

# additional packages
from matplotlib.mlab import frange

sns.set(context='poster', style='ticks', palette='deep')

def skewness(ax):
    '''Normal and skewed distribution'''
    
    t = frange(-6,10,0.1) # generate the desirded x-values
    normal = stats.norm.pdf(t,1,1.6)   
    chi2 = stats.chi2.pdf(t,3)
    
    ax.plot(t, normal, '--', label='normal')
    ax.plot(t, chi2, label='positive skew')
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')
    ax.legend()
    
def kurtosis(ax):
    ''' Distributions with different kurtosis'''
    
    # Generate the data
    t = frange(-3,3,0.1) # generate the desirded x-values
    platykurtic = stats.laplace.pdf(t)
    
    wigner = np.zeros(np.size(t))
    wignerIndex = np.abs(t) <= 1
    wigner[wignerIndex] = 2/np.pi * np.sqrt(1-t[wignerIndex]**2)
    
    ax.plot(t, platykurtic, label='kurtosis=3')
    ax.plot(t, wigner, '--', label='kurtosis=-1')
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')
    ax.legend()

if __name__=='__main__':
    fig, axs = plt.subplots(1,2)    
    
    skewness(axs[0])
    kurtosis(axs[1])    
    
    outDir = r'..\Images'
    outFile = 'Skewness.png'
    
    saveTo = os.path.join(outDir, outFile)
    plt.savefig(saveTo, dpi=200)
    
    print('OutDir: {0}'.format(outDir))
    print('Figure saved to {0}'.format(outFile))
    plt.show()
