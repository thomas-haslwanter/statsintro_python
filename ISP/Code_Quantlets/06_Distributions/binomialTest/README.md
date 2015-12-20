[<img src="../../../../pictures/quantletLogo_FH.png" alt="Intro to Statistics with Python">](https://github.com/thomas-haslwanter/statsintro_python)

## [<img src="../../../../pictures/qloqo.png" alt="Visit QuantNet">](http://quantlet.de/) **ISP_binomialTest** [<img src="../../../../pictures/QN2.png" width="60" alt="Visit QuantNet 2.0">](http://quantlet.de/d3/ia)

```yaml
Name of QuantLet: ISP_binomialTest

Published in:  An Introduction to Statistics with Python

Description: Example of a one-and two-sided binomial test.

Keywords: test, binomial, simulation

See also: ISP_centralLimitTheorem, ISP_distContinuous, ISP_distDiscrete, ISP_distNormal

Author: Thomas Haslwanter 

Submitted: October 31, 2015 

Output: 'return (p_oneTail, p_twoTail)'

```

```py
'''Binomial Test
Example of a one-and two-sided binomial test. Taken from Wikipedia
http://en.wikipedia.org/wiki/Binomial_test
'''

# Copyright(c) 2015, Thomas Haslwanter. All rights reserved, under the CC BY-SA 4.0 International License

from scipy import stats

def binomial_test(checkVal):
    '''Binomial Test'''
    
    # Set the parameters
    n = 235     # number of dice rolls
    p = 1.0/6   # probability of rolling a "6"; the "1.0" is required for Python 2.x
    
    
    # --- >>> START stats <<< ---
    # Calculate the on-sided test, i.e. the likelihood that you get the same or more times of "6"
    bd = stats.binom(n,p)
    p_oneTail = bd.sf(checkVal-1)   # how many values are "higher than" checkVal-1
    
    # Calculate the two-sided test, i.e. how many cases "as extreme or more" than the given case are likely to occur by chance:
    p_twoTail = stats.binom_test(checkVal, n, p)
    # --- >>> STOP stats <<< ---
    
    return (p_oneTail, p_twoTail)

#----------------------------------------------------------------------
if __name__ == '__main__':

    checkVal = 51
    p1, p2 = binomial_test(checkVal)
    print(('The chance that you roll {0} or more "6" is {1:5.3f}, and the chance of an event as extreme as {0} or more rolls is {2:5.3f}'.format(checkVal, p1, p2)))

```
