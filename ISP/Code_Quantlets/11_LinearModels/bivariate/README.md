
![quantletLogo_FH](../../../../pictures/quantletLogo_FH.png)

## ![qlogo](http://quantnet.wiwi.hu-berlin.de/graphics/quantlogo.png) **ISP_bivariate**


```yaml
Name of QuantLet: ISP_bivariate

Published in:  An Introduction to Statistics with Python

Description: 'Analysis of multivariate data
    - Regression line
    - Correlation (Pearson-rho, Spearman-rho, and Kendall-tau)'

Keywords: correlation, pearson rho, spearman rho, kendall tau

See also: 'ISP_anscombe, ISP_bootstrapDemo, ISP_fitLine,
        ISP_modelImplementations, ISP_simpleModels'

Author: Thomas Haslwanter 

Submitted: October 31, 2015 

Datafile:  altman_11_1.txt, altman_11_6.txt

```

```py
''' Analysis of multivariate data
- Regression line
- Correlation (Pearson-rho, Spearman-rho, and Kendall-tau)
'''

# Copyright(c) 2015, Thomas Haslwanter. All rights reserved, under the CC BY-SA 4.0 International License

# Import standard packages
import numpy as np
from scipy import stats
import pandas as pd

def regression_line():
    '''Fit a line, using the powerful "ordinary least square" method of pandas.
    
    Data from 24 type 1 diabetic patients, relating fasting blood glucose (mmol/l)
    to mean circumferential shortening velocity (%/sec), derived form echocardiography.
    '''
    
    # Get the data
    inFile = 'altman_11_6.txt'
    data = np.genfromtxt(inFile, delimiter=',')
    
    # Convert them into a pandas DataFrame
    df = pd.DataFrame(data, columns=['glucose', 'Vcf'])

    # --- >>> START stats <<< ---
    # Fit a regression line to the data, and display the model results
    model = pd.ols(y=df['Vcf'], x=df['glucose'])
    print((model.summary))
    # --- >>> STOP stats <<< ---
    
    return model.f_stat['f-stat'] # should be 4.4140184331462571
    
def correlation():
    '''Pearson correlation, and two types of rank correlation (Spearman, Kendall)
    comparing age and %fat (measured by dual-photon absorptiometry) for 18 normal adults.
    '''
    
    # Get the data
    inFile = 'altman_11_1.txt'
    data = np.genfromtxt(inFile, delimiter=',')
    x = data[:,0]
    y = data[:,1]
    
    # --- >>> START stats <<< ---
    # Calculate correlations
    # Resulting correlation values are stored in a dictionary, so that it is
    # obvious which value belongs to which correlation coefficient.
    corr = {}
    corr['pearson'], _ = stats.pearsonr(x,y)
    corr['spearman'], _ = stats.spearmanr(x,y)
    corr['kendall'], _ = stats.kendalltau(x,y)
    # --- >>> STOP stats <<< ---
    
    print(corr)    
    
    # Assert that Spearman's rho is just the correlation of the ranksorted data
    np.testing.assert_almost_equal(corr['spearman'], stats.pearsonr(stats.rankdata(x), stats.rankdata(y))[0])
    
    return corr['pearson']  # should be 0.79208623217849117
    
if __name__ == '__main__':
    regression_line()    
    correlation()
```
