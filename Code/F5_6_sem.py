# [xxx]

# Import standard packages
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import seaborn as sns

np.random.seed(123)
x = np.random.randn(100) + 5
sd = np.mean(x) + np.std(x, ddof=1)*np.r_[-1, 1]
se = np.mean(x) + stats.sem(x)*np.r_[-1, 1]

sns.set_style('ticks')
sns.set_context('poster')

plt.plot(x,'.')
plt.axhline(np.mean(x))
plt.axhline(sd[0], ls='--')
plt.axhline(sd[1], ls='--')
plt.axhline(se[0], ls='--', color='r')
plt.axhline(se[1], ls='--', color='r')
plt.savefig('standardError.png', dpi=200)
plt.show()
