'''
Short demonstration of a Python script.

author: Thomas Haslwanter
date:   May-2015
ver:    1.0
'''

# Import standard packages
import numpy as np
import matplotlib.pyplot as plt

# Generate the time-values
t = np.r_[0:10:0.1]

# Set the frequency, and calculate the sine-value
freq = 0.5
x = np.sin(2*np.pi*freq*t)

# Plot the data
plt.plot(t,x)

# Format the plot
plt.xlabel('Time[sec]')
plt.ylabel('Values')

# Generate a figure, one directory up
plt.savefig(r'..\Sinewave.png', dpi=200)

# Put it on the screen
plt.show()
