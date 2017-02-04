''' Demonstration of the probplot of a non-normal distribution '''

# Copyright(c) 2015, Thomas Haslwanter. All rights reserved, under the CC BY-SA 4.0 International License

# Import standard packages
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import seaborn as sns

# additional packages
# Import formatting commands if directory "Utilities" is available
import os
import sys
sys.path.append(os.path.join('..', 'Code_Quantlets', 'Utilities'))
try:
    from ISP_mystyle import setFonts, showData 
    
except ImportError:
# Ensure correct performance otherwise
    def setFonts(*options):
        return
    def showData(*options):
        plt.show()
        return

def generate_probplot():
    '''Generate a prob-plot for a chi2-distribution of sample data'''
    # Define the skewed distribution
    chi2 = stats.chi2(3)
    
    # Generate the data
    x = np.linspace(0,10, 100)
    y = chi2.pdf(x)
    np.random.seed(12345)
    numData = 100
    data = chi2.rvs(numData)
    
    # Arrange subplots
    sns.set_context('paper')
    sns.set_style('white')
    setFonts(11)
    fig, axs = plt.subplots(1,2)
    
    # Plot distribution
    axs[0].plot(x,y)
    axs[0].set_xlabel('X')
    axs[0].set_ylabel('PDF(X)')
    axs[0].set_title('chi2(x), k=3')
    sns.set_style('white')
    
    x0, x1 = axs[0].get_xlim()
    y0, y1 = axs[0].get_ylim()
    axs[0].set_aspect((x1-x0)/(y1-y0))
    
    
    # Plot probplot
    plt.axes(axs[1])
    stats.probplot(data, plot=plt)
    
    x0, x1 = axs[1].get_xlim()
    y0, y1 = axs[1].get_ylim()
    axs[1].axhline(0, lw=0.5, ls='--')
    axs[1].axvline(0, lw=0.5, ls='--')
    axs[1].set_aspect((x1-x0)/(y1-y0))
    
    showData('chi2pp.png')
    
    return(data)
    '''
    # To get an idea how probplot works, calculate the quantiles directly.
    # in "probplot", Filliben's estimate is used, which changes the values slightly
    data.sort()
    mark_y = data[:-1]
    
    nd = stats.norm()
    mark_x = nd.ppf(np.arange(1,len(data))/numData)
    axs[1].plot(mark_x, mark_y, 'rx-')
    '''
    
def KS_principle(inData):
    '''Show the principle of the Kolmogorov-Smirnov test.'''
    
    # CDF of normally distributed data
    nd = stats.norm()
    nd_x = np.linspace(-4, 4, 101)
    nd_y = nd.cdf(nd_x)
    
    # Empirical CDF of the sample data, which range for approximately 0 to 10
    numPts = 50
    lowerLim = 0
    upperLim = 10
    ecdf_x = np.linspace(lowerLim, upperLim, numPts)
    ecdf_y = stats.cumfreq(data, numPts, (lowerLim, upperLim))[0]/len(inData)
    
    #Add zero-point by hand
    ecdf_x = np.hstack((0., ecdf_x))
    ecdf_y = np.hstack((0., ecdf_y))
    
    # Plot the data
    sns.set_style('ticks')
    sns.set_context('poster')
    setFonts(36)
    
    plt.plot(nd_x, nd_y, 'k--')
    plt.hold(True)
    plt.plot(ecdf_x, ecdf_y, color='k')
    plt.xlabel('X')
    plt.ylabel('Cumulative Probability')
    
    # For the arrow, find the start
    ecdf_startIndex = np.min(np.where(ecdf_x >= 2))
    arrowStart = np.array([ecdf_x[ecdf_startIndex], ecdf_y[ecdf_startIndex]])
    
    nd_startIndex = np.min(np.where(nd_x >= 2))
    arrowEnd = np.array([nd_x[nd_startIndex], nd_y[nd_startIndex]])
    arrowDelta = arrowEnd - arrowStart
    
    plt.arrow(arrowStart[0], arrowStart[1], 0, arrowDelta[1],
              width=0.05, length_includes_head=True, head_length=0.04, head_width=0.4, color='k')
    
    plt.arrow(arrowStart[0], arrowStart[1]+arrowDelta[1], 0, -arrowDelta[1],
              width=0.05, length_includes_head=True, head_length=0.04, head_width=0.4, color='k')
    
    outFile = 'KS_Example.png'
    showData(outFile)
    
if __name__=='__main__':
    data = generate_probplot()    
    KS_principle(data)
    
