''' Test routine for Statsintro

'''

# author: Thomas Haslwanter, date: Aug-2015

# Import standard packages
import numpy as np
import pandas as pd

# additional packages
import unittest

import L12_1_logitShort
import C13_2_bayesianStats
import C2_7_statsmodelsIntro
from C2_8_getdata import getData
import C2_8_mystyle
import C3_2_readZip
import C4_2_gettingStarted
import C4_3_basicPrinciples
import C5_4_binomialTest
import C5_4_distDiscrete
import C5_5_centralLimitTheorem
import C5_5_distNormal
import C5_6_distContinuous
import C6_1_checkNormality
import C6_2_sampleSize
import C7_1_oneSample
import C7_2_twoSample 
import C7_3_anovaOneway
import C7_3_kruskalWallis
import C7_3_multipleTesting
import C7_3_anovaTwoway
import C8_3_compGroups
import C9_2_lifelinesDemo
import C10_1_multivariate
import C10_3_linRegModel
import C10_4_fitLine
import C10_4_models
import C10_5_anscombe
import C10_7_modeling
import C10_8_bootstrapDemo
import C11_2_multipleRegression
import C12_2_logit
import C12_4_ologit
import L2_1_pythonScript
import L2_2_pythonFunction
import L2_3_pythonImport
import L4_1_interactivePlots
import L9_1_weibullDemo
import L9_2_lifelinesSurvival

