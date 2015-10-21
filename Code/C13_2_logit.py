'''Logistic Regression
A logistic regression is an example of a "Generalized Linear Model (GLM)".

The input values are the recorded O-ring data from the space shuttle launches before 1986,
and the fit indicates the likelihood of failure for an O-ring.

Taken from http://www.brightstat.com/index.php?option=com_content&task=view&id=41&Itemid=1&limit=1&limitstart=2
'''

# author: Thomas Haslwanter, date: Sept-2015

# Import standard packages
import numpy as np
import matplotlib.pyplot as plt
import os
import pandas as pd
import seaborn as sns

# additional packages
import C2_8_mystyle
from statsmodels.formula.api import glm
from statsmodels.genmod.families import Binomial

def getData():
    '''Get the data '''
    
    dataDir = r'..\Data\data_bayes'
    fileName = 'challenger_data.csv'
    inFile = os.path.join(dataDir, fileName)
    
    data = np.genfromtxt(inFile, skip_header=1, usecols=[1, 2],
                                    missing_values='NA', delimiter=',')
    # Eliminate NaNs
    data = data[~np.isnan(data[:, 1])]
    
    return data
    
def prepareForFit(inData):
    ''' Make the temperature-values unique, and count the number of failures and successes.
    Returns a DataFrame'''
    
    # Create a dataframe, with suitable columns for the fit
    df = pd.DataFrame()
    df['temp'] = np.unique(inData[:,0])
    df['failed'] = 0
    df['ok'] = 0
    df['total'] = 0
    df.index = df.temp.values
    
    # Count the number of starts and failures
    for ii in range(inData.shape[0]):
        curTemp = inData[ii,0]
        curVal  = inData[ii,1]
        df.loc[curTemp,'total'] += 1
        if curVal == 1:
            df.loc[curTemp, 'failed'] += 1
        else:
            df.loc[curTemp, 'ok'] += 1
    
    return df

def logistic(x, beta, alpha=0):
    ''' Logistic Function '''
    return 1.0 / (1.0 + np.exp(np.dot(beta, x) + alpha))

def showResults(challenger_data, model):
    ''' Show the original data, and the resulting logit-fit'''
    
    # First plot the original data
    plt.figure()
    sns.set_context('poster')
    sns.set_style('whitegrid')
    np.set_printoptions(precision=3, suppress=True)
    
    plt.scatter(challenger_data[:, 0], challenger_data[:, 1], s=75, color="k",
                alpha=0.5)
    plt.yticks([0, 1])
    plt.ylabel("Damage Incident?")
    plt.xlabel("Outside temperature (Fahrenheit)")
    plt.title("Defects of the Space Shuttle O-Rings vs temperature")
    plt.xlim(50, 85)
    
    # Plot the fit
    x = np.arange(50, 85)
    alpha = model.params[0]
    beta = model.params[1]
    y = logistic(x, beta, alpha)
    
    plt.hold(True)
    plt.plot(x,y,'r')
    outFile = 'ChallengerPlain.png'
    C2_8_mystyle.printout_plain(outFile, outDir='..\Images')
    plt.show()
    
    
if __name__ == '__main__':
    inData = getData()
    dfFit = prepareForFit(inData)
    
    # fit the model
    
    # --- >>> START stats <<< ---
    model = glm('ok + failed ~ temp', data=dfFit, family=Binomial()).fit()
    # --- >>> STOP stats <<< ---
    
    print(model.summary())
    
    showResults(inData, model)
    
