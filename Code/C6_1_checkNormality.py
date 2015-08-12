'''
Graphical and quantitative check, if a given distribution is normal.
- For small sample-numbers (<50), you should use the Shapiro-Wilk test or the "normaltest"
- for intermediate sample numbers, the Lilliefors-test is good since the original KS-test is unreliable when mean and std of the distribution
are not known.
- the Kolmogorov-Smirnov(KS) test should only be used for large sample numbers (>300)

'''

# author: Thomas Haslwanter, date: May-2014

# Import standard packages
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
import pandas as pd

# additional packages
from statsmodels.stats.diagnostic import kstest_normal

def check_normality():
    '''Check if the distribution is normal.'''
    # Set the parameters
    numData = 100
    myMean = 0
    mySD = 3
    
    # To get reproducable values, I provide a seed value
    np.random.seed(987654321)   
    
    # Generate and show random data
    data = stats.norm.rvs(myMean, mySD, size=numData)
    plt.hist(data)
    plt.show()

    # --- >>> START stats <<< ---
    # Graphical test: if the data lie on a line, they are pretty much
    # normally distributed
    _ = stats.probplot(data, plot=plt)
    plt.show()

    pVals = pd.Series()
    # The scipy normaltest is based on D-Agostino and Pearsons test that
    # combines skew and kurtosis to produce an omnibus test of normality.
    _, pVals['omnibus'] = stats.normaltest(data)

    # Shapiro-Wilk test
    _, pVals['Shapiro-Wilk'] = stats.shapiro(data)
    
    # Or you can check for normality with Lilliefors-test
    ksStats, pVals['Lilliefors'] = kstest_normal(data)
    
    # Alternatively with original Kolmogorov-Smirnov test
    _, pVals['KS'] = stats.kstest((data-np.mean(data))/np.std(data,ddof=1), 'norm')
    
    print(pVals)
    if pVals['omnibus'] > 0.05:
        print('Data are normally distributed')
    # --- >>> STOP stats <<< ---
    
    return pVals['KS']
    
if __name__ == '__main__':
    p = check_normality()    

