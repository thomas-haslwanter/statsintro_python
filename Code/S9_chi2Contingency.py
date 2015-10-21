'''Solution for Exercise "Categorical Data":
Chi2-test with frequency tables
'''

# author: Thomas Haslwanter, date: Sept-2015

from scipy import stats

obs = [[36,14], [30,25]]
chi2, p, dof, expected = stats.chi2_contingency(obs)

print('--- Contingency Test ---')
if p < 0.05:
    print('p={0:6.4f}: the drug affects the heart rate.'.format(p))
else:
    print('p={0:6.4f}: the drug does NOT affect the heart rate.'.format(p))
    
obs2 = [[36,14], [29,26]]
chi2, p, dof, expected = stats.chi2_contingency(obs2)
chi2, p2, dof, expected = stats.chi2_contingency(obs2, correction=False)

print('If the response in 1 non-treated person were different, \n we would get p={0:6.4f} with Yates correction, and p={1:6.4f} without.'.format(p, p2))