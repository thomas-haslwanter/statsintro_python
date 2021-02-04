"""Solution for Exercise "Categorical Data"
"A Lady Tasting Tea"
"""

# author: Thomas Haslwanter, date: Feb-2021

from scipy import stats
obs = [[3,1], [1,3]]
_, p = stats.fisher_exact(obs, alternative='greater')

#obs2 = [[4,0], [0,4]]
#stats.fisher_exact(obs2, alternative='greater')

print('\n--- A Lady Tasting Tea (Fisher Exact Test) ---')
print('The chance that the lady selects 3 or more cups correctly' +
      f' by chance is {p:5.3f}')
