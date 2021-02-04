""" Simple manipulations of normal distribution functions.
- Different displays of normally distributed data
- Compare different samples from a normal distribution
- Work with the cumulative distribution function (CDF)
"""

# author: Thomas Haslwanter, date: Feb-2021

# Import standard packages
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import os
import seaborn as sns

import sys
sys.path.append(os.path.join('..', '..', 'Utilities'))

try:
# Import formatting commands if directory "Utilities" is available
    from ISP_mystyle import showData 
    
except ImportError:
# Ensure correct performance otherwise
    def showData(*options):
        plt.show()
        return

# General formatting options
#sns.set(context='poster', style='ticks', palette='muted')


def simple_normal() -> None:
    """ Different aspects of a normal distribution"""
    
    # Generate the data
    x = np.arange(-4,4,0.1) # generate the desirded x-values
    x2 = np.arange(0,1,0.001)

    nd = stats.norm()   # First simply define the normal distribution;
                        # don't calculate any values yet

    
    # This is a more complex plot-layout: the first row
    # is taken up completely by the PDF
    ax = plt.subplot2grid((3,2),(0,0), colspan=2)

    plt.plot(x,nd.pdf(x))
    plt.xlim(-4, 4)
    plt.gca().xaxis.set_ticks_position('bottom')
    plt.gca().yaxis.set_ticks_position('left')
    plt.yticks(np.linspace(0, 0.4, 5))
    plt.title('Normal Distribution - PDF: Probability Density Fct')
    
    # CDF
    plt.subplot(323)
    plt.plot(x,nd.cdf(x))
    plt.gca().xaxis.set_ticks_position('bottom')
    plt.gca().yaxis.set_ticks_position('left')
    plt.xlim(-4, 4)
    plt.ylim(0, 1)
    plt.vlines(0, 0, 1, linestyles='--')
    plt.title('CDF: Cumulative Distribution Fct')
    
    # SF
    plt.subplot(324)
    plt.plot(x,nd.sf(x))
    plt.gca().xaxis.set_ticks_position('bottom')
    plt.gca().yaxis.set_ticks_position('left')
    plt.xlim(-4, 4)
    plt.ylim(0, 1)
    plt.vlines(0, 0, 1, linestyles='--')
    plt.title('SF: Survival Fct')
    
    # PPF
    plt.subplot(325)
    plt.plot(x2,nd.ppf(x2))
    plt.gca().xaxis.set_ticks_position('bottom')
    plt.gca().yaxis.set_ticks_position('left')
    plt.yticks(np.linspace(-4,4,5))
    plt.hlines(0, 0, 1, linestyles='--')
    plt.xlim(0, 1)
    plt.ylim(-4, 4)
    plt.title('PPF: Percentile Point Fct')

    # ISF
    plt.subplot(326)
    plt.plot(x2,nd.isf(x2))
    plt.gca().xaxis.set_ticks_position('bottom')
    plt.gca().yaxis.set_ticks_position('left')
    plt.yticks(np.linspace(-4,4,5))
    plt.hlines(0, 0, 1, linestyles='--')
    plt.title('ISF: Inverse Survival Fct')
    plt.xlim(0, 1)
    plt.ylim(-4, 4)
    plt.tight_layout()
    
    outFile = 'DistributionFunctions.png'
    showData(outFile)
    

def shifted_normal() -> None:
    """PDF and scatter plot"""
    
    # Plot 3 PDFs (Probability density functions) for normal distributions 
    
    # Select 3 mean values, and 3 SDs
    myMean = [0,0,0,-2]
    mySD = [0.2,1,5,0.5]
    t = np.linspace(-5, 5, 201)
    
    # Plot the 3 PDFs, using the color-palette "hls"
    with sns.color_palette('hls', 4):
        for mu,sigma in zip(myMean, np.sqrt(mySD)):
            y = stats.norm.pdf(t, mu, sigma)
            plt.plot(t, y, label=f'$\mu={mu}, \; \t\sigma={sigma:3.1f}$')
        
    # Format the plot
    plt.legend()
    plt.xlim([-5,5])
    plt.title('Normal Distributions')
    
    # Show the plot, and save the out-file
    outFile = 'Normal_Distribution_PDF.png'
    showData(outFile)
    
    # Generate random numbers with a normal distribution -----------------
    myMean = 0
    mySD = 3
    numData = 500
    data = stats.norm.rvs(myMean, mySD, size = numData)
    
    # Plot the data
    plt.scatter(np.arange(len(data)), data)
    
    # Format the plot
    plt.title('Normally distributed data')
    plt.xlim([0,500])
    plt.ylim([-10,10])
    plt.show()
    plt.close()
    
    
def many_normals() -> None:
    """Show the histograms of 25 samples distributions,
    and compare the mean values """
    
    # Set the parameters
    numRows = 5
    numData = 100
    myMean = 0
    mySD = 1
    
    # Plot the histograms of the sample distributions, and format the plots
    plt.figure()
    for ii in range(numRows):
        for jj in range(numRows):
            data = stats.norm.rvs(myMean, mySD, size=numData)
            plt.subplot(numRows,numRows,numRows*ii+jj+1)
            plt.hist(data, edgecolor='k', lw=0.5)
            plt.gca().set_xlim([-3, 3])
            plt.gca().set_xticks(())
            plt.gca().set_yticks(())
            plt.gca().set_xticklabels(())
            plt.gca().set_yticklabels(())
    
    plt.tight_layout()
    
    # Show the data, and save the out-file
    outFile = 'Normal_MultHist.png'
    showData(outFile)
    
    # Check out the mean of 1000 normal sample distributions
    numTrials = 1000;
    numData = 100
    
    # Pre-allocate the memory for the output variable
    myMeans = np.ones(numTrials)*np.nan
    
    for ii in range(numTrials):
        data = stats.norm.rvs(myMean, mySD, size=numData)
        myMeans[ii] = np.mean(data)
    se = np.std(myMeans)
    print('The standard error of the mean, with {numData} samples, is {se}')

    
def values_fromCDF():
    """Calculate an empirical cumulative distribution function, compare it with
    the exact one, and find the exact point for a specific data value."""
    
    # Generate normally distributed random data
    myMean = 5
    mySD = 2
    numData = 100
    data = stats.norm.rvs(myMean, mySD, size=numData)
    
    # Calculate the cumulative distribution function, CDF
    numbins = 20
    counts, bin_edges = np.histogram(data, bins=numbins, normed=True)
    cdf = np.cumsum(counts)
    cdf /= np.max(cdf)
    
    # compare with the exact CDF
    plt.step(bin_edges[1:],cdf)
    x = np.arange(-5,15,0.1)
    plt.plot(x, stats.norm.cdf(x, myMean, mySD),'r')
    
    # Find out the value corresponding to the x-th percentile: the
    # "cumulative distribution function"
    value = 2
    myMean = 5
    mySD = 2
    cdf = stats.norm.cdf(value, myMean, mySD)
    print(f'With a threshold of {value:4.2f}' +
          ' you get {round(cdf*100)}% of the data')
    
    # For the percentile corresponding to a certain value: 
    # the "inverse cumulative distribution function" 
    value = 0.025
    icdf = stats.norm.isf(value, myMean, mySD)
    print(f'To get {(1-value)*100}% of the data' +
           f' you need a threshold of {icdf:4.2f}.')
    plt.show()

    
if __name__ == '__main__':
    many_normals()
    simple_normal()
    sns.set(font_scale=1.5, style='white')
    values_fromCDF()
    shifted_normal()

