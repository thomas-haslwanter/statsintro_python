''' Solution for Exercise "Data Display" 
Read in weight-data recorded from newborns, and analyze the
data based on the gender of the baby.'''

# author: Thomas Haslwanter, date: Oct-2015

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import pandas as pd
import seaborn as sns
import os

def getData():
    '''Read in data from a text-file, and return them as labelled DataFrame'''
    
    # Set directory and infile
    dataDir = '.'
    inFile = 'babyboom.dat.txt'
    
    # Read and label the data
    os.chdir(dataDir)
    data = pd.read_csv(inFile, sep='[ ]*', header=None, engine='python',
                       names= ['TOB', 'sex', 'Weight', 'Minutes'])
    
    # Eliminate "Minutes", since this is redundant
    df = data[['Minutes', 'sex', 'Weight']]
    
    return(df)

def showData(df):
    '''Graphical data display'''
    
    # Show the data: first all of them ....
    plt.plot(df.Weight, 'o')
    
    plt.title('All data')
    plt.xlabel('Subject-Nr')
    plt.ylabel('Weight [g]')
    plt.show()
    
    # To make the plots easier to read, replace "1/2" with "female/male"
    df.sex = df.sex.replace([1,2], ['female', 'male'])
    
    # ... then show the grouped plots
    df.boxplot(by='sex')
    plt.show()
    
    # Display statistical information numerically
    grouped = df.groupby('sex')
    print(grouped.describe())
    
    # This is a bit fancier: scatter plots, with labels and individual symbols
    symbols = ['o', 'D']
    colors = ['r', 'b']
    
    fig = plt.figure()
    ax = fig.add_subplot(111)
    
    # "enumerate" provides a counter, and variables can be assigned names in one step if
    # the "for"-loop uses a tuple as input for each loop:
    for (ii, (sex, group)) in enumerate(grouped):
        ax.plot(group['Weight'], marker = symbols[ii], linewidth=0, color = colors[ii], label=sex)
        
    ax.legend()
    ax.set_ylabel('Weight [g]')
    plt.show()

    # Fancy finish: a kde-plot
    df.Weight = np.double(df.Weight)    # kdeplot requires doubles
    
    sns.kdeplot(grouped.get_group('male').Weight, color='b', label='male')
    plt.hold(True)
    sns.kdeplot(grouped.get_group('female').Weight, color='r', label='female')
    
    plt.xlabel('Weight [g]')
    plt.ylabel('PDF(Weight)')
    plt.show()

# Statistics: are the data normally distributed?
def isNormal(data, dataType):
    '''Check if the data are normally distributed'''
    alpha = 0.05
    (k2, pVal) = stats.normaltest(data)
    if pVal < alpha:
        print('{0} are NOT normally distributed.'.format(dataType))
    else:
        print('{0} are normally distributed.'.format(dataType))
        
def checkNormality(df):
    '''Check selected data vlaues for normality'''
    
    grouped = df.groupby('sex')
    
    # Run the check for male and female groups
    isNormal(grouped.get_group('male').Weight, 'male')
    isNormal(grouped.get_group('female').Weight, 'female')

if __name__ == '__main__':
    '''Main Program'''
    
    df = getData()
    showData(df)
    checkNormality(df)
    
    # Wait for an input before exiting
    input('Done - Hit any key to continue')
