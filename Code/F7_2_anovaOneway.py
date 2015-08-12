'''
Figure explaining the T-Test

'''

# author: Thomas Haslwanter, date: May-2014

# Import standard packages
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import os
import seaborn as sns

# additional packages
import C2_8_mystyle

def show_fig(std, ax, title):
    '''Create plot of 3 different, normally distributed data groups'''
    for ii in range(3):
        data = stats.norm(centers[ii], std).rvs(numData)
        offset = ii*numData
        ax.plot( offset+np.arange(numData), data, '.', color=colors[ii], ms=10)
        
    ax.xaxis.set_ticks([50,150,250])
    ax.set_xticklabels(['Group1', 'Group2', 'Group3'])
    ax.set_title(title)
    sns.despine()

if __name__ == '__main__':
    centers = [5, 5.3, 4.7]
    colors = 'brg'
    
    sns.set_context('paper')
    sns.set_style('whitegrid')
    C2_8_mystyle.set(14)
    
    fig, axs = plt.subplots(1, 2)
    stds = [0.1, 2]
    numData = 100
    show_fig(0.1, axs[0], 'SD=0.1')
    show_fig(2,   axs[1], 'SD=2.0')
    
    C2_8_mystyle.printout_plain('anova_oneway.png')
    
    plt.show()

