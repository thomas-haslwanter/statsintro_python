'''
Practical demonstration of the central limit theorem, based on the uniform distribution

'''

# author: Thomas Haslwanter, date: July-2015

# Import standard packages
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

# additional packages
import C2_8_mystyle

# Formatting options
sns.set(context='poster', style='ticks')

def main():
    '''Demonstrate central limit theorem.'''
    # Generate data
    ndata = 1e5
    nbins = 50
    data = np.random.random(ndata)
    
    # Show three graphs, side-by-side
    fig, axs = plt.subplots(1,3)
    
    axs[0].hist(data,bins=nbins)
    axs[0].set_title('Random data')
    axs[0].set_xticks([0, 0.5, 1])
    axs[0].set_ylabel('Counts')
    
    axs[1].hist( np.mean(data.reshape((ndata/2,2)),  axis=1), bins=nbins)
    axs[1].set_xticks([0, 0.5, 1])
    axs[1].set_title(' Average over 2')
    
    axs[2].hist( np.mean(data.reshape((ndata/10,10)),axis=1), bins=nbins)
    axs[2].set_xticks([0, 0.5, 1])
    axs[2].set_title(' Average over 10')
    
    plt.tight_layout()
    C2_8_mystyle.printout_plain('CentralLimitTheorem.png')
    
if __name__ == '__main__':
   main() 
