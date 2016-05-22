''' Graphical display of PDF (probability density function) and CDF (cumulative density function) '''

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

# Calculate the values
nd = stats.norm()

x = np.linspace(-3,3,100)
yp = nd.pdf(x)
y = nd.cdf(x)
x1 = np.linspace(-3, 1)
y1 = nd.pdf(x1)

# Make the plot
sns.set_context('paper')
sns.set_style('white')
setFonts(12)

figs, axs = plt.subplots(1,2)

axs[0].plot(x,yp, 'k')
axs[0].fill_between(x1, y1, facecolor='#CCCCCC')
axs[0].text(0, 0.1, 'CDF(x)', family='cursive', fontsize=14, horizontalalignment='center', style='italic')
axs[0].set_xlabel('x')
axs[0].set_ylabel('PDF(x)')
sns.despine()

axs[1].plot(x, y, '#999999', lw=3)
axs[1].set_xlabel('x')
axs[1].set_ylabel('CDF(x)')
plt.vlines(0, 0, 1, linestyles='--')
sns.despine()

# Save and show
showData('PDF_CDF.png')
plt.show()
