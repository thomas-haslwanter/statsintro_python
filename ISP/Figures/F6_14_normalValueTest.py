""" Short demo of how to check for the significance of an individual value. """

# author: Thomas Haslwanter, date: Feb-2021

# Import standard packages
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import seaborn as sns
import os

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

# Generate a "frozen" the normal distribution
md, sd = 3.5, 0.76
nd = stats.norm(md, sd)

# Set up the plot
sns.set_context(context='notebook')
sns.set_style('ticks')
setFonts()

# Plot the normal distribution within 3 SDs
limits = (md-3*sd, md+3*sd)
num_pts = 200
x = np.linspace(limits[0], limits[1], num_pts)
y = nd.pdf(x)

# Shade the regions beyond a certain "checkVal"
checkVal = 2.6
print(f'p = {nd.cdf(checkVal):5.3f}')

x1 = np.linspace(limits[0], checkVal, num_pts)
y1 = nd.pdf(x1)
x2 = np.linspace(md + (md-checkVal), limits[1], num_pts)
y2 = nd.pdf(x2)

plt.plot(x,y)
plt.fill_between(x1, y1, alpha=0.5)
plt.fill_between(x2, y2, alpha=0.2)

#  Label the axes
plt.xlabel('Weight')
plt.ylabel('P(Weight)')
plt.text(2.1, 0.05, '11.8%', fontsize=18)

# Remove the right- and top-axis
sns.despine()
plt.gca().margins(0,0)

# Save and show
showData('pdf_checkValue.png')
