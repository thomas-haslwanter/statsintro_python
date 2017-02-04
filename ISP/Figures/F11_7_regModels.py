# -*- coding: utf-8 -*-
'''
Explanation of the output of statsmodels OLS-command.
Strongly based on a blog by Connor Johnson.
http://connor-johnson.com/2014/02/18/linear-regression-with-python/
'''

# Copyright(c) 2015, Thomas Haslwanter. All rights reserved, under the CC BY-SA 4.0 International License

# Import standard packages
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import pandas as pd
import os

# additional packages
# Import formatting commands if directory "Utilities" is available
import os
import sys
sys.path.append(os.path.join('..', 'Code_Quantlets', 'Utilities'))
try:
    from ISP_mystyle import setFonts, showData 
    
except ImportError:
# Ensure correct performance otherwise
    def setFonts(*options):
        return
    def showData(*options):
        plt.show()
        return
    
import matplotlib as mpl
import statsmodels.formula.api as sm
from sklearn.linear_model import LinearRegression

data_str = '''Region Alcohol Tobacco
North 6.47 4.03
Yorkshire 6.13 3.76
Northeast 6.19 3.77
East_Midlands 4.89 3.34
West_Midlands 5.63 3.47
East_Anglia 4.52 2.92
Southeast 5.89 3.20
Southwest 4.79 2.71
Wales 5.27 3.53
Scotland 6.08 4.51
Northern_Ireland 4.02 4.56'''

# Python 2/3 use different packages for "StringIO"
if sys.version_info[0] == 3:
    from io import StringIO
else:
    from StringIO import StringIO
    
df = pd.read_csv(StringIO(data_str), sep=r'\s+')

# Plot the data
setFonts(18)
plt.plot(df.Tobacco, df.Alcohol, 'o', ms=10)
plt.xlabel('Tobacco')
plt.ylabel('Alcohol')
plt.title('Sales in Several UK Regions')
plt.ylim([3.8, 6.7])

outFile = 'Alc_vs_Tobacco.png'
showData(outFile)

result = sm.ols('Alcohol ~ Tobacco', df[:-1]).fit()
print(result.summary())

N = result.nobs
k = result.df_model+1
dfm, dfe = k-1, N - k
F = result.mse_model / result.mse_resid
p = 1.0 - stats.f.cdf(F,dfm,dfe)
print('F-statistic: {:.3f},  p-value: {:.5f}'.format( F, p ))

N = result.nobs
SSR = result.ssr
s2 = SSR / N
L = ( 1.0/np.sqrt(2*np.pi*s2) ) ** N * np.exp( -SSR/(s2*2.0) )
print('ln(L) =', np.log( L ))

print(result.params)

# Standard Errors ---------------
df['Eins'] = np.ones(( len(df), ))
Y = df.Alcohol[:-1]
X = df[['Tobacco','Eins']][:-1]

# ------------
X = df.Tobacco[:-1]

# add a column of ones for the constant intercept term
X = np.vstack(( np.ones(X.size), X ))

# convert the NumPy arrray to matrix
X = np.matrix( X )

# perform the matrix multiplication,
# and then take the inverse
C = np.linalg.inv( X * X.T )

# multiply by the MSE of the residual
C *= result.mse_resid

# take the square root
SE = np.sqrt(C)

print(SE)
# ------------------------

i = 1
beta = result.params[i]
se = SE[i,i]
t = beta / se
print('t =', t)

N = result.nobs
k = result.df_model + 1
dof = N - k
p_onesided = 1.0 - stats.t( dof ).cdf( t )
p = p_onesided * 2.0
print('p = {0:.3f}'.format(p))

# CI -----------------
i = 0

# the estimated coefficient, and its variance
beta, c = result.params[i], SE[i,i]

# critical value of the t-statistic
N = result.nobs
P = result.df_model
dof = N - P - 1
z = stats.t( dof ).ppf(0.975)

# the confidence interval
print(beta - z * c, beta + z * c)

# Omnibus test ------------------------
d = Y - result.fittedvalues
S = np.mean( d**3.0 ) / np.mean( d**2.0 )**(3.0/2.0)
K = np.mean( d**4.0 ) / np.mean( d**2.0 )**(4.0/2.0)
print('Skewness: {:.3f},  Kurtosis: {:.3f}'.format( S, K ))

