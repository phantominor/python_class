import numpy as np
import pandas as pd 
import sklearn # or its sub-package
from sklearn import datasets
import matplotlib.pyplot as plt
# We use the breast dataset from sklean in this question:

# load dataset
cancer = datasets.load_breast_cancer(as_frame=True)

# split dataset
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(cancer['data'], cancer.target, test_size=0.3, random_state=0, stratify=cancer.target)
# In this question, we want to analyze the breast cancer dataset further. 
# First, use MinMaxScaler to normalize the data. 
# Next, use PCA to reduce the feature dimension to 2. 
# Use plt.scatter to visualize the data points, and annotate each data point using its label with different colors. (class 0: green; class 1: blue)

# Note that only X_train and y_train will be used in this question.

def pca_plot(X_train, y_train):

    plt.xlabel('PC 1')
    plt.ylabel('PC 2')
    plt.legend(loc='lower right')
    plt.title('Q2: PCA on breast cancer dataset')
    plt.tight_layout()
    plt.savefig('./q2_pca.png')
    
pca_plot(X_train, y_train)