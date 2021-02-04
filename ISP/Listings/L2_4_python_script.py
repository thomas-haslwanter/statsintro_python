""" Short demonstration of a Python script.
After a short one-line description of the content, the header can contain
further details.
"""

# Import standard packages
import numpy as np
import matplotlib.pyplot as plt

# Generate the time-values
t = np.arange(0, 10, 0.1)

# Set the frequency, and calculate the sine-value
freq = 0.5
omega = 2 * np.pi * freq
x = np.sin(omega * t)

# Plot the data
plt.plot(t,x)

# Format the plot
plt.xlabel('Time[sec]')
plt.ylabel('Values')

# Generate a figure, one directory up, and let the user know about it
out_file = '../Sinewave.jpg'
plt.savefig(out_file, dpi=200, quality=90)
print(f'Image has been saved to {out_file}')

# Put it on the screen
plt.show()
