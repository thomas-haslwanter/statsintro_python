"""Solution to Exercise 'Binary Data' of the chapter 'Data Input' 

Read in binary data, with an 256 byte ASCII-header.
"""

# author:   Thomas Haslwanter
# date:     June-2020

# Import the required packages
import numpy as np
import matplotlib.pyplot as plt
import array


# Set the parameters
data_file = 'data.raw'
length_header = 256     # byte

# Approach #1: -------------------------------

# Read and show the file header
fh = open(data_file, 'rb')
txt = fh.read(length_header).decode()
print(txt)

# Read all the binary data
bin_data = fh.read()

# Interpret them as 'double', and reshape them to an ndarray
double = 8  # byte
num_cols = 3
num_data = int(len(bin_data)/(num_cols*double))    # needs to be an integer
values = array.array('d', bin_data)
mat = np.reshape(values, (num_data,-1))

# Assign the three columns to the variables (t,x,y)
t,x,y = mat.T

# Plot the data
fig, axs = plt.subplots(2,1)
axs[0].plot(t, x)
axs[1].plot(t, y)
axs[0].set_title('Retrieved Data')
plt.show()


# Approach #2: -------------------------------

# Define a structured array
dt = np.dtype([('t', 'd'), ('x', 'd'), ('y', 'd')])

# Position the file pointer after the header
fh.seek(256)

# Read the data in as a structured array
structured_array = np.fromfile(fh, dtype=dt)

# Convert that array to a numpy-ndarray
mat = np.array(structured_array.tolist())

# Plot the data again
fig, axs = plt.subplots(2,1)
axs[0].plot(t, x)
axs[1].plot(t, y)
axs[0].set_title('Retrieved Data, Version 2')
plt.show()
