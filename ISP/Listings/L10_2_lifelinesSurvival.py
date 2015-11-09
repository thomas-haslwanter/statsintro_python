''' Graphical representation of survival curves, and comparison of two
curves with logrank test.
"miR-137" is a short non-coding RNA molecule that functions to regulate
the expression levels of other genes.
'''
# author: Thomas Haslwanter, date: Jun-2015

# Import standard packages
import matplotlib.pyplot as plt

# additional packages
import sys
sys.path.append(r'..\Quantlets\Utilities')
import ISP_mystyle 

from lifelines.datasets import load_waltons
from lifelines import KaplanMeierFitter
from lifelines.statistics import logrank_test

# Set my favorite font
ISP_mystyle.setFonts(18)

# Load and show the data
df = load_waltons() # returns a Pandas DataFrame

print(df.head())
'''
    T  E    group
0   6  1  miR-137
1  13  1  miR-137
2  13  1  miR-137
3  13  1  miR-137
4  19  1  miR-137
'''

T = df['T']
E = df['E']

groups = df['group']
ix = (groups == 'miR-137')

kmf = KaplanMeierFitter()

kmf.fit(T[~ix], E[~ix], label='control')
ax = kmf.plot()

kmf.fit(T[ix], E[ix], label='miR-137')
kmf.plot(ax=ax)

plt.ylabel('Survival Probability')
outFile = 'lifelines_survival.png'
ISP_mystyle.showData(outFile)

# Compare the two curves
results = logrank_test(T[ix], T[~ix], event_observed_A=E[ix], event_observed_B=E[~ix])
results.print_summary()
