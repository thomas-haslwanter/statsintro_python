"""Solution for Exercise "Categorical Data":
Chi2-test with frequency tables
"""

# author: Thomas Haslwanter, date: Feb-2021

from scipy import stats

obs = [[36,14], [30,25]]
chi2, p, dof, expected = stats.chi2_contingency(obs)

print('--- Contingency Test ---')
if p < 0.05:
    print(f'p={p:6.4f}: the drug affects the heart rate.')
else:
    print(f'p={p:6.4f}: the drug does NOT affect the heart rate.')
    
obs2 = [[36,14], [29,26]]
chi2, p, dof, expected = stats.chi2_contingency(obs2)
chi2, p2, dof, expected = stats.chi2_contingency(obs2, correction=False)

print('If the response in 1 non-treated person were different,\n'+
      f' we would get p={p:6.4f} with Yates correction,'+
      f' and p={p2:6.4f} without.')
