"""Solution to the Examples in Section 6.3.1"""

# author:   Thomas Haslwanter
# date:     Sept-2019

# Import the required packages
import numpy as np
from scipy import stats


def man_183():
    """If cans are assumed to have a standard deviation of 4 g, what does the average
       weight need to be in order to ensure that 99 % of all cans have a weight of at least
       250 g?

       To answer that question, we calculate the probability that the size is
       between 183.0 and 184.0 cm."""
    
    # Define the distribution
    mean = 175
    sd = 6
    nd = stats.norm(mean, sd)
    
    # Calculate and show the probability
    prob_183 = 100*(nd.cdf(184) - nd.cdf(183))
    print(f'The probability that a man is exactly 183 cm tall is {prob_183:4.1f} %')
    
    # Note that here I use "f-strings", which only have become available in Python 3.7.
    # For Python 3.6 or earlier, you have to use:
    # print('The probability that a man is exactly 183 cm tall is {0:4.1f} %'.format(prob_183))
    

def weight_cans():
    """If cans are assumed to have a standard deviation of 4 g, what does the average
    weight need to be in order to ensure that 99 % of all cans have a weight of at least
    250 g? """
    
    # Define the parameters
    sd = 4
    lower_lim = 250
    nd = stats.norm()
    
    # Calculate the average weight, and show the result
    mean = lower_lim + sd * nd.ppf(0.99)
    print(f'If the average can weighs {mean:4.1f} g and the standard ' + 
          f'deviation is {sd} g, then 99% will weigh above {lower_lim} g.')
    
    
def small_men():
    """ If cans are assumed to have a standard deviation of 4 g, what does the average
    weight need to be in order to ensure that 99 % of all cans have a weight of at least
    250 g?
    """
    
    # Define the parameters
    male = {'avg':175, 'sd':6}
    female = {'avg':168, 'sd':3}
    
    # Calculate the distribution for the difference between a randomly selected man, and a randomly selected woman
    diff = {'avg':male['avg'] - female['avg'], 'sd': np.sqrt(male['sd']**2 + female['sd']**2)}
    nd = stats.norm(diff['avg'], diff['sd'])
    p_small_male = nd.cdf(0)
    
    # Show the likelyhood that the man is smaller
    print(f'The probability that a randomly selected man is shorter than a randomly selected woman is {p_small_male*100:4.1f}%.')
    
    
if __name__ == '__main__':
    """Run the individual solutions"""
    man_183()
    weight_cans()
    small_men()
    
