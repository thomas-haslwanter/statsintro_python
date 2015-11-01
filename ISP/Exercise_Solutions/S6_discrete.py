'''Solution for Exercise "Continuous Distribution Functions" '''

# author: Thomas Haslwanter, date: Sept-2015

from scipy import stats

# Binomial distribution --------------------------------------------------
# Generate the distribution
p = 0.37
n = 15
bd = stats.binom(n, p)

# Select the interesting numbers, and calculate the "Probability Mass Function" (PMF)
x = [3,6,10]
y = bd.pmf(x)

# To print the result, we use the "zip" function to generate pairs of numbers
for num, solution in zip(x,y):
    print('The chance of finding {0} students with blue eyes is {1:4.1f}%.'.format(num, solution*100))

# Poisson distribution --------------------------------------------------
# Generate the distribution.
# Watch out NOT to divide integers, as "3/4" gives "0" in Python 2.x!
prob = 62./(365./7)
pd = stats.poisson(prob)

# Select the interesting numbers, calculate the PMF, and print the results
x = [0,2,5]
y = pd.pmf(x)*100
for num, solution in zip(x,y):
    print('The chance of haveing {0} fatal accidents in one week is {1:4.1f}%.'.format(num,solution))

# The last line just makes sure that the program does not close, when it is run from the commandline.
input('Done! Thanks for using programs by thomas.')

