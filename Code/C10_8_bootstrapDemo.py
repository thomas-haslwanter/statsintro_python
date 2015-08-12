''' Example of bootstrapping the confidence interval for the mean of a sample distribution
This function requires "bootstrap.py", which is available from
https://github.com/cgevans/scikits-bootstrap
   
'''

# author: Thomas Haslwanter, date: Feb-2015

# Import standard packages
import matplotlib.pyplot as plt
import scipy as sp
from scipy import stats

# additional packages
import scikits.bootstrap as bootstrap

def generate_data():
    # To get reproducable values, I provide a seed value
    sp.random.seed(987654321)   
    
    # Generate a non-normally distributed datasample
    data = stats.poisson.rvs(2, size=1000)
    
    # Show the data
    plt.plot(data, '.')
    plt.title('Non-normally distributed dataset: Press any key to continue')
    #plt.show()
    plt.waitforbuttonpress()
    plt.close()    
    
    return(data)
    
def calc_bootstrap(data):
    # --- >>> START stats <<< ---
    # Calculate the bootstrap
    CIs = bootstrap.ci(data=data, statfunction=sp.mean)
    # --- >>> STOP stats <<< ---
    
    # Print the data: the "*" turns the array CIs into a list
    print(('The conficence intervals for the mean are: {0} - {1}'.format(*CIs)))
    
    return CIs

if __name__ == '__main__':
    data = generate_data()
    calc_bootstrap(data)
    input('Done')
