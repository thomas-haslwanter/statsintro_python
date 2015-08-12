"""
Plot explaining the principle of a Kernel-Density-Estimation (KDE).

"""

# author: Thomas Haslwanter, date: May-2015

# Import standard packages
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# additional packages
import C2_8_mystyle

# Generate dummy data
x = np.array([-2.1, -1.3, -0.4, 1.9, 5.1, 6.2])

# Prepare cumulative arrays
xcum = np.arange(-6, 11, 0.1)
ycum = np.zeros_like(xcum)

# Left plot: histogram ------------------------
plt.subplot(121)

plt.hist(x, bins=6, range=[-4, 8], normed=True)

plt.xlim(-6, 11)
plt.ylim(-0.005, 0.18)
plt.xlabel('x')
plt.ylabel('Density Function')
plt.hold(True)

# Add rugplot
for ii in range(len(x)):
    plt.plot([x,x], [0, -0.005], 'b')    
    
# Explanation of KDE --------------------

# Width of the individual Gaussians
var = 2.25
sd = np.sqrt(var)

# Plot individual Gaussians
def plotNorm(pos, sd, xcum, ycum):
    # Individual curve
    x = np.arange(pos-3*sd, pos+3*sd, 0.1)
    nd = stats.norm(pos, sd)
    y = nd.pdf(x)
    plt.plot(x,y/10, 'r--')
    
    # Cumulative curve
    xcr = np.round(xcum*10)
    xir = np.round(x*10)
    for ii in range(len(xir)):
        ycum[xcr==xir[ii]] += y[ii]
    return ycum
    
# Right plot
plt.subplot(122)

# Format
plt.hold(True)
plt.xlim(-6, 11)
plt.ylim(-0.005, 0.18)
plt.xlabel('x')
plt.axhline(0)

# Rugplot & individual Gaussians
for ii in range(len(x)):
    plt.plot([x,x], [0, -0.005], 'b')    
    ycum = plotNorm(x[ii], sd, xcum, ycum)

# Plot cumulative curve
ycum /= np.sum(ycum)/10
plt.plot(xcum, ycum)

C2_8_mystyle.printout_plain('KDEexplained.png')
plt.show()
