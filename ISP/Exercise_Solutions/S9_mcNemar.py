"""Solution for Exercise "Categorical Data"
McNemar's Test
"""

# author: Thomas Haslwanter, date: Feb-2021

from scipy import stats
from statsmodels.sandbox.stats.runs import mcnemar

obs = [[19,1], [6, 14]]
obs2 = [[20,0], [6, 14]]

_, p = mcnemar(obs)
_, p2 = mcnemar(obs2)

print('\n--- McNemar Test ---')
if p < 0.05:
    print('The results from the neurologist are' +
    f' significanlty different from the questionnaire (p={p:5.3f}).')
else:
    print('The results from the neurologist are' +
          f' NOT significanlty different from the questionnaire (p={p:5.3f}).')
    
if (p<0.05 == p2<0.05):
    print('The results would NOT change' +
          ' if the expert had diagnosed all "sane" people correctly.')
else:
    print('The results would change' +
          ' if the expert had diagnosed all "sane" people correctly.')
