import pandas as pd 
import numpy as np

class main:

    training = pd.read_csv('train.csv')
    test = pd.read_csv('test.csv')
    print(training.head())
