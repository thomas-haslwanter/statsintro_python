'''Show the origin of ROC-curves
ROC curves plot "sensitivity" against "1-specificity".
The example here uses two normally distributed groups, with a mean of 1 and 6,
respectively, and a standard deviation of 2.
'''

# Copyright(c) 2015, Thomas Haslwanter. All rights reserved, under the CC BY-SA 4.0 International License

# Import standard packages
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# additional packages
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

def arrow_bidir(ax, start, end, headWidth=0.01):
    '''Plot a bidirectional arrow'''
    
       # For the arrow, find the start
       
    start = np.array(start)
    end = np.array(end)
    delta = end - start
    
    ax.arrow(start[0], start[1], delta[0], delta[1],
              width=headWidth, length_includes_head=True, head_length=headWidth*3, head_width=headWidth*5, color='k')
    
    ax.arrow(end[0], end[1], -delta[0], -delta[1],
              width=headWidth, length_includes_head=True, head_length=headWidth*3, head_width=headWidth*5, color='k')

def main():
    # Calculate the PDF-curves
    x = np.linspace(-10, 15, 201)
    nd1 = stats.norm(1,2)
    nd2 = stats.norm(6,2)
    y1 = nd1.pdf(x)
    y2 = nd2.pdf(x)
    
    # Axes locations
    ROC = {'left': 0.35,
           'width': 0.36,
           'bottom': 0.1,
           'height': 0.47}
    
    PDF = {'left': 0.1,
           'width': 0.8,
           'bottom': 0.65,
           'height': 0.3}
           
    rect_ROC = [ROC['left'], ROC['bottom'], ROC['width'], ROC['height']]
    rect_PDF = [PDF['left'], PDF['bottom'], PDF['width'], PDF['height']]
    
    fig = plt.figure()
    
    ax1 = plt.axes(rect_PDF)
    ax2 = plt.axes(rect_ROC)
    
    # Plot and label the PDF-curves
    ax1.plot(x,y1)
    ax1.hold(True)
    ax1.fill_between(x,0,y1, where=x<3, facecolor='#CCCCCC', alpha=0.5)
    ax1.annotate('Sensitivity',
                 xy=(x[75], y1[65]),
                 xytext=(x[40], y1[75]*1.2), 
                 fontsize=14,
                 horizontalalignment='center',
                 arrowprops=dict(facecolor='#CCCCCC'))
    
    ax1.plot(x,y2,'#888888')
    ax1.fill_between(x,0,y2, where=x<3, facecolor='#888888', alpha=0.5)
    ax1.annotate('1-Specificity',
                 xy=(2.5, 0.03),
                 xytext=(6,0.05), 
                 fontsize=14,
                 horizontalalignment='center',
                 arrowprops=dict(facecolor='#888888'))
    
    ax1.set_ylabel('PDF')
    
    # Plot the ROC-curve
    ax2.plot(nd2.cdf(x), nd1.cdf(x), 'k')
    ax2.hold(True)
    ax2.plot(np.array([0,1]), np.array([0,1]), 'k--')
    
    # Format the ROC-curve
    ax2.set_xlim([0, 1])
    ax2.set_ylim([0, 1])
    ax2.axis('equal')
    ax2.set_title('ROC-Curve')
    ax2.set_xlabel('1-Specificity')
    ax2.set_ylabel('Sensitivity')
    
    arrow_bidir(ax2, (0.5,0.5), (0.095, 0.885))
    
    # Show the plot, and create a figure
    showData('ROC.png')    
    
if __name__ == '__main__':
    main()
