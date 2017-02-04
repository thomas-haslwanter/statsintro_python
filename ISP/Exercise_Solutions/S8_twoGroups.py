'''Solution for Exercise "Comparing Groups" '''

# author: Thomas Haslwanter, date: May-2016

import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
from scipy import stats
import os

def oneGroup():
    '''Test of mean value of a single set of data'''
    
    print('Single group of data =========================================')
    
    # First get the data
    data = np.array([5260, 5470, 5640, 6180, 6390, 6515, 6805, 7515, 7515, 8230, 8770], dtype=np.float)
    checkValue = 7725   # value to compare the data to
    
    # 4.1.1. Normality test
    # We don't need the first parameter, so we just assign the output to the dummy variable "_"
    (_, p) = stats.normaltest(data)
    if p > 0.05:
        print('Data are distributed normally, p = {0}'.format(p))
        
    # 4.1.2. Do the onesample t-test
    t, prob = stats.ttest_1samp(data, checkValue)
    if prob < 0.05:
        print('With the one-sample t-test, {0:4.2f} is significantly different from the mean (p={1:5.3f}).'.\
        format(checkValue, prob))
    else:
        print('No difference from reference value with onesample t-test.')
    
    # 4.1.3. This implementation of the Wilcoxon test checks for the "difference" of one vector of data from zero
    (_,p) = stats.wilcoxon(data-checkValue)
    if p < 0.05:
        print('With the Wilcoxon test, {0:4.2f} is significantly different from the mean (p={1:5.3f}).'.\
        format(checkValue, p))
    else:
        print('No difference from reference value with Wilcoxon rank sum test.')
    
def twoGroups():
    '''Compare the mean of two groups'''
    
    print('Two groups of data =========================================')

    # Enter the data
    data1 = [76., 101., 66., 72., 88., 82., 79., 73., 76., 85., 75., 64., 76., 81., 86.]
    data2 = [64., 65., 56., 62., 59., 76., 66., 82., 91., 57., 92., 80., 82., 67., 54.]
    
    # Normality test 
    print('\n Normality test --------------------------------------------------')
    
    # To do the test for both data-sets, make a tuple with "(... , ...)", add a counter with
    # "enumerate", and and iterate over the set:
    for ii, data in enumerate((data1, data2)):
        (_, pval) = stats.normaltest(data)
        if pval > 0.05:
            print('Dataset # {0} is normally distributed'.format(ii))
    
    # T-test of independent samples 
    print('\n T-test of independent samples -------------------------------------------')
    
    # Do the t-test for independent samples
    t, pval = stats.ttest_ind(data1, data2)
    if pval < 0.05:
        print('With the T-test, data1 and data2 are significantly different (p = {0:5.3f})'.format(pval))
    else:
        print('No difference between data1 and data2 with T-test.')
    
    # Mann-Whitney test --------------------------------------------------------------
    print('\n Mann-Whitney test --------------------------------------------------------')
    # Watch out: the keyword "alternative" was introduced in scipy 0.17, with default"two-sided";
    if np.int(sp.__version__.split('.')[1]) > 16:
        u, pval = stats.mannwhitneyu(data1, data2, alternative='two-sided')
    else:
        u, pval = stats.mannwhitneyu(data1, data2)
        pval *= 2    # because the default was a one-sided p-value

    if pval < 0.05:
        print('With the Mann-Whitney test, data1 and data2 are significantly different(p = {0:5.3f})'.format(pval))
    else:
        print('No difference between data1 and data2 with Mann-Whitney test.')

if __name__ == '__main__':
    oneGroup()    
    twoGroups()
    
    # And at the end, make sure the results are displayed, even if the program is run from the commandline
    input('\nDone! Thanks for using programs by thomas.\nHit any key to finish.')
