'''Solution for Exercise "Correlation" in Chapter 11 '''

# author: Thomas Haslwanter, date: Oct-2015

import numpy as np
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns

def getModelData(show=True):
    ''' Get the data from an Excel-file '''
    
    # First, define the in-file and get the data
    in_file = 'AvgTemp.xls'
    
    # When the data are neatly organized, they can be read in directly with the pandas-function:
    # with "ExcelFile" you open the file
    xls = pd.ExcelFile(in_file)
    
    # and with "parse" you get get the data from the file, from the specified Excel-sheet
    data = xls.parse('Tabelle1')
    
    if show:
        data.plot('year', 'AvgTmp')
        plt.xlabel('Year')
        plt.ylabel('Average Temperature')
        plt.show()
    
    return data

if __name__=='__main__':
    data = getModelData()
    
    # Correlation ------------------------------------------------------
    # Calculate and show the different correlation coefficients
    print('Pearson correlation coefficient: {0:5.3f}'.format( data['year'].corr(data['AvgTmp'], method = 'pearson') ))
    print('Spearman correlation coefficient: {0:5.3f}'.format( data['year'].corr(data['AvgTmp'], method = 'spearman') ))
    print('Kendall tau: {0:5.3f}'.format( data['year'].corr(data['AvgTmp'], method = 'kendall') ))