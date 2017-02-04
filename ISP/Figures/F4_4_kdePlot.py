""" Plot showing the effekt of a Kernel-Density-Estimation (KDE). """

# Copyright(c) 2015, Thomas Haslwanter. All rights reserved, under the CC BY-SA 4.0 International License

# Import standard packages
from scipy import stats
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

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

# Generate normally distributed data
nd = stats.norm(0,1)
np.random.seed(12345)
data = nd.rvs(100)

x = np.linspace(-5, 5, 101)
pdf = nd.pdf(x)

# Calculate the KDE
sd = np.std(data, ddof=1)
h = (4/(3*100))**0.2
h_str = '{0:4.2f}'.format(h)

# Calculate the smoothed plots, with 3 different parameters
kde_small = stats.kde.gaussian_kde(data, 0.1)
kde = stats.kde.gaussian_kde(data, h)
kde_large = stats.kde.gaussian_kde(data, 1)

# Generate two plots: one KDE with rug-plot, and one with different parameters
sns.set_context('poster')
sns.set_style('ticks')
setFonts()
fig, axs = plt.subplots(1,2)
sns.distplot(data, rug=True, ax=axs[0])

axs[1].plot(x, pdf)
axs[1].plot(x, kde.evaluate(x), 'r')
axs[1].plot(x,kde_small.evaluate(x),'-', color=[0.8, 0.8, 0.8])
axs[1].plot(x,kde_large.evaluate(x),'--')
axs[1].legend(['exact', h_str, '0.1', '1.0'])
axs[1].set_ylim(0, 0.40)

# Save and show
showData('kdePlot.png')
plt.show()
