'''Sketch to indicate why the sample SD underestimates the population SD '''

# Copyright(c) 2015, Thomas Haslwanter. All rights reserved, under the CC BY-SA 4.0 International License

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
    
# Set up the three axes
fig, axs = plt.subplots(3,1)

# Data for the "wide" distribution
x_wide = np.linspace(-10,10,201)
gauss_wide = stats.norm(0,3).pdf(x_wide)

# Points for the narrow distribution
data = np.array([-1,1])

# On each of the three plots, plot a normal distribution fitted to the (two) datapoints:
for index, offset in enumerate([-3,0,3]):
    curData = data + offset
    fitPars = stats.norm.fit(curData)
    axs[index].plot(x_wide, gauss_wide, color='r', lw=2, ls='--')
    axs[index].plot(curData, 0.005+np.zeros_like(curData), 'bo')
    axs[index].plot(x_wide, stats.norm(*fitPars).pdf(x_wide))
    axs[index].set_yticks([])

# Save and show
outFile = 'fig_SDunderestimation.png'
showData(outFile)
