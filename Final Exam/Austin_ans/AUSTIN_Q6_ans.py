import numpy as np
import pandas as pd 
import sklearn # or its sub-package
from sklearn import datasets
import matplotlib.pyplot as plt
# 題目：Low-pass filter
# 試將有呼吸雜訊的ECG signal轉變為clean，越接近越好

clean = np.loadtxt('https://raw.githubusercontent.com/Kungbohan/final2022/main/101_original.csv')
noisy = np.loadtxt('https://raw.githubusercontent.com/Kungbohan/final2022/main/101_noisy.csv')

def denoise_ecg(data):
    size=130
    window=list()
    corr=[0]*len(data)
    for i in range(0,len(data)):
        if i-size not in range(0,len(data)) or i+size not in range(0,len(data)):
            pass
        else: 
            window=data[i-size:i+size]
            corr[i]=np.mean(window)
            
    ans=np.array(corr)                                                    
    denoised_signal=data-ans
    return denoised_signal

correct = denoise_ecg(noisy)
print(f'Your mean square error is: {np.sum((correct-clean)**2)/len(clean)}')