'''Code for generating Anscombe's Quartet.
Very closely based on the code from the seaborn-documentation
http://web.stanford.edu/~mwaskom/software/seaborn/examples/anscombes_quartet.html
Note that this program requires a web-connection to load the dataset!
'''

# Copyright(c) 2015, Thomas Haslwanter. All rights reserved, under the CC BY-SA 4.0 International License

# Import standard packages
import seaborn as sns
import os

# additional packages
import sys
sys.path.append(os.path.join('..', '..', 'Utilities'))

try:
# Import formatting commands if directory "Utilities" is available
    from ISP_mystyle import showData 
    
except ImportError:
# Ensure correct performance otherwise
    def showData(*options):
        plt.show()
        return

# additional packages
import sys
sys.path.append(os.path.join('..', '..', 'Utilities'))
import ISP_mystyle

sns.set(style="ticks")

# Load the example dataset for Anscombe's quartet
df = sns.load_dataset("anscombe")

# Show the results of a linear regression within each dataset
sns.lmplot(x="x", y="y", col="dataset", hue="dataset", data=df,
           col_wrap=2, ci=None, palette="muted", size=4,
           scatter_kws={"s": 50, "alpha": 1})           

outFile = 'Anscombes_quartet.png'
showData(outFile)
