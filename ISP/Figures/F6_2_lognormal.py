''' Lognormal distribution functions. '''

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

# Generate the data
x = np.logspace(-9,1,1001)+1e-9
lnd = stats.lognorm(2)
y = lnd.pdf(x)

# Generate 2 plots, side-by-side
sns.set_style('ticks')
setFonts(18)
fig, axs = plt.subplots(1,2, sharey=True)
sns.set_context('poster')

# Left plot: linear scale on x-axis
axs[0].plot(x,y)
axs[0].set_xlim(-0.5,8)
axs[0].set_xlabel('x')
axs[0].set_ylabel('pdf(x)')

# Right plot: logarithmic scale on x-axis
axs[1].plot(np.log(x), y)
axs[1].set_xlim(-12,5)
axs[1].set_xlabel('log(x)')

# Save and show
outFile = 'logNormal.png'
showData(outFile)
