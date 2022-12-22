import numpy as np
import pandas as pd 
import sklearn # or its sub-package
from sklearn import datasets
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans

# Following the previous question, we reduce the data dimension to 2 and visualize the result using a 2-D scattering plot. We observe that the datapoints with different labels seem separable. Thus, let's try to classify datapoints without label information.

# As the previous question, train your normalization and PCA model using X_train.
# Perform the k-means clustering (cluster=2) using the PCA results. (Now, your model pipeline is Normalize --> PCA --> kmeans)
# Apply the normalization and PCA model to X_test. Note that the normalization and PCA model is trained using X_train.
# Use plt.scatter to to visualize the PCA results of X_test. In addition, plot the center (two points) of your k-means model.
# Evaluate your model and calculate the accuracy using X_test and y_test. Return the accuracy.
# Check your answer. The function my_kmeans() would save a scatter plot and return the accuracy on the test set.
cancer = datasets.load_breast_cancer(as_frame=True)
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(cancer['data'], cancer.target, test_size=0.3, random_state=0, stratify=cancer.target)

def my_kmeans(X_train, y_train, X_test, y_test):
    ''' 
    1. plot and save a figure
    2. return accuracy
    '''
    scaler = MinMaxScaler()
    scaler.fit(X_train)
    train_scale = scaler.transform(X_train)

    pca = PCA(n_components=2)
    pca.fit(train_scale)
    train_pca = pca.transform(train_scale)

    kmeans = KMeans(n_clusters=2)
    kmeans.fit(train_pca)
    anch = kmeans.cluster_centers_


    test_scale = scaler.transform(X_test)
    test_pca = pca.transform(test_scale)
    #print(test_pca)
    pre = (test_pca[:, 0] < 0).astype(int)
    ans = y_test.to_numpy()
    corr = (pre == ans).astype(int)
    acc = corr.sum() / len(ans)
    plt.scatter(test_pca[:, 0], test_pca[:, 1], c=y_test) # please refer to lecture note
    plt.scatter(anch[0, 0], anch[0, 1], marker='*')
    plt.scatter(anch[1, 0], anch[1, 1], marker = '*')
    plt.legend(loc='best')
    plt.title('Unsupervised classifier')
    plt.tight_layout()
    plt.savefig('./kmeans_results.png')
    return acc 
    
acc=my_kmeans(X_train, y_train, X_test, y_test)
print(acc)
