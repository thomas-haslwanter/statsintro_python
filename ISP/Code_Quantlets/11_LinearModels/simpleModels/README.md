
![quantletLogo_FH](../../../../pictures/quantletLogo_FH.png)

## ![qlogo](http://quantnet.wiwi.hu-berlin.de/graphics/quantlogo.png) **ISP_simpleModels**


```yaml
Name of QuantLet: ISP_simpleModels

Published in:  An Introduction to Statistics with Python

Description: 'Simple linear models.
    - <model_formulas> is based on examples in Kaplan''s book <Statistical Modeling>.
    - <polynomial_regression> shows how to work with simple design matrices,
      like MATLAB''s <regress> command.'

Keywords: linear regression model

See also: 'ISP_anscombe, ISP_bivariate, ISP_bootstrapDemo, ISP_fitLine,
        ISP_modelImplementations'

Author: Thomas Haslwanter 

Submitted: October 31, 2015 

Datafile: swim100m.csv 
```

```py
'''Simple linear models.
- "model_formulas" is based on examples in Kaplan's book "Statistical Modeling".
- "polynomial_regression" shows how to work with simple design matrices, like MATLAB's "regress" command.
'''

# Copyright(c) 2015, Thomas Haslwanter. All rights reserved, under the CC BY-SA 4.0 International License

# Import standard packages
import numpy as np
import pandas as pd

# additional packages
from statsmodels.formula.api import ols
import statsmodels.regression.linear_model as sm
from statsmodels.stats.anova import anova_lm

def model_formulas():
    ''' Define models through formulas '''
    
    # Get the data:
    # Development of world record times for the 100m Freestyle, for men and women.
    data = pd.read_csv('swim100m.csv')
    
    # Different models
    model1 = ols("time ~ sex", data).fit()  # one factor
    model2 = ols("time ~ sex + year", data).fit()   # two factors
    model3 = ols("time ~ sex * year", data).fit()   # two factors with interaction
    
    # Model information
    print((model1.summary()))
    print((model2.summary()))
    print((model3.summary()))
    
    # ANOVAs
    print('----------------- Results ANOVAs: Model 1 -----------------------')
    print((anova_lm(model1)))
    
    print('--------------------- Model 2 -----------------------------------')
    print((anova_lm(model2)))
    
    print('--------------------- Model 3 -----------------------------------')
    model3Results = anova_lm(model3)
    print(model3Results)
    
    # Just to check the correct run
    return model3Results['F'][0] # should be 156.1407931415788
    
def polynomial_regression():
    ''' Define the model directly through the design matrix.
        Similar to MATLAB's "regress" command.
        '''

    # Generate the data: a noisy second order polynomial
    
    # To get reproducable values, I provide a seed value
    np.random.seed(987654321)       
    
    t = np.arange(0,10,0.1)
    y = 4 + 3*t + 2*t**2 + 5*np.random.randn(len(t))
    
    # --- >>> START stats <<< ---
    # Make the fit. Note that this is another "OLS" than the one in "model_formulas",
    # as it works directly with the design matrix!
    M = np.column_stack((np.ones(len(t)), t, t**2))
    res = sm.OLS(y, M).fit()
    # --- >>> STOP stats <<< ---
        
    # Display the results
    print('Summary:')
    print((res.summary()))
    print(('The fit parameters are: {0}'.format(str(res.params))))
    print('The confidence intervals are:')
    print((res.conf_int()))
    
    return res.params # should be [ 4.74244177,  2.60675788,  2.03793634]

if __name__ == '__main__':
    model_formulas()
    polynomial_regression()
```
