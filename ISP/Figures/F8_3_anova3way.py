""" Plotting a three-way ANOVA """

# author: Thomas Haslwanter, date: Feb-2021

# Import standard packages
import matplotlib.pyplot as plt
import seaborn as sns

# additional packages
# Import formatting commands if directory "Utilities" is available
import os
import sys
sys.path.append(os.path.join('..', 'Code_Quantlets', 'Utilities'))
try:
    from ISP_mystyle import showData 
    
except ImportError:
# Ensure correct performance otherwise
    def showData(*options):
        plt.show()
        return

sns.set(style="whitegrid", font_scale=1.25)

df = sns.load_dataset("exercise")

sns.factorplot("time", "pulse", hue="kind", col="diet", data=df,
               hue_order=["rest", "walking", "running"],
               palette="YlGnBu_d", aspect=.75).despine(left=True)

outFile = 'ANOVA_3way.png'
showData(outFile)
