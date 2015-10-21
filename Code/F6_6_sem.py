'''Scatterplot of normally distributed data, with Standard Deviation and Standard Error'''

# author: Thomas Haslwanter, date: Sept-2015

# Import standard packages
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import seaborn as sns

# additional packages
import C2_8_mystyle
from F7_10_roc import arrow_bidir

# Generate the data
np.random.seed(123)
x = np.random.randn(100) + 5

# Calculate "standard devation" and "standard error" locations
sdVal = np.std(x, ddof=1)
seVal = stats.sem(x)
sd = np.mean(x) + sdVal*np.r_[-1, 1]
se = np.mean(x) + seVal*np.r_[-1, 1]

# Set up the plot
sns.set_style('ticks')
sns.set_context('poster')

# Plot the data
plt.plot(x,'.')
plt.axhline(np.mean(x))
plt.axhline(sd[0], ls='--')
plt.axhline(sd[1], ls='--')
plt.axhline(se[0], ls='--', color='r')
plt.axhline(se[1], ls='--', color='r')

# Make the arrows
plt.arrow(10, np.mean(x), 0, sdVal,
    width=0.2, length_includes_head=True, head_length=0.2, head_width=1, color='k')
plt.arrow(10, np.mean(x), 0, -sdVal,
    width=0.2, length_includes_head=True, head_length=0.2, head_width=1, color='k')

plt.arrow(35, np.mean(x)-4*seVal, 0, 3*seVal,
    width=0.2, length_includes_head=True, head_length=0.1, head_width=1, color='k')
plt.arrow(35, np.mean(x)+4*seVal, 0, -3*seVal,
    width=0.2, length_includes_head=True, head_length=0.1, head_width=1, color='k')

#plt.text(10, 5.5, '$\pm$ 1SD', family='sans-seriv', fontsize=28)
#plt.text(35, 5.2, '$\pm$ 1SEM', family='sans-seriv', fontsize=28)
plt.text(10, 5.5, '$\pm$ 1SD', fontsize=28)
plt.text(35, 5.2, '$\pm$ 1SEM', fontsize=28)
plt.annotate('mean', (70,np.mean(x)),xycoords='data', fontsize=28, 
                xytext=(75, 5.5), textcoords='data',
                arrowprops=dict(facecolor='black', shrink=0.05))


# Add the text


# Save and show
outFile = ('standardError.png')
C2_8_mystyle.printout_plain(outFile)
