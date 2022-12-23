# AUSTIN_Q2_ans.py
import numpy as np
import pandas as pd 
import sklearn # or its sub-package
from sklearn import datasets
import matplotlib.pyplot as plt

# We use the breast dataset from sklearn in this question:
# load dataset
cancer = datasets.load_breast_cancer(as_frame=True)

# split dataset
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(cancer['data'], cancer.target, test_size=0.3, 
                                                    random_state=0, stratify=cancer.target)

# 題目：用MinMaxScaler去normalize，用PCA降至二維，繪製散佈圖。
def pca_plot(X_train, y_train):
    #preprocessing
    from sklearn.preprocessing import MinMaxScaler
    mm = MinMaxScaler()
    X_train_std = mm.fit_transform(X_train)
    X_test_std = mm.transform(X_test)
    
    #PCA
    from sklearn.decomposition import PCA
    pca = PCA(n_components=2)
    X_train_pca = pca.fit_transform(X_train_std)
    X_test_pca = pca.transform(X_test_std)
    
    colors = ['g', 'b']
    markers = ['s', 'x']

    for l, c, m in zip(np.unique(y_train), colors, markers): # In this example there are three kinds of labels
        plt.scatter(X_train_pca[y_train == l, 0], 
                    X_train_pca[y_train == l, 1], 
                    c=c, label=l, marker=m)
        
    plt.xlabel('PC 1')
    plt.ylabel('PC 2')
    plt.legend(loc='lower right')
    plt.title('Q2: PCA on breast cancer dataset')
    plt.tight_layout()
    # plt.savefig('./q2_pca.png')
    plt.show()
    
pca_plot(X_train, y_train)