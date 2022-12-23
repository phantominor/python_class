# AUSTIN_Q4_ans.py
import numpy as np
import pandas as pd 
import sklearn # or its sub-package
from sklearn import datasets
from sklearn.preprocessing import MinMaxScaler
from sklearn.decomposition import PCA
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt

# We use the breast dataset from sklearn in this question:
# load dataset
cancer = datasets.load_breast_cancer(as_frame=True)

# split dataset
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(cancer['data'], cancer.target, test_size=0.3, 
                                                    random_state=0, stratify=cancer.target)

# 題目：train一個supervised kNN model，並且和前面三個unsupervised model比較。將n-neighbors結果繪製成折線圖。
def my_knn(X_train, y_train, X_test, y_test):
    
    #preprocessing
    from sklearn.preprocessing import MinMaxScaler
    mm = MinMaxScaler()
    X_train_std = mm.fit_transform(X_train)
    X_test_std = mm.transform(X_test)
    
    #PCA
    pca = PCA(n_components=2)
    X_train_pca = pca.fit_transform(X_train_std)
    X_test_pca = pca.transform(X_test_std)
    
    raw_curve=list(range(1,16))
    std_curve=list(range(1,16))
    pca_curve=list(range(1,16))
    
    #raw_curve
    for i in range(0,15):
        knn = KNeighborsClassifier(n_neighbors=i+1)
        knn.fit(X_train, y_train)
        raw_curve[i]=knn.score(X_test, y_test)
        
    #std_curve
    for i in range(0,15):
        knn = KNeighborsClassifier(n_neighbors=i+1)
        knn.fit(X_train_std, y_train)
        std_curve[i]=knn.score(X_test_std, y_test)
        
    #pca_curve
    for i in range(0,15):
        knn = KNeighborsClassifier(n_neighbors=i+1)
        knn.fit(X_train_pca, y_train)
        pca_curve[i]=knn.score(X_test_pca, y_test)
    
    ''' prepare raw_curve, std_curve, and pca_curve'''
    
    plt.plot(range(1,16), raw_curve, 'o-', label='raw', color='r')
    plt.plot(range(1,16), std_curve, 'o-', label='std', color='b')
    plt.plot(range(1,16), pca_curve, 'o-', label='pca', color='c')
    plt.grid()
    plt.legend()
    plt.xlabel('n_neighbors')
    plt.ylabel('Accuracy')
    plt.title('Accuracy under different n_neighbors')
    plt.tight_layout()
    # plt.savefig('./knn_test.png')
    plt.show()

my_knn(X_train, y_train, X_test, y_test)
