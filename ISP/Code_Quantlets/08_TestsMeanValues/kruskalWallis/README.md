[<img src="../../../../pictures/quantletLogo_FH.png" alt="Intro to Statistics with Python">](https://github.com/thomas-haslwanter/statsintro_python)

## [<img src="../../../../pictures/qloqo.png" alt="Visit QuantNet">](http://quantlet.de/) **ISP_kruskalWallis** [<img src="../../../../pictures/QN2.png" width="60" alt="Visit QuantNet 2.0">](http://quantlet.de/d3/ia)


```yaml
Name of QuantLet: ISP_kruskalWallis

Published in:  An Introduction to Statistics with Python

Description: Example of a Kruskal-Wallis test (for not normally distributed data)

Keywords: kruskal-wallis test,  

See also: 'ISP_anovaOneway, ISP_anovaTwoway,
    ISP_multipleTesting, ISP_oneGroup, ISP_twoGroups' 

Author: Thomas Haslwanter 

Submitted: October 31, 2015 

```

```py
'''Example of a Kruskal-Wallis test (for not normally distributed data)
Taken from http://www.brightstat.com/index.php?option=com_content&task=view&id=41&Itemid=1&limit=1&limitstart=2
'''

# Copyright(c) 2015, Thomas Haslwanter. All rights reserved, under the CC BY-SA 4.0 International License

# Import standard packages
import numpy as np

# additional packages
from scipy.stats.mstats import kruskalwallis

def main():
    '''These data could be a comparison of the smog levels in four different cities. '''
    
    # Get the data
    city1 = np.array([68, 93, 123, 83, 108, 122])
    city2 = np.array([119, 116, 101, 103, 113, 84])
    city3 = np.array([70, 68, 54, 73, 81, 68])
    city4 = np.array([61, 54, 59, 67, 59, 70])
    
    # --- >>> START stats <<< ---
    # Perform the Kruskal-Wallis test
    h, p = kruskalwallis(city1, city2, city3, city4)
    # --- >>> STOP stats <<< ---
    
    # Print the results
    if p<0.05:
        print('There is a significant difference between the cities.')
    else:
        print('No significant difference between the cities.')
        
    return h

if __name__ == '__main__':
    main()    
```
