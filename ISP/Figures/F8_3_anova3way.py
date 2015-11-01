""" Plotting a three-way ANOVA """

# author: Thomas Haslwanter, date: Oct-2015

# Import standard packages
import matplotlib.pyplot as plt
import seaborn as sns

# additional packages
#sns.set_palette('muted')
import sys
sys.path.append(r'..\Quantlets\Utilities')
import ISP_mystyle

sns.set(style="whitegrid", font_scale=1.25)

df = sns.load_dataset("exercise")

sns.factorplot("time", "pulse", hue="kind", col="diet", data=df,
               hue_order=["rest", "walking", "running"],
               palette="YlGnBu_d", aspect=.75).despine(left=True)

outFile = 'ANOVA_3way.png'
ISP_mystyle.printout_plain(outFile)
