
```yaml
Name of QuantLet: ISP_centralLimitTheorem

Published in:  An Introduction to Statistics with Python

Description: Practical demonstration of the central limit theorem, based on the uniform distribution

Keywords: CLT, normal-distribution, normal approximation, simulation, uniform, distribution

See also: 

Author: Thomas Haslwanter

Submitted: October 31, 2015

Example: CentralLimitTheorem.png

```


![Picture1](CentralLimitTheorem.png)


```py
''' Practical demonstration of the central limit theorem, based on the uniform distribution '''

# author: Thomas Haslwanter, date: Aug-2015

# Import standard packages
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

# additional packages
import sys
sys.path.append(r'..\..\Utilities')
import ISP_mystyle

# Formatting options
sns.set(context='poster', style='ticks', palette='muted')

# Input data
ndata = 1e5
nbins = 50

def showAsHistogram(axis, data, title):
    '''Subroutine showing a histogram and formatting it'''
    
    axis.hist( data, bins=nbins)
    axis.set_xticks([0, 0.5, 1])
    axis.set_title(title)

def main():
    '''Demonstrate central limit theorem.'''
    
    ISP_mystyle.set(24)
    # Generate data
    data = np.random.random(ndata)
    
    # Show three histograms, side-by-side
    fig, axs = plt.subplots(1,3)
    
    showAsHistogram(axs[0], data, 'Random data')
    showAsHistogram(axs[1], np.mean(data.reshape((ndata/2, 2 )), axis=1), 'Average over 2')
    showAsHistogram(axs[2], np.mean(data.reshape((ndata/10,10)), axis=1), 'Average over 10')
    
    # Format them and show them
    axs[0].set_ylabel('Counts')
    plt.tight_layout()
    ISP_mystyle.printout_plain('CentralLimitTheorem.png')
    
if __name__ == '__main__':
   main() 

```
