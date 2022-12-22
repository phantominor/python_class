import numpy as np
import pandas as pd 
import sklearn # or its sub-package
from sklearn import datasets
import matplotlib.pyplot as plt
# In the previous question, we used unsupervised learning to train a classifier and achieved favorable classification results, even though we did not use the training labels during training. In this question, we will train a supervised k-nearest neighbors (kNN) model and compare the results to unsupervised learning.

# There are many training methods and hyperparameters for the kNN model, including the type of input data used and the number of neighbors (n_neighbors) to consider when making predictions. To determine the best settings, we will test the following:

# test different n_neighbors from 1 to 15.
# test three different training data:
# raw data, shape=(398, 30)
# normalized data (MinMaxScalar), shape=(398, 30)
# PCA data, shape=(398, 2)
# Use plt.plot to show your results in a figure with three curves. The x-axis should represent the different values of n_neighbors and the y-axis should represent the accuracy of the model.



def my_knn(X_train, y_train, X_test, y_test):
    
    ''' prepare raw_curve, std_curve, and pca_curve'''
    
    plt.plot(range(1,15), raw_curve, 'o-', label='raw', color='r')
    plt.plot(range(1,15), std_curve, 'o-', label='std', color='b')
    plt.plot(range(1,15), pca_curve, 'o-', label='pca', color='c')
    plt.grid()
    plt.legend()
    plt.xlabel('n_neighbors')
    plt.ylabel('Accuracy')
    plt.title('Accuracy under different n_neighbors')
    plt.tight_layout()
    plt.savefig('./knn_test.png')

    
my_knn(X_train, y_train, X_test, y_test)
    