def Z1( s, n ):
    Y = s * np.sqrt( ( ( n + 1 )*( n + 3 ) ) / ( 6.0 * ( n - 2.0 ) ) )
    b = 3.0 * ( n**2.0 + 27.0*n - 70 )*( n + 1.0 )*( n + 3.0 )
    b /= ( n - 2.0 )*( n + 5.0 )*( n + 7.0 )*( n + 9.0 )
    W2 = - 1.0 + np.sqrt( 2.0 * ( b - 1.0 ) )
    alpha = np.sqrt( 2.0 / ( W2 - 1.0 ) )
    z = 1.0 / np.sqrt( np.log( np.sqrt( W2 ) ) )
    z *= np.log( Y / alpha + np.sqrt( ( Y / alpha )**2.0 + 1.0 ) )
    return z

def Z2( k, n ):
    E = 3.0 * ( n - 1.0 ) / ( n + 1.0 )
    v = 24.0 * n * ( n - 2.0 )*( n - 3.0 )
    v /= ( n + 1.0 )**2.0*( n + 3.0 )*( n + 5.0 )
    X = ( k - E ) / np.sqrt( v )
    b = ( 6.0 * ( n**2.0 - 5.0*n + 2.0 ) ) / ( ( n + 7.0 )*( n + 9.0 ) )
    b *= np.sqrt( ( 6.0 * ( n + 3.0 )*( n + 5.0 ) ) / ( n * ( n - 2.0 )*( n - 3.0 ) ) )
    A = 6.0 + ( 8.0 / b )*( 2.0 / b + np.sqrt( 1.0 + 4.0 / b**2.0 ) )
    z = ( 1.0 - 2.0 / A ) / ( 1.0 + X * np.sqrt( 2.0 / ( A - 4.0 ) ) )
    z = ( 1.0 - 2.0 / ( 9.0 * A ) ) - z**(1.0/3.0)
    z /= np.sqrt( 2.0 / ( 9.0 * A ) )
    return z

K2 = Z1( S, N )**2.0 + Z2( K, N )**2.0
print('Omnibus: {}'.format( K2))

p = 1.0 - stats.chi2(2).cdf( K2 )
print('Pr( Omnibus ) = {}'.format( p ))

(K2, p) = stats.normaltest(result.resid)
print('Omnibus: {0}, p = {1}'.format(K2, p))

# ---------------------

JB = (N/6.0) * ( S**2.0 + (1.0/4.0)*( K - 3.0 )**2.0 )
p = 1.0 - stats.chi2(2).cdf(JB)
print('JB-statistic: {:.5f},  p-value: {:.5f}'.format( JB, p ))

# ---------------------

X = np.matrix( X )
EV = np.linalg.eig( X * X.T )
print(EV)
CN = np.sqrt( EV[0].max() / EV[0].min() )
print('Condition No.: {:.5f}'.format( CN ))

# sklearn ----------------
data = np.matrix( df )
cln = LinearRegression()
org = LinearRegression()

X, Y = data[:,2], data[:,1]
cln.fit( X[:-1], Y[:-1] )
org.fit( X, Y )

clean_score = '{0:.3f}'.format( cln.score( X[:-1], Y[:-1] ) )
original_score = '{0:.3f}'.format( org.score( X, Y ) )

mpl.rcParams['font.size']=14

if sys.version_info[0] == 3:
    labelStart = 'All other regions, $Rˆ2$ = '
else:
    labelStart = 'All other regions, R2 = '

plt.plot( df.Tobacco[:-1], df.Alcohol[:-1], 'bo', markersize=10,
    label=labelStart + clean_score )

plt.hold(True)
if sys.version_info[0] == 3:
    labelStart = 'N. Ireland, outlier, $Rˆ2$ = ' 
else:
    labelStart = 'N. Ireland, outlier, R2 = '
    
plt.plot( df.Tobacco[-1:], df.Alcohol[-1:], 'r*', ms=20, lw=10,
    label=labelStart+original_score)    

test = np.arange( 2.5, 4.85, 0.1 )
test = np.array( np.matrix( test ).T )
plt.plot( test, cln.predict( test ), 'k' )
plt.plot( test, org.predict( test ), 'k--' )

plt.xlabel('Tobacco')
plt.xlim(2.5,4.75)
plt.ylabel('Alcohol')
plt.ylim(2.75,7.0)
plt.title('Regression of Alcohol from Tobacco') ;
plt.grid() ;
plt.legend(loc='lower center')

outFile = 'alcohol_regressed_over_tobacco.png'
showData(outFile)
