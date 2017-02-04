'''Common formatting and print commands, for the book "Introduction to Statistics with Python".
These commands ensure a common layout, and reduce the code required to generate plots
in the other modules.
'''

# Copyright(c) 2015, Thomas Haslwanter. All rights reserved, under the CC BY-SA 4.0 International License

# Import standard packages
import matplotlib.pyplot as plt
import os

# additional packages
import matplotlib as mpl

def setFonts(fs=24):
    '''Set my favorite defaulte fonts'''
    
    font = {'family' : 'sans-serif',
            'weight' : 'normal',
            'size'   : fs}

    xtick = {'direction': 'out',
             'major.size': 6,
             'labelsize': fs-2}
    
    ytick = {'direction': 'out',
             'major.size': 6,
             'labelsize': fs-2}
    
    axes = {'labelsize': fs,
            'titlesize': fs}
    
    legend = {'fontsize': fs}
    
    figure = {'autolayout': True}
    
    mpl.rc('font', **font)
    mpl.rc('xtick', **xtick)
    mpl.rc('ytick', **ytick)
    mpl.rc('axes', **axes)
    mpl.rc('legend', **legend)
    mpl.rc('figure', **figure)
    
def showData(outFile, outDir = '.'):
    '''Save a figure with subplots to a file, and then display it'''
    
    # Generate the plot
    saveTo = os.path.join(outDir, outFile)
    plt.savefig(saveTo, dpi=200)
    
    # Show the user where the file is saved to
    print('OutDir: {0}'.format(outDir))
    print('Figure saved to {0}'.format(outFile))
    
    # Show the plot
    plt.show()
    plt.close()

if __name__ == '__main__':
    setFonts()
