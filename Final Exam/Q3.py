import numpy as np
import pandas as pd 
import sklearn # or its sub-package
from sklearn import datasets
import matplotlib.pyplot as plt
# Following the previous question, we reduce the data dimension to 2 and visualize the result using a 2-D scattering plot. We observe that the datapoints with different labels seem separable. Thus, let's try to classify datapoints without label information.

# As the previous question, train your normalization and PCA model using X_train.
# Perform the k-means clustering (cluster=2) using the PCA results. (Now, your model pipeline is Normalize --> PCA --> kmeans)
# Apply the normalization and PCA model to X_test. Note that the normalization and PCA model is trained using X_train.
# Use plt.scatter to to visualize the PCA results of X_test. In addition, plot the center (two points) of your k-means model.
# Evaluate your model and calculate the accuracy using X_test and y_test. Return the accuracy.
# Check your answer. The function my_kmeans() would save a scatter plot and return the accuracy on the test set.


def my_kmeans(X_train, y_train, X_test, y_test):
    ''' 
    1. plot and save a figure
    2. return accuracy
    '''
    plt.scatter() # please refer to lecture note
    plt.legend(loc='best')
    plt.title('Unsupervised classifier')
    plt.tight_layout()
    plt.savefig('./kmeans_results.png')
    
    return acc 
    
acc=my_kmeans(X_train, y_train, X_test, y_test)
print(acc)