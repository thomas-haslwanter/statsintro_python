"""Short demonstration of Python for scientific data analysis

This script covers the following points:
* Plotting a sine wave
* Generating a column matrix of data
* Writing data to a text-file, and reading data from a text-file
* Waiting for a button-press to continue the program exectution
    (Note: this does NOT work in ipython, if you run it with inline figures!)
* Using a dictionary, which is similar to MATLAB structures
* Extracting data which fulfill a certain condition
* Calculating the best-fit-line to noisy data
* Formatting text-output
* Waiting for a keyboard-press
* Calculating confidence intervals for line-fits
* Saving figures

For such a short program, the definition of a "main" function, and calling
it by default when the module is imported by the main program, is a bit
superfluous. But it shows good Python coding style.
"""

# author: Thomas Haslwanter, date: Jan-2021

# In Python you explicitly have to load the modules that you need
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

def main():
    """Define the main function. """
    
    # Create a sine-wave
    x = np.arange(0,10,0.1)
    y = np.sin(x)

    # Save the data in a text-file, in column form
    # The formatting is a bit clumsy: data are by default row variables; so to
    # get a matrix, you stack the two rows above each other, and then transpose
    # the matrix
    outFile = 'test.txt'
    np.savetxt(outFile, np.column_stack((x,y)) )

    # Read the data into a different variable
    inData = np.loadtxt(outFile)
    x_2 = inData[:,0] # Note that Python starts at "0"!
    y_2 = inData[:,1]

    # Plot the data, and wait for the user to click
    plt.plot(x_2, y_2)
    plt.title('Hit any key to continue')
    plt.waitforbuttonpress()

    # Generate a noisy line
    x = np.arange(-100,100)
    # use a Python "dictionary" to group the parameters
    par = {'offset':100, 'slope':0.5, 'noiseAmp':4}
    y = par['offset'] + par['slope']*x + par['noiseAmp']*np.random.randn(len(x))

    # Select "late" values, i.e. with x>10
    late = x > 10
    x_high = x[late]
    y_high = y[late]
    
    # Determine the best-fit line
    res = stats.linregress(x_high, y_high)

    # Plot the "late" data, and the best-fit line
    plt.close()
    plt.plot(x_high, y_high, label = 'raw data')
    plt.plot(x_high, res.intercept + res.slope*x_high, 'r', label='fit')
    
    out_file = 'line_fit.png'
    plt.savefig(out_file, dpi=200)
    plt.show()
    
    print(f'Results saved to {out_file}')
    
    # For the confidence interval of the slope we need the
    # two-sided inverse Students t-distribution
    p = 0.05        # probability
    df = len(x)-2   # degrees of freedom
    
    ts = np.abs(stats.t.ppf(p/2, df))
    print(f"slope (95%): {res.slope:.3f} +/- {ts*res.stderr:.3f}")
    # >> slope (95%): 0.517 +/- 0.033 

if __name__=='__main__':
    main()    # Execute the main function