class TestSequenceFunctions(unittest.TestCase):
    def setUp(self):
        t = np.arange(0,10,0.1)
        x = np.sin(t)
        self.data = x
        
    def test_figs_BasicPrinciples(self):
        C4_3_basicPrinciples.main()
        
    def test_figs_DistributionNormal(self):
        C5_5_distNormal.simple_normal()
        C5_5_distNormal.shifted_normal()
        C5_5_distNormal.many_normals()
        
    def test_figs_DistContinuous(self):
        C5_6_distContinuous.showChi2()
        C5_6_distContinuous.showT()
        C5_6_distContinuous.showChi2()
        C5_6_distContinuous.showF()
        C5_6_distContinuous.showExp()
        
    def test_figs_DistDiscrete(self):
        C5_4_distDiscrete.show_binomial()
        C5_4_distDiscrete.show_poisson()
        
    def test_anovaOneway(self):
        (F,p) = C7_3_anovaOneway.anova_oneway()
        self.assertAlmostEqual(F, 3.711335988266943)
        self.assertAlmostEqual(p, 0.043589334959179327)
        
        (F,p) = C7_3_anovaOneway.anova_byHand()
        self.assertAlmostEqual(F, 3.711335988266943)
        self.assertAlmostEqual(p, 0.043589334959179327)
        
        F = C7_3_anovaOneway.show_teqf()
        self.assertAlmostEqual(F, 2083.481, places=2)
        
        F = C7_3_anovaOneway.anova_statsmodels()         
        self.assertAlmostEqual(F, 933.18460306573411)

    def test_anovaTwoway(self):
        F = C7_3_anovaTwoway.anova_interaction()
        self.assertAlmostEqual(F, 2113.101449275357)
        
    def test_bayesianStats(self):
        (temperature, failures) = C13_2_bayesianStats.getData()    
        (alpha, beta) = C13_2_bayesianStats.mcmcSimulations(temperature, failures)
        (linearTemperature, mean_p, p, quantiles) = C13_2_bayesianStats.calculateProbability(alpha, beta, temperature, failures)
        
        self.assertAlmostEqual(linearTemperature[20][0], 63.51020408)
        self.assertAlmostEqual(mean_p[20], 0.573, places=1) 

    def test_binomialTest(self):
        p1,p2 = C5_4_binomialTest.binomial_test(51)
        self.assertAlmostEqual(p1, 0.0265442457117)
        self.assertAlmostEqual(p2, 0.0437479701824)
        
    def test_bootstrapDemo(self):
        data = C10_8_bootstrapDemo.generate_data()
        CI = C10_8_bootstrapDemo.calc_bootstrap(data)        
        self.assertAlmostEqual(CI[0], 1.884, places=2)
        
    def test_checkNormality(self):
        p = C6_1_checkNormality.check_normality()
        self.assertAlmostEqual(p, 0.987205618534)
        
    def test_compGroups(self):
        ci = C8_3_compGroups.oneProportion()
        self.assertAlmostEqual(ci[0], 0.130, places=2)
        
        chi2 = C8_3_compGroups.chiSquare()
        self.assertAlmostEqual(chi2[0], 4.141, places=2)
        
        fisher = C8_3_compGroups.fisherExact()
        self.assertAlmostEqual(fisher[1], 0.035, places=2)
        
    def test_fitLine(self):
        
        # example data
        x = np.array([15.3, 10.8, 8.1, 19.5, 7.2, 5.3, 9.3, 11.1, 7.5, 12.2,
                      6.7, 5.2, 19.0, 15.1, 6.7, 8.6, 4.2, 10.3, 12.5, 16.1, 
                      13.3, 4.9, 8.8, 9.5])
        y = np.array([1.76, 1.34, 1.27, 1.47, 1.27, 1.49, 1.31, 1.09, 1.18, 
                      1.22, 1.25, 1.19, 1.95, 1.28, 1.52, np.nan, 1.12, 1.37, 
                      1.19, 1.05, 1.32, 1.03, 1.12, 1.70])
                      
        goodIndex = np.invert(np.logical_or(np.isnan(x), np.isnan(y)))
        (a,b,(ci_a, ci_b), ri,newy) = C10_4_fitLine.fitLine(x[goodIndex],y[goodIndex], alpha=0.01,newx=np.array([1,4.5]))        
        
        self.assertAlmostEqual(a,1.09781487777)
        self.assertAlmostEqual(b,0.02196252226)
        
    def test_getdata(self):
        data = getData('altman_93.txt', subDir='../Data/data_altman')
        self.assertEqual(data[0][0], 5260)
        
    def test_gettingStarted(self):
        C4_2_gettingStarted.main()
        
    def test_interactivePlots(self):
        L4_1_interactivePlots.normalPlot()    
        L4_1_interactivePlots.positionOnScreen()    
        L4_1_interactivePlots.showAndPause()    
        L4_1_interactivePlots.waitForInput()    
        L4_1_interactivePlots.keySelection()
        
    def test_KruskalWallis(self):
        h = C7_3_kruskalWallis.main()
        self.assertAlmostEqual(h, 16.028783253379856)
        
    def test_logit(self):
        from statsmodels.formula.api import glm
        from statsmodels.genmod.families import Binomial
        
        inData = C12_2_logit.getData()
        dfFit = C12_2_logit.prepareForFit(inData)
        model = glm('ok + failed ~ temp', data=dfFit, family=Binomial()).fit()
        C12_2_logit.showResults(inData, model)
        
        self.assertAlmostEqual(model.params.Intercept, -15.042902, places=5)
        
    def test_modeling(self):
        F = C10_7_modeling.model_formulas()
        self.assertAlmostEqual(F, 156.1407931415788)
        
        params = C10_7_modeling.polynomial_regression()
        self.assertAlmostEqual(params[0], 4.74244177)
        
    def test_multipleTesting(self):
        var = C7_3_multipleTesting.main()
        self.assertAlmostEqual(var, 1.1296296296296295)
        
    def test_multivariate(self):
        F = C10_1_multivariate.regression_line()    
        self.assertAlmostEqual(F, 4.4140184331462571)
        
        pearson = C10_1_multivariate.correlation()
        self.assertAlmostEqual(pearson, 0.79208623217849117)
        
    def test_multipleRegression(self):
        (X,Y,Z) = C11_2_multipleRegression.generatedata()    
        bestfit1 = C11_2_multipleRegression.regressionmodel(X,Y,Z)    
        self.assertAlmostEqual(bestfit1[0], -4.99754526)
        
        bestfit2 = C11_2_multipleRegression.linearmodel(X,Y,Z)        
        self.assertAlmostEqual(bestfit2[0][0], -4.99754526)
        
    def test_ologit(self):
        out = C12_4_ologit.main()
        self.assertAlmostEqual(out, 3.5623885918, places=5)
        
    def test_oneSample(self):
        p = C7_1_oneSample.check_mean()
        self.assertAlmostEqual(p, 0.018137235176105802)
        
        p2 = C7_1_oneSample.compareWithNormal()
        self.assertAlmostEqual(p2, 0.054201154690070759)

    def test_readZip(self):
        url = 'http://cdn.crcpress.com/downloads/C9500/GLM_data.zip'
        inFile = r'GLM_data/Table 2.8 Waist loss.xls'
        df = C3_2_readZip.getDataDobson(url, inFile)
        
        self.assertAlmostEqual(df['after'][0], 97)
        
    def test_sampleSize(self):
        n1 = C6_2_sampleSize.sampleSize_oneGroup(0.5)
        self.assertEqual(n1, 31)
        
        n2 = C6_2_sampleSize.sampleSize_twoGroups(0.4, sigma1=0.6, sigma2=0.6)
        self.assertEqual(n2, 35)
        
    def test_statsmodels_intro(self):
        params = C2_7_statsmodelsIntro.simple_fit()
        C2_7_statsmodelsIntro.pandas_boxplot()
    
        self.assertAlmostEqual(params.x, 0.49964655355455068)
        
    def test_twoSample(self):
        p1 = C7_2_twoSample.paired_data()
        self.assertAlmostEqual(p1, 0.0033300139117459797) 
        
        p2 = C7_2_twoSample.unpaired_data()
        self.assertAlmostEqual(p2, 0.0010608066929400244)
        
    '''
    def test_figROC(self):
        fig_roc.main()
        
    def test_gettingStarted_ipy(self):
        gettingStarted_ipy.main()
        
    def test_pandas_intro(self):
        df = pandas_intro.labelled_data()
        self.assertAlmostEqual(df['values'][0], 4.7465508100784524)
        
        parameters = pandas_intro.simple_fit(df)
        self.assertAlmostEqual(parameters['x'], 0.50516249093121246)
        
    def test_residuals(self):
        exec(compile(open('residuals.py').read(), 'residuals.py', 'exec'), {})
        
    def test_showStats(self):
        showStats.main()
        
    '''
        
if __name__ == '__main__':
    testAll = True
    if testAll:
        unittest.main()
    else:
        suite = unittest.TestSuite()
        suite.addTest(TestSequenceFunctions('test_logit'))
        runner = unittest.TextTestRunner()
        runner.run(suite)
    
    eval(input('Thanks for using programs from Thomas!'))
    
    '''
    # should raise an exception 
    self.assertRaises(TypeError, savgol, np.arange(3), window_size=5)
    self.assertTrue(np.abs(1-smoothed[round(np.pi/2*10)]<0.001))
    self.assertEqual(firstDeriv[14], fD[14])
    '''
