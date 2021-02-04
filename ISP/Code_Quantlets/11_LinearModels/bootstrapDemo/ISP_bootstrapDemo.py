""" Example of bootstrapping the confidence interval for the mean
This function requires "bootstrap.py", which is available from
https://github.com/cgevans/scikits-bootstrap
"""

# author: Thomas Haslwanter, date: Feb-2021

# Import standard packages
import matplotlib.pyplot as plt
import scipy as sp
from scipy import stats

# additional packages
import scikits.bootstrap as bootstrap


def generate_data():
    """ Generate the data for the bootstrap simulation """
    
    # To get reproducable values, I provide a seed value
    sp.random.seed(987654321)   
    
    # Generate a non-normally distributed datasample
    data = stats.poisson.rvs(2, size=1000)
    
    # Show the data
    plt.plot(data, '.')
    plt.title('Non-normally distributed dataset: Press any key to continue')
    plt.waitforbuttonpress()
    plt.close()    
    
    return(data)
    

def calc_bootstrap(data):
    """ Find the confidence interval for the mean of the given data set with bootstrapping. """
    
    # --- >>> START stats <<< ---
    # Calculate the bootstrap
    CIs = bootstrap.ci(data=data, statfunction=sp.mean)
    # --- >>> STOP stats <<< ---
    
    # Print the data: the "*" turns the array "CIs" into a list
    print(f'The conficence intervals for the mean are: {CIs[0]} - {CIs[1]}')
    
    return CIs


if __name__ == '__main__':
    data = generate_data()
    calc_bootstrap(data)
    input('Done')
