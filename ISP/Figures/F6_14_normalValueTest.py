''' Short demo of how to check for the significance of an individual value. '''

# author: Thomas Haslwanter, date: Oct-2015

# Import standard packages
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import seaborn as sns
import os

# additional packages
import sys
sys.path.append(r'..\Quantlets\Utilities')
import ISP_mystyle

# Generate a "frozen" the normal distribution
md, sd = 3.5, 0.76
nd = stats.norm(md, sd)

# Set up the plot
sns.set_context(context='poster')
sns.set_style('ticks')
ISP_mystyle.set()

# Plot the normal distribution within 3 SDs
limits = (md-3*sd, md+3*sd)
x = np.linspace(limits[0], limits[1])
y = nd.pdf(x)

# Shade the regions beyond a certain "checkVal"
checkVal = 2.6
print('p = {0:5.3f}'.format(nd.cdf(checkVal)))

x1 = np.linspace(limits[0], checkVal)
y1 = nd.pdf(x1)
x2 = np.linspace(md + (md-checkVal), limits[1])
y2 = nd.pdf(x2)

plt.plot(x,y)
plt.fill_between(x1, y1, alpha=0.5)
plt.fill_between(x2, y2, alpha=0.2)

#  Label the axes
plt.xlabel('Weight')
plt.ylabel('P(Weight)')
plt.text(2.1, 0.05, '11.8%', fontsize=24)

# Remove the right- and top-axis
sns.despine()

# Save and show
ISP_mystyle.printout_plain('pdf_checkValue.png')