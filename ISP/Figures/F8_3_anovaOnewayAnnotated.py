""" Figure explaining the T-Test """

# author: Thomas Haslwanter, date: Feb-2021

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
    
sns.set(context='notebook', style='ticks', palette='muted')


def show_fig(std, ax, title):
    """Create plot of 3 different, normally distributed data groups"""
    
    groupMean = []
    for ii in range(3):
        data = stats.norm(centers[ii], std).rvs(numData)
        offset = ii*numData
        ax.plot( offset+np.arange(numData), data, '.', ms=18)
        groupMean.append(np.mean(data))
        
    ax.xaxis.set_ticks([50,150,250])
    ax.set_xticklabels(['Group1', 'Group2', 'Group3'])
    ax.yaxis.set_ticks([])
    ax.set_title(title)
    
    grandMean = np.mean(groupMean)
    gray = '#999999'
    arrowprops = dict(arrowstyle = '<->', facecolor='black', color=gray)
    
    ax.axhline(grandMean, color=gray)
    ax.plot([80, 220], [groupMean[1], groupMean[1]], color=gray)
    ax.plot([80, 120], [groupMean[1]+0.2, groupMean[1]+0.2], color=gray)
    ax.annotate('', xy=(210, grandMean), xytext=(210,groupMean[1]), 
            arrowprops=arrowprops )
    ax.annotate('', xy=(90, groupMean[1]), xytext=(90,groupMean[1]+0.2), 
            arrowprops=arrowprops )
    ax.text(210, (grandMean + groupMean[1])/2., '$SS_{Treatment}$', fontsize=18)
    ax.text(90, groupMean[1]+0.1, '$SS_{Error}$', ha='right', fontsize=18)

    
if __name__ == '__main__':
    centers = [5, 5.3, 4.7]
    
    np.random.seed(123)
    setFonts(18)
    
    fig = plt.figure()
    ax = fig.add_subplot(111)
    std = 0.1
    numData = 100
    show_fig(0.1, ax, 'Sum-Squares')
    
    # Save and show
    showData('anova_annotated.png')
