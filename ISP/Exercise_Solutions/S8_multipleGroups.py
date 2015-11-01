''' Solution for Exercise "Comparing Multiple Groups" '''

# author: Thomas Haslwanter, date: Sept-2015

# Load the required modules -----------------------------------------------------------
# Standard modules
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import pandas as pd

# Modules for data-analysis
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm
from statsmodels.stats import multicomp

# Module for working with Excel-files
import xlrd

def get_ANOVA_data():
    '''Get the data for the ANOVA'''

    # First we have to get the Excel-data into Python. This can be done e.g. with the package "xlrd"
    # You have to make sure that you select a valid location on your computer!
    inFile = 'Table 6.6 Plant experiment.xls'
    book = xlrd.open_workbook(inFile)
    # We assume that the data are in the first sheet. This avoids the language problem "Tabelle/Sheet"
    sheet = book.sheet_by_index(0)
    
    # Select the columns and rows that you want:
    # The "treatment" information is in column "E", i.e. you have to skip the first 4 columns
    # The "weight" information is in column "F", i.e. you have to skip the first 5 columns
    treatment = sheet.col_values(4)
    weight = sheet.col_values(5)
    
    # The data start in line 4, i.e. you have to skip the first 3
    # I use a "pandas" DataFrame, so that I can assign names to the variables.
    data = pd.DataFrame({'group':treatment[3:], 'weight':weight[3:]})
    
    return data

def do_ANOVA(data):
    '''4.3.2. Perform an ANOVA on the data'''
    
    print('ANOVA: ----------------------------------------------')
    
    # First, I fit a statistical "ordinary least square (ols)"-model to the data, using the
    # formula language from "patsy". The formula 'weight ~ C(group)' says:
    # "weight" is a function of the categorical value "group"
    # and the data are taken from the DataFrame "data", which contains "weight" and "group"
    model = ols('weight ~ C(group)', data).fit()
    
    # "anova_lm" (where "lm" stands for "linear model") extracts the ANOVA-parameters
    # from the fitted model.
    anovaResults = anova_lm(model)
    print(anovaResults)
    
    if anovaResults['PR(>F)'][0] < 0.05:
        print('One of the groups is different.')
        
def compare_many(data):
    '''Multiple comparisons: Which one is different? '''
    
    print('\n MultComp: --------------------------------------')
    
    # An ANOVA is a hypothesis test, and only answers the question: "Are all the groups 
    # from the same distribution?" It does not tell you which one is different.
    # Since we now compare many different groups to each other, we have to adjust the
    # p-values to make sure that we don't get a Type I error. For this, we use the 
    # statscom module "multicomp"
    mc = multicomp.MultiComparison(data['weight'], data['group'])
    
    # There are many ways to do multiple comparisons. Here, we choose
    # "Tukeys Honest Significant Difference" test
    # The first element of the output ("0") is a table containing the results
    print(mc.tukeyhsd().summary())
    
    # Show the group names
    print(mc.groupsunique)
    
    # Generate a print ----------------
    
    res2 = mc.tukeyhsd()     # Get the data
    
    simple = False
    if simple:
        # You can do the plot with a one-liner, but then this does not - yet - look that great
        res2.plot_simultaneous()
    else:
        # Or you can do it the hard way, i.e. by hand:
        
        # Plot values and errorbars
        xvals = np.arange(3)
        plt.plot(xvals, res2.meandiffs, 'o')
        errors = np.ravel(np.diff(res2.confint)/2)
        plt.errorbar(xvals, res2.meandiffs, yerr=errors, fmt='o')
        
        # Set the x-limits
        xlim = -0.5, 2.5
        # The "*xlim" passes the elements of the variable "xlim" elementwise into the function "hlines"
        plt.hlines(0, *xlim)
        plt.xlim(*xlim)
        
        # Plot labels (this is a bit tricky):
        # First, "np.array(mc.groupsunique)" makes an array with the names of the groups;
        # and then, "np.column_stack(res2[1][0])]" puts the correct groups together
        pair_labels = mc.groupsunique[np.column_stack(res2._multicomp.pairindices)]
        plt.xticks(xvals, pair_labels)
        
        plt.title('Multiple Comparison of Means - Tukey HSD, FWER=0.05' +
        '\n Pairwise Mean Differences')
    
    plt.show()

def KruskalWallis(data):
    '''Non-parametric comparison between the groups'''
    
    print('\n Kruskal-Wallis test ----------------------------------------------------')
    
    # First, I get the values from the dataframe
    g_a = data['weight'][data['group']=='TreatmentA']
    g_b = data['weight'][data['group']=='TreatmentB']
    g_c = data['weight'][data['group']=='Control']
    
    #Note: this could also be accomplished with the "groupby" function from pandas
    #groups = pd.groupby(data, 'group')
    #g_a = groups.get_group('TreatmentA').values[:,1]
    #g_c = groups.get_group('Control').values[:,1]
    #g_b = groups.get_group('TreatmentB').values[:,1]
    
    # Then do the Kruskal-Wallis test
    h, p = stats.kruskal(g_c, g_a, g_b)
    print('Result from Kruskal-Wallis test: p = {0}'.format(p))

if __name__ == '__main__':
    data = get_ANOVA_data()
    do_ANOVA(data)
    compare_many(data)
    KruskalWallis(data)
    
    input('\nThanks for using programs by Thomas!\nHit any key to finish')
