'''Solution for Exercise "Categorical Data" '''

# author: Thomas Haslwanter, date: Sept-2015

from scipy import stats

# Chi2-oneway-test
obs = [4,6,14,10,16]
_, p = stats.chisquare(obs)

print('\n--- Chi2-oneway ---')
if p < 0.05:
    print('The difference in opinion between the different age groups is significant (p={0:6.4f})'.format(p))
else:
    print('The difference in opinion between the different age groups is NOT significant (p={0:6.4f})'.format(p))

print('DOF={0:3d}'.format(len(obs)-1))