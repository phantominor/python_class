# AUSTIN_Q3_ans.py
import numpy as np
import pandas as pd 
import sklearn # or its sub-package
from sklearn import datasets
from sklearn.preprocessing import MinMaxScaler
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

# We use the breast dataset from sklearn in this question:
# load dataset
cancer = datasets.load_breast_cancer(as_frame=True)

# split dataset
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(cancer['data'], cancer.target, test_size=0.3, 
                                                    random_state=0, stratify=cancer.target)

# 題目：根據上題，似乎兩群可分開，使用k means clustering將PCA結果分群。將PCA model套用至X test，並且繪製散佈圖。
# 題目：利用X test與y test計算accuracy。
k=2
def init_centers(X, k):
    # @YOUSE: randomly sample k data points as centers
    # should return a (k x d) numpy array
    # hint: use some function from np.random
    sampling = np.random.choice(X.shape[0], size=k, replace=False)
    # sampling = np.randon.randint(0, X.shape[0], k) may return two same indices
    return X[sampling]

def distance(a,b):
    # @YOUSE: return the squared Euclidean distance ||a-b||^2
    # a and b are 1-D numpy array of the same length
    sum = 0
    for i in range(len(a)):
        sum += (a[i] - b[i])**2
        
    return sum

def compute_d2(X, centers):
    n = X.shape[0]
    D = np.empty((n, k))
    
    # @YOUSE: fill D[i,j] as the squared euclidean distance from point i to center j
    #for i in range(n):
    #    for j in range(k):
    #        D[i, j] = np.linalg.norm(X[i] - centers[j]) ** 2
    
    # faster way
    for i in range(n):
        D[i, :] = np.linalg.norm(X[i] - centers, axis=1) ** 2

    return D

def cluster_points(D):
    # @YOUSE: return an 1-D length-n numpy array which shows the assigned cluster for each point
    # For example, D = [[0.3, 0.2],
    #                   [0.1, 0.5],
    #                   [0.4, 0.2]]
    # should return np.array([1,0,1])    
    return np.argmin(D, axis=1)

def update_centers(X, clustering):
    d = X.shape[1]
    centers = np.empty((k, d))
    for i in range(k):
        # @YOUSE: compute the new center of cluster i  (centers[i, :])
        members = (clustering == i)
        assert any(members), f"No data point in cluster {i}"
        centers[i] = np.mean(X[members], axis=0)
    return centers

def WCSS(D):
    # @YOUSE: return the objective function value (within-cluster sum of squares)
    # For example, D = [[0.3, 0.2],
    #                   [0.1, 0.5],
    #                   [0.4, 0.2]]
    # should return 0.2 + 0.1 + 0.2 = 0.5
    min_val = np.min(D, axis=1)
    return np.sum(min_val)

def has_converged(old_centers, centers):
    # @YOUSE: return true if the k center points remain the same 
    # note that the ordering may be different
    return set([tuple(x) for x in old_centers]) == set([tuple(x) for x in centers])

def kmeans_basic(X, k):
    # @YOUSE: implement the k-means algorithm
    # print the objective function value (WCSS) at each iteration until it converges
    # return the final clustering
    old_centers = init_centers(X, k)
    centers = init_centers(X, k)
    i = 0
    while not has_converged(old_centers, centers):
        old_centers = centers
        D = compute_d2(X, centers) # assignment step
        clustering = cluster_points(D) # assignment step
        centers = update_centers(X, clustering) # update step
        i += 1
    return clustering,centers



def my_kmeans(X_train, y_train, X_test, y_test):
    
    #preprocessing
    from sklearn.preprocessing import MinMaxScaler
    mm = MinMaxScaler()
    X_train_std = mm.fit_transform(X_train)
    X_test_std = mm.transform(X_test)
    
    #PCA
    pca = PCA(n_components=2)
    X_train_pca = pca.fit_transform(X_train_std)
    X_test_pca = pca.transform(X_test_std)
    
    #k means
    
    clustering,centers=kmeans_basic(X_test_pca,2)
    
    
    ''' 
    1. plot and save a figure
    2. return accuracy
    '''
    #plot
    colors = ['g', 'b']
    markers = ['s', 'x']
    
    for l, c, m in zip(np.unique(y_test), colors, markers): # In this example there are three kinds of labels
        plt.scatter(X_test_pca[y_test == l, 0], 
                    X_test_pca[y_test == l, 1], 
                    c=c, label=l, marker=m)
    plt.scatter(centers[:,0],centers[:,1],c='r', label='k-means', marker='^')
    plt.legend(loc='best')
    plt.title('Unsupervised classifier')
    plt.tight_layout()
    # plt.savefig('./kmeans_results.png')
    plt.show()
    
    #find acc
    difference = np.sum(y_test != clustering)
    n = y_test.shape[0]
    error = min(difference, n - difference)
    acc=100-(100.0 * error / n)
    
    return acc
    
acc=my_kmeans(X_train, y_train, X_test, y_test)
print(acc,'%')
