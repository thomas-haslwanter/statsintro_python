'''Figure for a an example of a T-test for a mean value '''

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

sns.set_context('poster')
sns.set_style('ticks')
setFonts()

# Generate the data
np.random.seed(1234)
nd = stats.norm(100, 20)
scores = nd.rvs(10)

# Make the plot
plt.plot(scores, 'o')
plt.axhline(110, ls='--')
plt.axhline(np.mean(scores), ls='-.')
plt.xlim(-0.2, 9.2)
plt.ylim(50, 130)
plt.xlabel('Student-Nr')
plt.ylabel('Score')

outFile = 'fig_ExampleTtest.png'
showData(outFile)
