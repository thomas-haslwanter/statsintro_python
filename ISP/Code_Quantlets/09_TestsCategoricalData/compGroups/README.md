[<img src="../../../../pictures/quantletLogo_FH.png" alt="Intro to Statistics with Python">](https://github.com/thomas-haslwanter/statsintro_python)

## [<img src="../../../../pictures/qloqo.png" alt="Visit QuantNet">](http://quantlet.de/) **ISP_compGroups** [<img src="../../../../pictures/QN2.png" width="60" alt="Visit QuantNet 2.0">](http://quantlet.de/d3/ia)


```yaml
Name of QuantLet: ISP_compGroups

Published in:  An Introduction to Statistics with Python

Description: 'Analysis of categorical data
    - Analysis of one proportion
    - Chi-square test
    - Fisher exact test
    - McNemar''s test
    - Cochran''s Q test'

Keywords: fisher exact test, chi-square test, mcnemar's test, cochran's test

See also: ISP_twoGroups 

Author: Thomas Haslwanter 

Submitted: October 31, 2015 

```

```py
''' Analysis of categorical data
- Analysis of one proportion
- Chi-square test
- Fisher exact test
- McNemar's test
- Cochran's Q test
'''

# Copyright(c) 2015, Thomas Haslwanter. All rights reserved, under the CC BY-SA 4.0 International License

# Import standard packages
import numpy as np
import scipy.stats as stats
import pandas as pd

# additional packages
from statsmodels.sandbox.stats.runs import cochrans_q, mcnemar


def oneProportion():
    '''Calculate the confidence intervals of the population, based on a
    given data sample.
    The data are taken from Altman, chapter 10.2.1.
    Suppose a general practitioner chooses a random sample of 215 women from
    the patient register for her general practice, and finds that 39 of them
    have a history of suffering from asthma. What is the confidence interval
    for the prevalence of asthma?
    '''

    # Get the data
    numTotal = 215
    numPositive = 39

    # --- >>> START stats <<< ---
    # Calculate the confidence intervals
    p = float(numPositive)/numTotal
    se = np.sqrt(p*(1-p)/numTotal)
    td = stats.t(numTotal-1)
    ci = p + np.array([-1,1])*td.isf(0.025)*se
    # --- >>> STOP stats <<< ---

    # Print them
    print('ONE PROPORTION ----------------------------------------')
    print(('The confidence interval for the given sample is {0:5.3f} to {1:5.3f}'.format(
        ci[0], ci[1])))
    
    return ci

def chiSquare():
    ''' Application of a chi square test to a 2x2 table.
    The calculations are done with and without Yate's continuity
    correction.
    Data are taken from Altman, Table 10.10:
    Comparison of number of hours' swimming by swimmers with or without erosion of dental enamel.
    >= 6h: 32 yes, 118 no
    <  6h: 17 yes, 127 no
    '''

    # Enter the data
    obs = np.array([[32, 118], [17, 127]])

    # --- >>> START stats <<< ---
    # Calculate the chi-square test
    chi2_corrected = stats.chi2_contingency(obs, correction=True)
    chi2_uncorrected = stats.chi2_contingency(obs, correction=False)
    # --- >>> STOP stats <<< ---

    # Print the result
    print('\nCHI SQUARE --------------------------------------------------')
    print(('The corrected chi2 value is {0:5.3f}, with p={1:5.3f}'.format(
        chi2_corrected[0], chi2_corrected[1])))
    print(('The uncorrected chi2 value is {0:5.3f}, with p={1:5.3f}'.format(
        chi2_uncorrected[0], chi2_uncorrected[1])))
    
    return chi2_corrected

def fisherExact():
    '''Fisher's Exact Test:
    Data are taken from Altman, Table 10.14
    Spectacle wearing among juvenile delinquensts and non-delinquents who failed a vision test
    Spectecle wearers: 1 delinquent, 5 non-delinquents
    non-spectacle wearers: 8 delinquents, 2 non-delinquents
    '''

    # Enter the data
    obs = np.array([[1,5], [8,2]])

    # --- >>> START stats <<< ---
    # Calculate the Fisher Exact Test
    # Note that by default, the option "alternative='two-sided'" is set;
    # other options are 'less' or 'greater'.
    fisher_result = stats.fisher_exact(obs)
    # --- >>> STOP stats <<< ---

    # Print the result
    print('\nFISHER --------------------------------------------------------')
    print(('The probability of obtaining a distribution at least as extreme '
    + 'as the one that was actually observed, assuming that the null ' +
    'hypothesis is true, is: {0:5.3f}.'.format(fisher_result[1])))
    
    return fisher_result

def cochranQ():
    '''Cochran's Q test: 12 subjects are asked to perform 3 tasks. The outcome of each task is "success" or 
    "failure". The results are coded 0 for failure and 1 for success. In the example, subject 1 was successful
    in task 2, but failed tasks 1 and 3.
    Is there a difference between the performance on the three tasks?
    '''
    
    tasks = np.array([[0,1,1,0,1,0,0,1,0,0,0,0],
                      [1,1,1,0,0,1,0,1,1,1,1,1],
                      [0,0,1,0,0,1,0,0,0,0,0,0]])
    
    # I prefer a DataFrame here, as it indicates directly what the values mean
    df = pd.DataFrame(tasks.T, columns = ['Task1', 'Task2', 'Task3'])
    
    # --- >>> START stats <<< ---
    (Q, pVal) = cochrans_q(df)
    # --- >>> STOP stats <<< ---
    print('\nCOCHRAN\'S Q -----------------------------------------------------')
    print('Q = {0:5.3f}, p = {1:5.3f}'.format(Q, pVal))
    if pVal < 0.05:
        print("There is a significant difference between the three tasks.")
    
def tryMcnemar():
    '''McNemars Test should be run in the "exact" version, even though approximate formulas are
    typically given in the lecture scripts. Just ignore the statistic that is returned, because
    it is different for the two options.
    
    In the following example, a researcher attempts to determine if a drug has an effect on a
    particular disease. Counts of individuals are given in the table, with the diagnosis
    (disease: present or absent) before treatment given in the rows, and the diagnosis
    after treatment in the columns. The test requires the same subjects to be included in
    the before-and-after measurements (matched pairs).
    '''
    
    
    f_obs = np.array([[101, 121],[59, 33]])
    (statistic, pVal) = mcnemar(f_obs)
    print('\nMCNEMAR\'S TEST -----------------------------------------------------')
    print('p = {0:5.3f}'.format(pVal))
    if pVal < 0.05:
        print("There was a significant change in the disease by the treatment.")    
    
if __name__ == '__main__':
    oneProportion()
    chiSquare()
    fisherExact()
    tryMcnemar()
    cochranQ()

```
