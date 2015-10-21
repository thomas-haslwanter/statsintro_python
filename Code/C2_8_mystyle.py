'''Common formatting and print commands, for the book "Introduction to Statistics with Python".
These commands ensure a common layout, and reduce the code required to generate plots
in the other modules.
'''

# author: Thomas Haslwanter, date: June-2015

# Import standard packages
import matplotlib.pyplot as plt
import os

# additional packages
import matplotlib as mpl

def despine(axis='right'):
    '''Despine a plot'''
    
    ax = plt.gca()
    ax.spines['right'].set_color('none')
    ax.yaxis.set_ticks_position('left')

def set(fs=24):
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
    mpl.rc( 'figure', **figure)
    
def printout(outFile, xlabel = '', ylabel='', title='', outDir = '..\Images'):
    '''Save the current figure to a file, and then display it'''
    
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    
    plt.tight_layout
    
    xlim = plt.gca().get_xlim()
    plt.hlines(0, xlim[0], xlim[1], linestyles='--', colors='#999999')
    plt.gca().set_xlim(xlim)
    
    saveTo = os.path.join(outDir, outFile)
    plt.savefig(saveTo, dpi=200)
    
    print('OutDir: {0}'.format(outDir))
    print('Figure saved to {0}'.format(outFile))
    
    plt.show()
    plt.close()

def printout_plain(outFile, outDir = '..\Images'):
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
    set()
