'''Figure for a an example of a T-test for a mean value '''

# author: Thomas Haslwanter, date: Sept-2015

# Import standard packages
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import seaborn as sns

# additional packages
import C2_8_mystyle

sns.set_context('poster')
sns.set_style('ticks')

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
C2_8_mystyle.printout_plain(outFile)
