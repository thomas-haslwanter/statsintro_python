''' Test routine for Statsintro

'''

# author: Thomas Haslwanter, date: Jan-2014

# Import standard packages
import numpy as np
import pandas as pd

# additional packages
import unittest

import F6_10_roc
import F10_3_residuals

class TestSequenceFunctions(unittest.TestCase):
    def setUp(self):
        t = np.arange(0,10,0.1)
        x = np.sin(t)
        self.data = x
        
    def test_figROC(self):
        F6_10_roc.main()
        
    def test_residuals(self):
        exec(compile(open('F10_3_residuals.py').read(), 'F10_3_residuals.py', 'exec'), {})
        
if __name__ == '__main__':
    unittest.main()
    eval(input('Thanks for using programs from Thomas!'))
    '''
    # should raise an exception 
    self.assertRaises(TypeError, savgol, np.arange(3), window_size=5)
    self.assertTrue(np.abs(1-smoothed[round(np.pi/2*10)]<0.001))
    self.assertEqual(firstDeriv[14], fD[14])
    '''
