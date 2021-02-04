""" Demonstration of some pandas data handling functionality
    - grouping of data
    - pivoting
"""

# author:   Thomas Haslwanter
# date:     Jan-2021

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from io import StringIO


def pivoting() -> None:
    """ Demonstration of pandas pivot_table """
    
    # Generate some string data
    data = '''name, exam, trial, points
    Peter, midTerm, 1, 40
    Paul, midTerm, 1, 60
    Mary, midTerm, 1, 20
    Mary, midTerm, 2, 70
    Peter, final, 1, 60
    Paul, final, 1, 20
    Mary, final, 1, 80
    Paul, final, 2, 75
    '''
    
    # Write them to a buffer
    buffer = StringIO()     # creating an empty buffer
    buffer.write(data)
    
    # Read it from the buffer into a pandas DataFrame
    buffer.seek(0)
    df = pd.read_csv(buffer, sep='[, ]+', engine='python')
    
    # Generate a pivot table
    pd.pivot_table(df, index=['exam', 'name'], values=['points'],
            columns=['trial'])
    out =  pd.pivot_table(df, index=['exam', 'name'], values=['points'],
            aggfunc=[np.max, len])
    print(out)


def grouping() -> None:
    """ Demonstration of pandas grouping function """
    
    # Generate some data
    data = pd.DataFrame({
            'Gender': ['f', 'f', 'm', 'f', 'm', 'm', 'f', 'm', 'f', 'm', 'm'],
            'TV': [3.4, 3.5, 2.6, 4.7, 4.1, 4.1, 5.1, 3.9, 3.7, 2.1, 4.3] })

    # Group the data
    grouped = data.groupby('Gender')
    
    # Do some overview statistics
    print(grouped.describe())
    
    # Grouped data can also be plotted
    grouped.boxplot()
    plt.show()
    
    # Get the groups as DataFrames
    df_female = grouped.get_group('f')    

    
if __name__ == '__main__':
    print('\n', '-'*60)
    grouping()
    
    print('\n', '-'*60)
    pivoting()
    
    """
    This produces the following printout:
   
     ------------------------------------------------------------
              TV                                               
           count      mean       std  min    25%  50%  75%  max
    Gender                                                     
    f        5.0  4.080000  0.769415  3.4  3.500  3.7  4.7  5.1
    m        6.0  3.516667  0.926103  2.1  2.925  4.0  4.1  4.3
    
     ------------------------------------------------------------
                    amax    len
                  points points
    exam    name               
    final   Mary      80      1
            Paul      75      2
            Peter     60      1
    midTerm Mary      70      2
            Paul      60      1
            Peter     40      1 
        
    """
      

