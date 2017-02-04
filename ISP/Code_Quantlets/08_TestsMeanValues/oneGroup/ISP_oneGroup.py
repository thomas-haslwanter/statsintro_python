'''Analysis of one group of data

This script shows how to
- Use a t-test for a single mean
- Use a non-parametric test (Wilcoxon signed rank sum) to check a single mean 
- Compare the values from the t-distribution with those of a normal distribution
'''

# Copyright(c) 2015, Thomas Haslwanter. All rights reserved, under the CC BY-SA 4.0 International License

# Import standard packages
import numpy as np
import scipy.stats as stats

def check_mean():        
    '''Data from Altman, check for significance of mean value.
    Compare average daily energy intake (kJ) over 10 days of 11 healthy women, and compare it to the recommended level of 7725 kJ.
    '''
    
    # Get data from Altman
    inFile = 'altman_91.txt'
    data = np.genfromtxt(inFile, delimiter=',')

    # Watch out: by default the standard deviation in numpy is calculated with ddof=0, corresponding to 1/N!
    myMean = np.mean(data)
    mySD = np.std(data, ddof=1)     # sample standard deviation
    print(('Mean and SD: {0:4.2f} and {1:4.2f}'.format(myMean, mySD)))

    # Confidence intervals
    tf = stats.t(len(data)-1)
    # multiplication with np.array[-1,1] is a neat trick to implement "+/-"
    ci = np.mean(data) + stats.sem(data)*np.array([-1,1])*tf.ppf(0.975)
    print(('The confidence intervals are {0:4.2f} to {1:4.2f}.'.format(ci[0], ci[1])))

    # Check if there is a significant difference relative to "checkValue"
    checkValue = 7725
    # --- >>> START stats <<< ---
    t, prob = stats.ttest_1samp(data, checkValue)
    if prob < 0.05:
        print(('{0:4.2f} is significantly different from the mean (p={1:5.3f}).'.format(checkValue, prob)))

    # For not normally distributed data, use the Wilcoxon signed rank sum test
    (rank, pVal) = stats.wilcoxon(data-checkValue)
    if pVal < 0.05:
      issignificant = 'unlikely'
    else:
      issignificant = 'likely'
    # --- >>> STOP stats <<< ---
      
    print(('It is ' + issignificant + ' that the value is {0:d}'.format(checkValue)))
    
    return prob # should be 0.018137235176105802
 
def compareWithNormal():
    '''This function is supposed to give you an idea how big/small the difference between t- and normal
    distribution are for realistic calculations.
    '''

    # generate the data
    np.random.seed(12345)
    normDist = stats.norm(loc=7, scale=3)
    data = normDist.rvs(100)
    checkVal = 6.5

    # T-test
    # --- >>> START stats <<< ---
    t, tProb = stats.ttest_1samp(data, checkVal)
    # --- >>> STOP stats <<< ---

    # Comparison with corresponding normal distribution
    mmean = np.mean(data)
    mstd = np.std(data, ddof=1)
    normProb = stats.norm.cdf(checkVal, loc=mmean,
            scale=mstd/np.sqrt(len(data)))*2

    # compare
    print(('The probability from the t-test is ' + '{0:5.4f}, and from the normal distribution {1:5.4f}'.format(tProb, normProb)))
    
    return normProb # should be 0.054201154690070759
           
if __name__ == '__main__':
    check_mean()
    compareWithNormal()
