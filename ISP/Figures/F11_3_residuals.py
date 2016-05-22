'''Demo-plot of residuals to a best-fit line '''

# Copyright(c) 2015, Thomas Haslwanter. All rights reserved, under the CC BY-SA 4.0 International License

# Import standard packages
import numpy as np
import matplotlib.pyplot as plt

# additional packages
# Import formatting commands if directory "Utilities" is available
import os
import sys
sys.path.append(os.path.join('..', 'Code_Quantlets', 'Utilities'))
try:
    from ISP_mystyle import showData 
    
except ImportError:
# Ensure correct performance otherwise
    def showData(*options):
        plt.show()
        return

def main():
    # generate the data
    x = np.arange(10)
    np.random.seed(10)
    y = 3*x+2+20*np.random.rand(len(x))
    
    # determine the line-fit
    k,d = np.polyfit(x,y,1)
    yfit = k*x+d
    
    # plot the data
    plt.scatter(x,y)
    plt.hold(True)
    plt.plot(x, yfit, '--',lw=2)
    for ii in range(len(x)):
        plt.plot([x[ii], x[ii]], [yfit[ii], y[ii]], 'k')
        
    plt.xlim((-0.1, 9.1))
    plt.xlabel('X')
    plt.ylabel('Y')
    
    showData('residuals.png') 

if __name__ == '__main__':
    main()
