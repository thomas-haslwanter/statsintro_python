""" Comparison of two groups
- Analysis of paired data
- Analysis of unpaired data
"""

# author: Thomas Haslwanter, date: Feb-2021

# Import standard packages
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats


def paired_data() -> float:
    """Analysis of paired data
    Compare mean daily intake over 10 pre-menstrual
    and 10 post-menstrual days (in kJ).

    Returns
    -------
    p : probability of the Wilcoxon-test
    """
    
    # Get the data:  daily intake of energy in kJ for 11 women
    inFile = 'altman_93.txt'
    data = np.genfromtxt(inFile, delimiter=',')
    
    np.mean(data, axis=0)
    np.std(data, axis=0, ddof=1)
    
    pre = data[:,0]
    post = data[:,1]
    
    # --- >>> START stats <<< ---
    # paired t-test: doing two measurments on the same experimental unit
    # e.g., before and after a treatment
    t_statistic, p_value = stats.ttest_1samp(post - pre, 0)
    
    # p < 0.05 => alternative hypothesis:
    # the difference in mean is not equal to 0
    print(("paired t-test", p_value))
    
    # alternative to paired t-test when data has an ordinary scale or when not
    # normally distributed
    rankSum, p_value = stats.wilcoxon(post - pre, mode='approx')
    # --- >>> STOP stats <<< ---
    print(("Wilcoxon-Signed-Rank-Sum test", p_value))
    
    return p_value # should be 0.0033300139117459797
    # z-value -2.9341


def unpaired_data() -> float:
    """ Then some unpaired comparison: 24 hour total energy
    expenditure (MJ/day), in groups of lean and obese women

    Returns
    -------
    p : probability of the Mann-Whitney test
    """
    
    # Get the data: energy expenditure in mJ and stature (0=obese, 1=lean)
    inFile = 'altman_94.txt'
    energ = np.genfromtxt(inFile, delimiter=',')
    
    # Group them
    group1 = energ[:, 1] == 0
    group1 = energ[group1][:, 0]
    group2 = energ[:, 1] == 1
    group2 = energ[group2][:, 0]
    
    np.mean(group1)
    np.mean(group2)
    
    # --- >>> START stats <<< ---
    # two-sample t-test
    # null hypothesis: the two groups have the same mean
    # this test assumes the two groups have the same variance...
    # (can be checked with tests for equal variance)
    # independent groups: e.g., how boys and girls fare at an exam
    # dependent groups: e.g., how the same class fare at 2 different exams
    t_statistic, p_value = stats.ttest_ind(group1, group2)
    
    # p_value < 0.05 => alternative hypothesis:
    # they don't have the same mean at the 5% significance level
    print(f'two-sample t-test: p = {p_value}')
    
    # For non-normally distributed data, perform the two-sample wilcoxon test
    # a.k.a Mann Whitney U
    u, p_value = stats.mannwhitneyu(group1, group2)
    print('Mann-Whitney test: p = {p_value:5.3f}')
    # --- >>> STOP stats <<< ---
    
    # Plot the data
    plt.plot(group1, 'bx', label='obese')
    plt.plot(group2, 'ro', label='lean')
    plt.legend(loc=0)
    plt.show()
    
    # The same calculations, but implemented with pandas, would be:
    #import pandas as pd
    #df = pd.DataFrame(energ, columns = ['energy', 'weightClass'])
    #grouped = df.groupby('weightClass')
    #grouped.mean()
    #t_statistic, p_value = stats.ttest_ind(grouped.get_group(0).energy,
    #           grouped.get_group(1).energy)    
    #grouped.energy.plot(marker='o', lw=0)
    #plt.legend(['obese', 'lean'])
    #plt.show()
    
    return p_value  # should be 0.0010608066929400244


if __name__ == '__main__':
    p = paired_data()    
    print(f'paired: {p}')
    
    p = unpaired_data()
    
    print(f'unpaired: {p}')
