"""
Graphical and quantitative check, if a given distribution is normal.
- For small sample-numbers (<50), you should use the Shapiro-Wilk test or the
    "normaltest"
- for intermediate sample numbers, the Lilliefors-test is good since the
    original Kolmogorov-Smirnov-test is unreliable when mean and std of the
    distribution are not known.
- the Kolmogorov-Smirnov(Kolmogorov-Smirnov) test should only be used for
    large sample numbers (>300)
"""

# author: Thomas Haslwanter, date: Feb-2021

# Import standard packages
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
import pandas as pd

# additional packages
from statsmodels.stats.diagnostic import lilliefors
from typing import List


def generate_data(show_flag:bool=True) -> np.ndarray:
    """Generates input data for the function 'check_normality'
    
    Parameters
    show_flag : Controls the display of the generated data
    
    
    Returns
    -------
    data : vector with random data
    """
    
    # Set the parameters
    numData = 1000
    myMean = 0
    mySD = 3
    
    # To get reproducable values, I provide a seed value
    np.random.seed(1234)   
    
    # Generate and show random data
    data = stats.norm.rvs(myMean, mySD, size=numData)
    
    if show_flag:
        plt.hist(data)
        plt.show()
    
    return data


def check_normality(data: np.ndarray, show_flag: bool=True) -> List[float]:
    """Check if the distribution is normal

    Parameters
    ----------
    data : vector of data to be tested
    show_flag : controls the display of data

    Returns
    -------
    ps : List of p-values for different normality tests
    """
    
    few_data = data[::10]

    # --- >>> START stats <<< ---
    # Graphical test: if the data lie on a line, they are pretty much
    # normally distributed
    if show_flag:
        _ = stats.probplot(data, plot=plt)
        plt.show()

    pVals = pd.Series()
    pFewVals = pd.Series()
    # The scipy normaltest is based on D-Agostino and Pearsons test that
    # combines skew and kurtosis to produce an omnibus test of normality.
    _, pVals['Omnibus']    = stats.normaltest(data)
    _, pFewVals['Omnibus'] = stats.normaltest(few_data)

    # Shapiro-Wilk test
    _, pVals['Shapiro-Wilk']    = stats.shapiro(data)
    _, pFewVals['Shapiro-Wilk'] = stats.shapiro(few_data)
    
    # Or you can check for normality with Lilliefors-test
    _, pVals['Lilliefors']    = lilliefors(data)
    _, pFewVals['Lilliefors'] = lilliefors(few_data)
    
    # Alternatively with original Kolmogorov-Smirnov test
    _, pVals['Kolmogorov-Smirnov']    = \
            stats.kstest((data-np.mean(data))/np.std(data,ddof=1), 'norm')
    _, pFewVals['Kolmogorov-Smirnov'] = \
        stats.kstest((few_data-np.mean(few_data))/np.std(few_data,ddof=1), 'norm')
    
    print(f'p-values for all {len(data)} data points: ----------------')
    print(pVals)
    print('p-values for the first 100 data points: ----------------')
    print(pFewVals)
    
    if pVals['Omnibus'] > 0.05:
        print('Data are normally distributed')
    # --- >>> STOP stats <<< ---
    
    return pVals
    

if __name__ == '__main__':

    data = generate_data()
    ps = check_normality(data)
    input('Done!')

