''' Paired T-test
'''

# Copyright(c) 2015, Thomas Haslwanter. All rights reserved, under the CC BY-SA 4.0 International License

# Import standard packages
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

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
x = np.r_[3, 1.5, 4, 6, 3, 2]
dx = np.r_[0.1, 0.3, 0.2, 0.2, 0.3, 0.25]
xs = x-dx
index = range(len(x))

# plot the data
setFonts(20)
plt.plot(x, 'o', ms=10, label='pre')
plt.plot(xs, 'r*', ms=12, label='post')
plt.bar(index, dx, width=0.5, align='center',
        color=0.75*np.ones(3), label='pre-post')

# Format the plot
plt.legend(loc='upper left')
plt.axhline(0, ls='--')
plt.xlim(-0.3, 5.3)
plt.ylim(-0.2, 6.2)
plt.xlabel('Subject Nr')
plt.ylabel('Value')
plt.tight_layout()

# P-values for paired and unpaired T-tests
_, p_paired = stats.ttest_rel(x, xs)
_, p_ind = stats.ttest_ind(x, xs)
print('A paired comparison yields p={0:.4f}, while an unpaired T-test gives us p={1:.3f}'.format(p_paired, p_ind))

# Show and save figure
outFile = 'pairedTtest.png'
showData(outFile)
