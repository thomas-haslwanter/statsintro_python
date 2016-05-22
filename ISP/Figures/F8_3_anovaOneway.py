''' Figure explaining the T-Test '''

# Copyright(c) 2015, Thomas Haslwanter. All rights reserved, under the CC BY-SA 4.0 International License

# Import standard packages
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import os
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

sns.set_palette('muted')

def show_fig(std, ax, title):
    '''Create a plot of normally distributed data in a given axis'''
    
    for ii in range(3):
        data = stats.norm(centers[ii], std).rvs(numData)
        offset = ii*numData
        ax.plot( offset+np.arange(numData), data, '.', ms=10)
        
    ax.xaxis.set_ticks([50,150,250])
    ax.set_xticklabels(['Group1', 'Group2', 'Group3'])
    ax.set_title(title)
    sns.despine()

if __name__ == '__main__':
    
    # Set up the figure
    sns.set_context('paper')
    sns.set_style('whitegrid')
    setFonts(14)
    
    # Create 2 plots of 3 different, normally distributed data groups, with different SDs
    fig, axs = plt.subplots(1, 2)
    centers = [5, 5.3, 4.7]
    stds = [0.1, 2]
    numData = 100
    show_fig(0.1, axs[0], 'SD=0.1')
    show_fig(2,   axs[1], 'SD=2.0')
    
    showData('anova_oneway.png')
