'''Solution for Exercise "Normality Check" in Chapter 11 '''

# author: Thomas Haslwanter, date: Sept-2015

from scipy import stats
import matplotlib.pyplot as plt
import statsmodels.formula.api as sm
import seaborn as sns

# We don't need to invent the wheel twice ;)
from S11_correlation import getModelData

if __name__== '__main__':
    
    # get the data
    data = getModelData(show=False)
    
    # Fit the model
    model = sm.ols('AvgTmp ~ year', data)
    results = model.fit()
    
    # Normality check ----------------------------------------------------
    res_data = results.resid    # Get the values for the residuals
    
    # QQ-plot, for a visual check
    stats.probplot(res_data, plot=plt)
    plt.show()
    
    # Normality test, for a quantitative check:
    _, pVal = stats.normaltest(res_data)
    if pVal < 0.05:
        print('WARNING: The data are not normally distributed (p = {0})'.format(pVal))
    else:
        print('Data are normally distributed.')