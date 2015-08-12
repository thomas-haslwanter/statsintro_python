"""
Plotting a three-way ANOVA

"""

# author: Thomas Haslwanter, date: Nov-2014

# Import standard packages
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="whitegrid")

df = sns.load_dataset("exercise")

sns.factorplot("time", "pulse", hue="kind", col="diet", data=df,
               hue_order=["rest", "walking", "running"],
               palette="YlGnBu_d", aspect=.75).despine(left=True)
plt.savefig('ANOVA_3way.png', dpi=200)
plt.show()
