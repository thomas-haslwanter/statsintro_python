"""Solution to Exercise 'Reading in Data' of the chapter 'Data Input' """

# author:   Thomas Haslwanter
# date:     June-2020

# Import the standard packages
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# ------------ data.csv --------------------------------
# The name "df" indicates a Pandas-DataFrame
in_file = 'data.csv'
df = pd.read_csv(in_file, index_col=0)
print(df.head())
print(df.tail())

# ------------ data_tab.txt -----------------------------
in_file = 'data_tab.txt'
df = pd.read_csv(in_file, sep='\t', header=None)
print(df.head())
print(df.tail())

# ------------ data_modified.txt ------------------------
in_file = 'data_modified.txt'
df = pd.read_csv(in_file, sep=',', header=2, index_col=0)
df.plot('t', 'values')
plt.show()

# ------------ data.xls ---------------------------------
in_file = 'data.xls'
df = pd.read_excel(in_file)
print(df.head())

# ------------ data.mat ---------------------------------
from scipy.io import loadmat
in_file = 'data.mat'
data_dict = loadmat(in_file)
print(data_dict['info'])
data = data_dict['data']
plt.plot(data[:,0], data[:,1])
plt.show()

