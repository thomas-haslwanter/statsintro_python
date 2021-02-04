"""Solution for Exercise "Categorical Data" """

# author: Thomas Haslwanter, date: Feb-2021

from scipy import stats

# Chi2-oneway-test
obs = [4,6,14,10,16]
_, p = stats.chisquare(obs)

print('\n--- Chi2-oneway ---')
if p < 0.05:
    print('The difference in opinion between the different age groups is' +
          f' significant (p={p:6.4f})')
else:
    print('The difference in opinion between the different age groups is' +
    f' NOT significant (p={p:6.4f})')

print(f'DOF={len(obs)-1:3d}')
