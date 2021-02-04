""" Different continuous distribution functions.
- T-distribution
- F-distribution
- Chi2-distribution
- Exponential
- Weibull
"""

# author: Thomas Haslwanter, date: Feb-2021

# Import standard packages
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import seaborn as sns
import os

# additional packages
import sys
sys.path.append(os.path.join('..', '..', 'Utilities'))

try:
# Import formatting commands if directory "Utilities" is available
    from ISP_mystyle import showData 
    
except ImportError:
# Ensure correct performance otherwise
    def showData(*options):
        plt.show()
        return

sns.set(context='poster', style='ticks', palette='muted', font_scale=1.5)


def show_t():
    """Utility function to show T distributions"""
    
    t = np.linspace(-5, 5, 201)
    TVals = [1,5]
    
    normal = stats.norm.pdf(t)
    t1 = stats.t.pdf(t,1)
    t5 = stats.t.pdf(t,5)
    
    plt.plot(t,normal, '--',  label='normal')
    plt.plot(t, t1, label='df=1')
    plt.plot(t, t5, label='df=5')
    plt.legend()
        
    plt.xlim(-5,5)
    plt.title('T-Distribution')
    plt.xlabel('X')
    plt.ylabel('pdf(X)')
    plt.axis('tight')
    
    outFile = 'dist_t.png'
    showData(outFile)
    
    
def show_chi2():
    """Utility function to show Chi2 distributions"""
    
    t = np.linspace(0, 8, 201)
    Chi2Vals = [1,2,3,5]
    
    for chi2 in Chi2Vals:
        plt.plot(t, stats.chi2.pdf(t, chi2), label='k={0}'.format(chi2))
    plt.legend()
        
    plt.xlim(0,8)
    plt.title('Chi2-Distribution')
    plt.xlabel('X')
    plt.ylabel('pdf(X)')
    plt.axis('tight')
    
    outFile = 'dist_chi2.png'
    showData(outFile)
    
    
def show_f():
    """Utility function to show F distributions"""
    
    t = np.linspace(0, 3, 201)
    d1s = [1,2,5,100]
    d2s = [1,1,2,100]
    
    for (d1,d2) in zip(d1s,d2s):
        plt.plot(t, stats.f.pdf(t, d1, d2), label='F({0}/{1})'.format(d1,d2))
    plt.legend()
        
    plt.xlim(0,3)
    plt.title('F-Distribution')
    plt.xlabel('X')
    plt.ylabel('pdf(X)')
    plt.axis('tight')
    plt.legend()
        
    outFile = 'dist_f.png'
    showData(outFile)

    
def show_exp():
    """Utility function to show exponential distributions"""
    
    t = np.linspace(0, 3, 201)
    lambdas = [0.5, 1, 1.5]
    
    for par in lambdas:
        plt.plot(t, stats.expon.pdf(t, 0, par), label='$\lambda={0:3.1f}$'.format(par))
    plt.legend()
        
    plt.xlim(0,3)
    plt.title('Exponential-Distribution')
    plt.xlabel('X')
    plt.ylabel('pdf(X)')
    plt.axis('tight')
    plt.legend()
        
    outFile = 'dist_exp.png'
    showData(outFile)
    
    
def show_weibull():
    """Utility function to show Weibull distributions"""
    
    t = np.linspace(0, 2.5, 251)
    lambdaVal = 1
    ks = [0.5, 1, 1.5, 5]
    
    for k in ks:
        wd = stats.weibull_min(k)
        plt.plot(t, wd.pdf(t), label='k = {0:.1f}'.format(k))
        
    plt.xlim(0,2.5)
    plt.ylim(0,2.5)
    plt.title('Weibull-Distribution')
    plt.xlabel('X')
    plt.ylabel('pdf(X)')
    plt.legend()
        
    outFile = 'Weibull_PDF.png'
    showData(outFile)
    
    
if __name__ == '__main__':
    show_t()
    show_chi2()
    show_f()
    show_exp()
    show_weibull()
