""" Figure with simple regression line """

# author: Thomas Haslwanter, date: Feb-2021

# Import standard packages
import numpy as np
import matplotlib.pyplot as plt
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

# additional packages
# Import formatting commands if directory "Utilities" is available
import os
import sys
sys.path.append(os.path.join('..', '..', 'Utilities'))
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
x = np.arange(-20, 80)
y = 10 + 0.2*x + 4*np.random.randn(len(x))

# Make the plot
sns.set_style('ticks')
sns.set_context('notebook')
setFonts()

fig = plt.figure()
ax = fig.add_subplot(111)

ax.plot(x,y,'.')
ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')

sns.despine()

# Draw the fitted line
p = np.polyfit(x,y, 1)
yFit = np.polyval(p, x)
ax.plot(x,yFit, 'r')

# Save and show
outFile = 'Linear_regression.png'
showData(outFile)
