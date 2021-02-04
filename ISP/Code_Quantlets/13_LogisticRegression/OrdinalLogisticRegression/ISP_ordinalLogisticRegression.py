""" Implementation of logistic ordinal regression (aka proportional odds) model
Based on original code in https://github.com/fabianp/minirank
"""

# author:   Thomas Haslwanter
# date:     Feb-2021

# Import standard packages
import numpy as np
import matplotlib.pyplot as plt
from typing import Tuple

# Import additional required packages
from sklearn import linear_model, metrics, preprocessing, datasets
from sklearn.model_selection import ShuffleSplit
import mord


class Classifier:
    """ Classifiers, for comparing different models
    name : name of the classifier
    clf : classifier, with the syntax of scikit-learn
    scores : scores of the training runs
    
    """

    def __init__(self, name: str, model):
        """Constructor"""
        self.name = name
        self.clf = model
        self.scores = []


def get_data() -> Tuple[np.ndarray, np.ndarray]:
    """Get and preprocess the Boston Housing data
    
    Returns
    -------
    X : features
    y : targets
    """
    
    # Get the data
    boston = datasets.load_boston()
    X,y = boston.data, np.round(boston.target)
    
    # Do a bit of pre-processing
    X = preprocessing.StandardScaler().fit(X).transform(X)
    y = np.int32(y) # required by mord
    
    return (X, y)


def compare_models(X: np.ndarray, y: np.ndarray) -> Tuple:
    """Fit and evaluate the different models
    
    Parameters
    ----------
    X : features
    y : targets
    
    Returns
    -------
    models : fitted models and fitting scores
    """
    
    # Initialize the models
    models = []
    
    # Create the 3 models
    models.append( Classifier('logistic', 
        linear_model.LogisticRegression(C=1., random_state=0, max_iter=1000) ))
    models.append( Classifier('oridinal_logistic', mord.LogisticAT(alpha=1.)) )
    models.append( Classifier('ridge', linear_model.Ridge(alpha=1.)) )
    
    # Perform repeated training, to provide a realistic comparison
    n_splits = 50
    rs = ShuffleSplit(n_splits=n_splits, test_size=0.1, random_state=0)
    
    for ii, (train, test) in enumerate(rs.split(X)):
        printProgressBar(ii, n_splits, prefix = 'Progress:',
                         suffix = 'Complete', length = 40)
        
        # we need the train set to contain all different classes
        if set(y[train]) != set(y):
            continue
        
        # Logistic classifier
        for model in models: 
            model.clf.fit(X[train], y[train])
            model.scores.append(
              metrics.mean_absolute_error(model.clf.predict(X[test]), y[test]) )
        
    return models


def show_results(models, out_file: str) -> None:
    """Generate a nice output plot
    
    Parameters
    ----------
    models : fitted models
    out_file : name of out_file
    
    """
    
    # Extract and print the data
    names = []
    scores = []
    errors = []
    
    print('------- Results ------\n')
    for model in models:
        name = model.name
        score = np.mean(model.scores)
        error = np.std(model.scores)
        
        print(f'Mean absolute error {name.upper():18s}:',
              f'{score:.2f} +/- {error:.2f}' )
              
        names.append(name)
        scores.append(score)
        errors.append(error)
    
    
    # Generate a horizontal bar-plot, with errorbars
    fig, ax = plt.subplots()
    y_pos = np.arange(len(names))
    ax.barh(y_pos, scores, xerr=errors, align='center')
    
    # Format the plot
    ax.set_yticks(y_pos)
    ax.set_yticklabels(names, rotation=45)
    ax.set_xlabel('Performance')
    ax.set_title('Mean absolute error')
    
    # Save the result
    print(f'Score-image saved to {out_file}.')
    plt.tight_layout()
    plt.savefig(out_file, dpi=200)
    plt.show()    
    
    
def printProgressBar (iteration: int,
                      total: int,
                      prefix: str = '',
                      suffix: str = '',
                      decimals: int = 1,
                      length: int = 100,
                      fill: str = '█',
                      printEnd: str = "\r") -> None:
    """ Call in a loop to create terminal progress bar
    
    Parameters
    -----=----
    iteration: current iteration [required]
    total    : total iterations [required]
    prefix   : prefix string
    suffix   : suffix string
    decimals : positive number of decimals in percent complete
    length   : character length of bar
    fill     : bar fill character
    printEnd : end character (e.g. "\r", "\r\n")
    """
    value = 100*iteration/total
    percent = ("{0:." + str(decimals) + "f}").format(value)
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end = printEnd)
    # Print New Line on Complete
    if iteration == total: 
        print()        
        
        
if __name__ == '__main__':
    out_file = 'ordinal_logistic_regression.jpg'
    
    X, y = get_data()
    models = compare_models(X, y)
    show_results(models, out_file)
    
    
