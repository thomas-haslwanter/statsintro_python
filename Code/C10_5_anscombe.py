'''Code for generating Anscombe's Quartet.
Very closely based on the code from the seaborn-documentation
http://web.stanford.edu/~mwaskom/software/seaborn/examples/anscombes_quartet.html
'''
import seaborn as sns
import C2_8_mystyle

sns.set(style="ticks")

# Load the example dataset for Anscombe's quartet
df = sns.load_dataset("anscombe")

# Show the results of a linear regression within each dataset
sns.lmplot(x="x", y="y", col="dataset", hue="dataset", data=df,
           col_wrap=2, ci=None, palette="muted", size=4,
           scatter_kws={"s": 50, "alpha": 1})           

outFile = 'Anscombes_quartet.png'
C2_8_mystyle.printout_plain(outFile)