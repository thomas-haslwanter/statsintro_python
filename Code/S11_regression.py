'''Solution for Exercise "Regression" '''

# author: Thomas Haslwanter, date: Sept-2015

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import seaborn as sns
import statsmodels.formula.api as sm

# We don't need to invent the wheel twice ;)
from S11_correlation import getModelData

if __name__== '__main__':
    
    # get the data
    data = getModelData(show=False)
    
    # Regression --------------------------------------------------------
    # For "ordinary least square" models, you can do the model directly with pandas
    #model = pd.ols(x=data['year'], y=data['AvgTmp'])
    
    # or you can use the formula-approach from statsmodels:
    # offsets are automatically included in the model
    model = sm.ols('AvgTmp ~ year', data)
    results = model.fit()
    print(results.summary())
    
    # Visually, the confidence intervals can be shown using seaborn
    sns.lmplot('year', 'AvgTmp', data)
    plt.show()
    
    # Is the inclination significant?
    ci = results.conf_int()
    
    # This line is a bit tricky: if both are above or both below zero, the product is positive:
    # we look at the coefficient that describes the correlation with "year"
    if np.prod(ci.loc['year'])>0:
        print('The slope is significant')