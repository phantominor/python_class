import numpy as np
import pandas as pd 
import sklearn # or its sub-package
from sklearn import datasets
import matplotlib.pyplot as plt

# We detected R-peaks of ECG signals in HW4. The signal is very clean, so it is effortless to detect R-peaks. However, in the real world, the ECG signal is always noisy, making it difficult to analyze them. Noise in ECG signals can be caused by breathing or electrical interference. In this exercise, we will attempt to denoise the ECG signals. We have loaded a clean ECG signal and a noisy ECG signal as follows:

clean = np.loadtxt('https://raw.githubusercontent.com/Kungbohan/final2022/main/101_original.csv')
noisy = np.loadtxt('https://raw.githubusercontent.com/Kungbohan/final2022/main/101_noisy.csv')
plt.plot(noisy, label='noisy')
plt.plot(clean, label='clean')
plt.legend()

# The blue curve represents the measured ECG signal, which is very noisy and exhibits some offsets. In contrast, the orange curve represents the expected clean signal, which is more consistent than the blue curve. Your task is to design a method to mitigate the noise in the measured ECG signal and transform it into the clean signal. Note that the clean signal is only used to evaluate your method, so you should not use it inside the denoise_ecg function. You can evaluate your method using the mean squared error (MSE) as follows:"

correct = denoise_ecg(noisy)
print(f'Your mean square error is: {np.sum((correct-clean)**2)/len(clean)}')
Judge:

MSE < 400 : +1pts
MSE < 350 : +1pts
MSE < 300 : +1pts
MSE < 250 : +1pts
MSE < 200 : +1pts
MSE < 160 : +1pts (Total: 6pts)

Question 6: (6 pts)
We detected R-peaks of ECG signals in HW4. The signal is very clean, so it is effortless to detect R-peaks. However, in the real world, the ECG signal is always noisy, making it difficult to analyze them. Noise in ECG signals can be caused by breathing or electrical interference. In this exercise, we will attempt to denoise the ECG signals. We have loaded a clean ECG signal and a noisy ECG signal as follows:

clean = np.loadtxt('https://raw.githubusercontent.com/Kungbohan/final2022/main/101_original.csv')
noisy = np.loadtxt('https://raw.githubusercontent.com/Kungbohan/final2022/main/101_noisy.csv')
plt.plot(noisy, label='noisy')
plt.plot(clean, label='clean')
plt.legend()
Image
The blue curve represents the measured ECG signal, which is very noisy and exhibits some offsets. In contrast, the orange curve represents the expected clean signal, which is more consistent than the blue curve. Your task is to design a method to mitigate the noise in the measured ECG signal and transform it into the clean signal. Note that the clean signal is only used to evaluate your method, so you should not use it inside the denoise_ecg function. You can evaluate your method using the mean squared error (MSE) as follows:"

correct = denoise_ecg(noisy)
print(f'Your mean square error is: {np.sum((correct-clean)**2)/len(clean)}')
Judge:

MSE < 400 : +1pts
MSE < 350 : +1pts
MSE < 300 : +1pts
MSE < 250 : +1pts
MSE < 200 : +1pts
MSE < 160 : +1pts (Total: 6pts)

Hints: low-pass filters

clean = np.loadtxt('https://raw.githubusercontent.com/Kungbohan/final2022/main/101_original.csv')
noisy = np.loadtxt('https://raw.githubusercontent.com/Kungbohan/final2022/main/101_noisy.csv')

def denoise_ecg(signal):
    ''' You should not use `clean` signal inside this function''' 
   
    return 'denoised signal'


correct = denoise_ecg(noisy)
print(f'Your mean square error is: {np.sum((correct-clean)**2)/len(clean)}')