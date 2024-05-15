import pandas as pd
import numpy as np

class Visualization:
   
    training = pd.read_csv('train.csv')
    test = pd.read_csv('test.csv')

    # training['train_test'] = 1
    # test['train_test'] = 0
    # test['Survived'] = np.NaN

    training.info() # Gives the null value count and datatypes of columns
    print(training.describe())
    