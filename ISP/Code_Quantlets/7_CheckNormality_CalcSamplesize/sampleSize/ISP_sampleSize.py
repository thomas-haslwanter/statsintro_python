"""Calculate the sample size for experiments, for normally distributed groups,
    for:
- Experiments with one single group
- Comparing two groups
"""

# author: Thomas Haslwanter, Feb-2021

# Import standard packages
import numpy as np

# additional packages
from scipy.stats import norm


def sampleSize_oneGroup(d:float, alpha:float=0.05, beta:float=0.2,
                        sigma:float=1) -> int:
    """Sample size for a single group.
    The formula corresponds to Eq 6.2 in the book.

    Parameters
    ----------
    d : Effect size
    alpha : Probability of Type I error (significance)
    beta : Probability of Type II error
    sigma : Standard deviation of data

    Returns
    -------
    n : Number of subjects required for a significant test
    """
    
    n = np.round((norm.ppf(1-alpha/2.) + norm.ppf(1-beta))**2 * sigma**2 / d**2)
    
    print(f'In order to detect a change of {d}' +
        f'in a group with an SD of {sigma},\n' +
        f'with significance {alpha} and test-power {100*(1-beta)},' +
        f'you need at least {int(n):d} subjects.\n')
    
    return n


def sampleSize_twoGroups(D:float, alpha:float=0.05, beta:float=0.2,
        sigma1:float=1, sigma2:float=1) -> int:
    """Sample size for two groups.
    The formula corresponds to Eq 6.4 in the book.

    Parameters
    ----------
    D : Effect size
    alpha : Probability of Type I error (significance)
    beta : Probability of Type II error
    sigma : Standard deviation of data

    Returns
    -------
    n : Number of subjects (in each group) required for a significant test
    """
    
    n = np.round((norm.ppf(1-alpha/2.) + \
            norm.ppf(1-beta))**2 * (sigma1**2 + sigma2**2) / D**2)
    
    print(f'In order to detect a change of {D} between groups' +
        f'with an SD of {sigma1} and {sigma2},\n' +
        f'with significance {alpha} and test-power {100*(1-beta)}, ' +
        f'you need in each group at least {int(n):d} subjects.')
    
    return n


if __name__ == '__main__':
    sampleSize_oneGroup(0.5)
    sampleSize_twoGroups(0.4, sigma1=0.6, sigma2=0.6)
    
