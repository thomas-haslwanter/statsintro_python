''' Stability of the T-distribution against outliers, compared to the normal distribution. '''

# Copyright(c) 2015, Thomas Haslwanter. All rights reserved, under the CC BY-SA 4.0 International License

# Import standard packages
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats 
import os

# additional packages
# Import formatting commands if directory "Utilities" is available
import os
import sys
sys.path.append(os.path.join('..', 'Code_Quantlets', 'Utilities'))
try:
    from ISP_mystyle import showData 
    
except ImportError:
# Ensure correct performance otherwise
    def showData(*options):
        plt.show()
        return

# Generate the data
np.random.seed(12345)
ndata = 100
data = stats.norm.rvs(size=(ndata,))
data2 = stats.norm.rvs(5, size=(20,))
dataWOutlier = np.hstack((data, data2))

# Calculate the fits
fit_gauss_wo = stats.norm.fit(data)
fit_gauss_w = stats.norm.fit(dataWOutlier)

fit_t_wo = stats.t.fit(data)
fit_t_w = stats.t.fit(dataWOutlier)

# Display the fit-results
print('Gaussian distribution: {0} -> {1}'.format(fit_gauss_wo, fit_gauss_w))
print('T-distribution: {0} -> {1}'.format(fit_t_wo[1:], fit_t_w[1:]))
# Fit of "df" is not shown, as it is pretty unstable for large df

# Plot the fitted curves, to both data sets
fitted_x = np.linspace(-7, 7, 200)       # x-values for fitted curves

# Fitted curves to the original data set
fitted_gauss_wo = stats.norm.pdf(fitted_x, loc=fit_gauss_wo[0], scale=fit_gauss_wo[1])
fitted_t_wo = stats.t.pdf(fitted_x, df=ndata-1, loc=fit_t_wo[1], scale=fit_t_wo[2])

# Fitted curves to the data set with outliers
fitted_gauss_w = stats.norm.pdf(fitted_x, loc=fit_gauss_w[0], scale=fit_gauss_w[1])
fitted_t_w = stats.t.pdf(fitted_x, df=ndata-1, loc=fit_t_w[1], scale=fit_t_w[2])

# Show the data
fig, axs = plt.subplots(2,1, sharex=True)

axs[0].hist(data, normed=True, bins=25, color='#CCCCCC')
axs[0].plot(fitted_x, fitted_gauss_wo, label='normal')
axs[0].plot(fitted_x, fitted_t_wo, ls='--', lw=2, label='t-dist')
axs[0].set_title('Without outliers')
axs[0].legend()

axs[1].hist(dataWOutlier, normed=True, bins=25, color='#CCCCCC')
axs[1].plot(fitted_x, fitted_gauss_w, label='norm')
axs[1].plot(fitted_x, fitted_t_w, ls='--', lw=2, label='t-dist')
axs[1].set_title('With outliers')

outFile = 'CentralLimitTheorem.png'
showData(outFile)

