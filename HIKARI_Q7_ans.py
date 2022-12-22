import numpy as np
import pandas as pd 
import sklearn # or its sub-package
from sklearn import datasets
import matplotlib.pyplot as plt

# A confusion matrix is a table that is used to evaluate the performance of a classification algorithm. It shows the number of correct and incorrect predictions made by the model, organized by the predicted class and the actual class. The columns of the matrix represent the predicted class, and the rows represent the actual class. The entries in the matrix show the number of instances that were predicted to be in a particular class, but were actually in a different class.

# For example, consider a binary classification problem where the goal is to classify items as either "positive" or "negative". A confusion matrix for this problem might look like this:

#        Predicted
#         Positive   Negative
# Actual
# Positive      TP       FN
# Negative      FP       TN
# In this matrix, TP (true positive) refers to the number of items that were correctly classified as positive, TN (true negative) refers to the number of items that were correctly classified as negative, FP (false positive) refers to the number of items that were incorrectly classified as positive, and FN (false negative) refers to the number of items that were incorrectly classified as negative.

# Confusion matrices are often used in conjunction with other metrics, such as precision, recall, and accuracy, to evaluate the performance of a classification model. Their definition are as follows:

# Precision = TP / (TP + FP)
# Recall = TP / (TP + FN)
# Accuracy = (TP + TN) / (TP + TN + FP + FN)
# Write a class called evaluation. The class takes two arguments in its constructor: "prediction" and "actual_value". These are both lists of predicted and actual values, respectively, for the classification task. Assume that 1 is positive and 0 is negative. The class also has four methods: confusion_matrix(), precision(), recall(), and accuracy(). These methods return the corresponding evaluation metric based on "prediction" and "actual_value". The confusion_matrix() method returns a NumPy array representing the confusion matrix for the classification task. The precision() method returns the precision score. The recall() method returns the recall score. Finally, the accuracy() method returns the accuracy score. If you finish your evaluation, you can run the following code to check your results.

# >>> my_evaluation = evaluation([0, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0], [1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0])
# >>> print('Confusion matrix:\n', my_evaluation.confusion_matrix())
# Confusion matrix:
# [[3 2]
#  [1 5]]
# >>> print('Precision:', my_evaluation.precision())
# Precision: 0.75
# >>> print('Recall:', my_evaluation.recall())
# Recall: 0.6
# >>> print('Accuracy:', my_evaluation.accuracy())
# Accuracy: 0.7272727272727273

class evaluation:
    def __init__(self, prediction, actual_value):
        self.prediction = prediction
        self.actual_value = actual_value   
        'code here'
        TP = 0
        FP = 0
        TN = 0
        FN = 0
        for i in range(len(prediction)):
            if prediction[i] == 1:
                if actual_value[i] == 1:
                    TP += 1
                if actual_value[i] == 0:
                    FP += 1
            if prediction[i] == 0:
                if actual_value[i] == 1:
                    FN += 1
                if actual_value[i] == 0:
                    TN += 1
        self.TP = TP
        self.FP = FP
        self.TN = TN
        self.FN = FN

    def confusion_matrix(self):
        'here, etc.'
        return np.array([[self.TP, self.FN], [self.FP, self.FN]])
    
    def precision(self):
        return self.TP / (self.TP + self.FP)
    
    def recall(self):
        return self.TP / (self.TP + self.FN)
    
    def accuracy(self):
        return (self.TP + self.TN) / (self.TP + self.TN + self.FP + self.FN)

my_evaluation = evaluation([0, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0], [1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0])
print('Confusion matrix:\n', my_evaluation.confusion_matrix())
print('Precision:', my_evaluation.precision())
print('Recall:', my_evaluation.recall())
print('Accuracy:', my_evaluation.accuracy())
