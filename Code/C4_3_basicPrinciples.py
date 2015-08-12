''' Show different ways to present statistical data
This script is written in "MATLAB" or "ipython" style, to show how best to use Python interactively.
Note than in ipython, the "show()" commands are automatically generated.
The examples contain:
- scatter plots
- histograms
- errorbars
- boxplots
- violinplots
- cumulative density functions

'''

# author: Thomas Haslwanter, date: Feb-2015

# First, import the libraries that you are going to need. You could also do
# that later, but it is better style to do that at the beginning.

# pylab imports the numpy, scipy, and matplotlib.pyplot libraries into the
# current environment

# Import standard packages
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
import seaborn as sns
import pandas as pd

# additional packages
import C2_8_mystyle   # custom module to set fontsize, etc

def main():
    '''Demonstrate the generation of different statistical standard plots'''
    
    # Univariate data -------------------------
    # Generate data that are normally distributed
    x = np.random.randn(500)
    
    # Set the fonts the way I like them
    sns.set_context('poster')
    sns.set_style('ticks')
    C2_8_mystyle.set(fs=32)
    
    # Scatter plot
    plt.scatter(np.arange(len(x)), x)
    plt.xlim([0, len(x)])
    
    # Save and show the data, in a systematic format
    C2_8_mystyle.printout('scatterPlot.png', xlabel='x', ylabel='y', title='Scatter')
    
    # Histogram
    plt.hist(x)
    C2_8_mystyle.printout('histogram_plain.png', xlabel='Data Values', ylabel='Frequency', title='Histogram, default settings')
    
    plt.hist(x,25)
    C2_8_mystyle.printout('histogram.png', xlabel='Data Values', ylabel='Frequency', title='Histogram, 25 bins')
    
    # Cumulative probability density
    numbins = 20
    plt.plot(stats.cumfreq(x,numbins)[0])
    C2_8_mystyle.printout('CumulativeFrequencyFunction.png', xlabel='Data Values', ylabel='CumFreq', title='Cumulative Frequncy')

    # KDE-plot
    sns.kdeplot(x)
    C2_8_mystyle.printout('kde.png', xlabel='Data Values', ylabel='Density',
            title='KDE_plot')
    
    # Boxplot
    # The ox consists of the first, second (middle) and third quartile
    plt.boxplot(x, sym='*')
    C2_8_mystyle.printout('boxplot.png', xlabel='Values', title='Boxplot')
    
    plt.boxplot(x, sym='*', vert=False)
    plt.title('Boxplot, horizontal')
    plt.xlabel('Values')
    plt.show()
    
    # Errorbars
    x = np.arange(5)
    y = x**2
    errorBar = x/2
    plt.errorbar(x,y, yerr=errorBar, fmt='o', capsize=5, capthick=3)
    plt.xlim([-0.2, 4.2])
    plt.ylim([-0.2, 19])
    C2_8_mystyle.printout('Errorbars.png', xlabel='Data Values', ylabel='Measurements', title='Errorbars')
    
    # Violinplot
    nd = stats.norm
    data = nd.rvs(size=(100))
    
    nd2 = stats.norm(loc = 3, scale = 1.5)
    data2 = nd2.rvs(size=(100))
    
    # Use pandas and the seaborn package for the violin plot
    df = pd.DataFrame({'Girls':data, 'Boys':data2})
    sns.violinplot(df)
    
    C2_8_mystyle.printout('violinplot.png', title='Violinplot')
    
    # Barplot
    df = pd.DataFrame(np.random.rand(10, 4), columns=['a', 'b', 'c', 'd'])
    df.plot(kind='bar', grid=False)
    C2_8_mystyle.printout('barplot.png', title='Barplot')

    # Grouped Boxplot
    sns.set_style('whitegrid')
    sns.boxplot(df)
    C2_8_mystyle.set(fs=28)
    C2_8_mystyle.printout('groupedBoxplot.png', title='sns.boxplot')

    # Bivariate Plots
    df2 = pd.DataFrame(np.random.rand(50, 4), columns=['a', 'b', 'c', 'd'])
    df2.plot(kind='scatter', x='a', y='b', s=df['c']*300);
    C2_8_mystyle.printout('bivariate.png')

    # Pieplot
    series = pd.Series(3 * np.random.rand(4), index=['a', 'b', 'c', 'd'], name='series')
    oldPalette = sns.color_palette()
    sns.set_palette("husl")
    series.plot(kind='pie', figsize=(6, 6))
    C2_8_mystyle.printout('piePlot.png', title='pie-plot')
    sns.set_palette(oldPalette)

def scatterplot():
    '''Fancy scatterplots, using the package "seaborn" '''
    import seaborn as sns
    
    df = sns.load_dataset("iris")
    sns.pairplot(df, hue="species", size=2.5)    
    C2_8_mystyle.printout_plain('multiScatterplot.png')
    
def show3D():
    '''Generation of 3D plots'''
    # imports specific to the plots in this example
    from matplotlib import cm   # colormaps
    
    # This module is required for 3D plots!
    from mpl_toolkits.mplot3d import Axes3D
    
    # Twice as wide as it is tall.
    fig = plt.figure(figsize=plt.figaspect(0.5))
    
    #---- First subplot
    # Generate the data
    X = np.arange(-5, 5, 0.1)
    Y = np.arange(-5, 5, 0.1)
    X, Y = np.meshgrid(X, Y)
    R = np.sqrt(X**2 + Y**2)
    Z = np.sin(R)
    
    # Note the definition of "projection", required for 3D  plots
    ax = fig.add_subplot(1, 2, 1, projection='3d')
    surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.jet,
            linewidth=0, antialiased=False)
    ax.set_zlim3d(-1.01, 1.01)
    
    fig.colorbar(surf, shrink=0.5, aspect=10)
    
    #---- Second subplot
    # Get some 3d test-data
    from mpl_toolkits.mplot3d.axes3d import get_test_data
    
    ax = fig.add_subplot(1, 2, 2, projection='3d')
    X, Y, Z = get_test_data(0.05)
    ax.plot_wireframe(X, Y, Z, rstride=10, cstride=10)

    C2_8_mystyle.printout_plain('3dGraph.png')
    
if __name__ == '__main__':
    scatterplot()
    main()
    show3D()
