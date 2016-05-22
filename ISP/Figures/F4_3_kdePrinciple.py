""" Plot explaining the principle of a Kernel-Density-Estimation (KDE). """

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

setFonts(18)

def plot_histogram(ax, data):
    ''' Left plot: histogram '''
    
    ax.hist(data, bins=6, range=[-4, 8], normed=True)
    
    ax.set_xlim(-6, 11)
    ax.set_ylim(-0.005, 0.18)
    ax.set_xlabel('x')
    ax.set_ylabel('Density Function')
    plt.hold(True)
    
    # Add rugplot
    for ii in range(len(data)):
        ax.plot([data,data], [0, -0.005], 'b')    
    
def plotNorm(pos, sd, xcum, ycum):
    ''' Plot individual curves '''
    
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
    
def explain_KDE(ax, data):
    ''' Right plot: Explanation of KDE '''
    
    # Prepare cumulative arrays
    xcum = np.arange(-6, 11, 0.1)
    ycum = np.zeros_like(xcum)

    # Width of the individual Gaussians
    var = 2.25
    sd = np.sqrt(var)
    
    # Plot individual Gaussians
    ax.set_xlim(-6, 11)
    ax.set_ylim(-0.005, 0.18)
    ax.set_xlabel('x')
    ax.axhline(0)
    
    # Rugplot & individual Gaussians
    for ii in range(len(data)):
        ax.plot([data,data], [0, -0.005], 'b')    
        ycum = plotNorm(data[ii], sd, xcum, ycum)
    
    # Plot cumulative curve
    ycum /= np.sum(ycum)/10
    ax.plot(xcum, ycum)

def main():
    # Generate dummy data
    x = np.array([-2.1, -1.3, -0.4, 1.9, 5.1, 6.2])
    
    # Define the two plots
    fig, axs = plt.subplots(1,2)
    
    # Generate the left plot
    plot_histogram(axs[0], x)
    
    # Generate the right plot
    explain_KDE(axs[1], x)
    
    # Save and show
    showData('KDEexplained.png')
    plt.show()
    
if __name__ == '__main__':
    main()
    
