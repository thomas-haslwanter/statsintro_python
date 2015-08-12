'''Linear Regression
Estimation of a linear regression model using the Spector and Mazzeo (1980) data set.

Documentation:
    data on 32 students TUCE scores
    5 columns with rows = students

    1) Grade ..... post grade
    2) constant .. term
    3) psi
    4) tuce ...... tuce (test of understanding of college economics) score
    5) gpa ....... grade point average

'''

'''
Author: Bruno Rodrigues
Date:   March-2013
Ver:    1.3 (Thomas Haslwanter)
'''

# For this we only need to import statsmodels
import statsmodels.api as sm

def main():
    # We load the spector dataset as a pandas dataframe
    # Of course, you can load your own datasets 
    data = sm.datasets.spector.load_pandas()
    
    # We define y as the endogenous variable, and x as the 
    # exogenous variable.
    # Note that if you load your own data, the methods endog 
    # and exog will not be available and you will have to 
    # explicitly define the endogenous and exogenous variables
    y, x = data.endog, data.exog
    
    # We do the regression
    reg = sm.OLS(y, x).fit()
    
    # And here we can see the results in a very nice looking table
    print('SUMMARY -------------------------------------------')
    print((reg.summary()))
    
    # We can only take a look at the parameter values though
    print('PARAMETERS ----------------------------------------')
    print((reg.params))
    
    # We can also extract the residuals
    print('RESIDUALS -----------------------------------------')
    print((reg.resid))
    
    # This line is just to prevent the output from vanishing when you
    # run the program by double-clicking
    input('Done - Hit any key to finish.')

if __name__ == '__main__':
    main()
