"""Binomial Test
Example of a one-and two-sided binomial test. Taken from Wikipedia
http://en.wikipedia.org/wiki/Binomial_test
"""

# author: Thomas Haslwanter, date: Feb-2021

from scipy import stats


def binomial_test(checkVal: int) -> list:
    """Binomial Test"""
    
    # Set the parameters
    n = 235     # number of dice rolls
    p = 1/6   # probability of rolling a "6"
    
    
    # --- >>> START stats <<< ---
    # Calculate the on-sided test, i.e. the likelihood that you get
    # the same or more times of "6"
    bd = stats.binom(n,p)
    p_oneTail = bd.sf(checkVal-1) # how many values are "higher than" checkVal-1
    
    # Calculate the two-sided test, i.e. how many cases "as extreme or more"
    # than the given case are likely to occur by chance:
    p_twoTail = stats.binom_test(checkVal, n, p)
    # --- >>> STOP stats <<< ---
    
    return (p_oneTail, p_twoTail)


if __name__ == '__main__':

    checkVal = 51
    p1, p2 = binomial_test(checkVal)
    print(f'The chance that you roll {checkVal} or more "6"s is {p1:5.3f}, \n' +
          f'and the chance of an event as extreme as {checkVal} or more ' +
          f'rolls is {p2:5.3f}')
