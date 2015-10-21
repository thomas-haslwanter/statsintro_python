'''Introductions to using the statistical Python package "statsmodels" '''

# author: Thomas Haslwanter, date: Sept-2015

# Import standard packages
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import pandas as pd

# additional packages
import statsmodels.formula.api as sm
import sys

# Python 2/3 use different packages for "urlopen"
if sys.version_info[0] == 3:
    from urllib.request import urlopen
else:
    from urllib import urlopen

def simple_fit():
    ''' Example: Linear regression fit '''
    
    # To get reproducable values, I provide a seed value
    np.random.seed(987654321)   
    
    # Generate a noisy line, and save the data in a pandas-DataFrame
    x = np.arange(100)
    y = 0.5*x - 20 + np.random.randn(len(x))
    df = pd.DataFrame({'x':x, 'y':y})

    # Fit a linear model, using the "formula" language added by the package "patsy"
    model = sm.ols('y~x', data=df).fit()

    # ... and print the summary
    print( model.summary() )

    return model.params

def pandas_boxplot():
    '''Example from Altman "Practical statistics for medical research'''

    # Get the data
    inFile = 'altman_94.txt'
    url_base = 'https://raw.github.com/thomas-haslwanter/statsintro/master/Data/data_altman/'
    url = url_base + inFile
    data = np.genfromtxt(urlopen(url), delimiter=',')

    # Group them into "lean" and "obese"
    lean = pd.Series(data[data[:,1]==1,0])
    obese = pd.Series(data[data[:,1]==0,0])

    # Combine them into a pandas DataFrame
    df = pd.DataFrame({'lean':lean, 'obese':obese})

    # Calculate the mean value, for each group
    print(df.mean())

    # Show a boxplot
    df.boxplot()
    plt.show()
    
    # Perform a T-test between "lean" and "obese" subjects
    stats.ttest_ind(lean, obese)
    
if __name__ == '__main__':
    params = simple_fit()
    pandas_boxplot()
    
    print('Done')
