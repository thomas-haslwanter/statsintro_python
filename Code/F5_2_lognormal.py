
''' Lognormal distribution functions.

'''

# author: Thomas Haslwanter, date: July-2015


# Import standard packages
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import seaborn as sns
import C2_8_mystyle

x = np.logspace(-9,1,1001)+1e-9
lnd = stats.lognorm(2)
y = lnd.pdf(x)

sns.set_style('ticks')
C2_8_mystyle.set(18)
fig, axs = plt.subplots(1,2, sharey=True)
sns.set_context('poster')

axs[0].plot(x,y)
axs[0].set_xlim(-0.1,8)
axs[0].set_xlabel('x')
axs[0].set_ylabel('pdf(x)')

axs[1].plot(np.log(x), y)
axs[1].set_xlim(-12,5)
axs[1].set_xlabel('log(x)')

outFile = 'logNormal.png'
C2_8_mystyle.printout_plain(outFile)