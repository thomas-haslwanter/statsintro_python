'''Visualization of the Sum-of-Squares. '''

# author: thomas haslwanter, date: Oct-2015

# Import standard packages
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# additional packages
import sys
sys.path.append(r'..\Quantlets\Utilities')
import ISP_mystyle
from matplotlib.patches import Rectangle

# Set the figure style
sns.set_context('poster')
sns.set_style('ticks')

# Generate data
yFit = lambda x: 1 + 0.5*x
x = np.r_[1., 2., 5., 6.]
y = yFit(x) + np.r_[-0.1, 0.1, -0.5, 0.5]

# Derived values
yMean = np.mean(y)
fit = np.polyfit(x,y,1)
xSmooth = np.linspace(0.5, 6.5, 101)
ySmooth = np.polyval(fit, xSmooth)

fig, axs = plt.subplots(1,2)

# Plot the datapoints, re \bar{y}
axs[0].plot(x,y, 'o')
axs[0].plot(xSmooth, ySmooth)

axs[0].set_xlim([0,7])
axs[0].set_ylim([0, 6])
axs[0].set_aspect('equal')
axs[0].hlines(yMean, 0, 7, lw=0.5)
axs[0].text(0.5, yMean+0.1, r'$\bar{y}$', fontsize=24)
sns.despine(ax=axs[0])

for ii in range(len(y)):
    width = yMean - y[ii]
    rect = Rectangle( (x[ii], y[ii]), width=width, height=width, facecolor='r', alpha=0.2)
    axs[0].add_patch(rect)

# Plot the datapoints, re \hat{y}
axs[1].plot(x,y, 'o')
axs[1].plot(xSmooth, ySmooth)

axs[1].set_xlim([0,7])
axs[1].set_ylim([0, 6])
axs[1].set_aspect('equal')
sns.despine(ax=axs[1])

for ii in range(len(y)):
    width = np.polyval(fit, x[ii]) - y[ii]
    rect = Rectangle( (x[ii], y[ii]), width=width, height=width, facecolor='b', alpha=0.4)
    axs[1].add_patch(rect)

# Save and show
outFile = 'sumOfSquares.png'
ISP_mystyle.printout_plain(outFile)