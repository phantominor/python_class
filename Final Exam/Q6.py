import numpy as np
import pandas as pd 
import sklearn # or its sub-package
from sklearn import datasets
import matplotlib.pyplot as plt

# We detected R-peaks of ECG signals in HW4. The signal is very clean, so it is effortless to detect R-peaks. 
# However, in the real world, the ECG signal is always noisy, making it difficult to analyze them. 
# Noise in ECG signals can be caused by breathing or electrical interference. 
# In this exercise, we will attempt to denoise the ECG signals. 
# We have loaded a clean ECG signal and a noisy ECG signal as follows:

# Question 6: (6 pts)
import numpy as np
import pandas as pd 
import sklearn # or its sub-package
from sklearn import datasets
import matplotlib.pyplot as plt
# 題目：Low-pass filter
# 試將有呼吸雜訊的ECG signal轉變為clean，越接近越好

# Judge:
# MSE < 400 : +1pts
# MSE < 350 : +1pts
# MSE < 300 : +1pts
# MSE < 250 : +1pts
# MSE < 200 : +1pts
# MSE < 160 : +1pts (Total: 6pts)

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

def denoise_ecg_2(signal):
    def low_pass_filter(data: np.ndarray, bandlimit, sampling_rate) -> np.ndarray:
        bandlimit_index = int(bandlimit*data.size/sampling_rate)
        fsig = np.fft.fft(data)
        for i in range(bandlimit_index+1, len(fsig)):
            fsig[i] = 0
        data_filtered = np.fft.ifft(fsig)
        return np.real(data_filtered)
    return low_pass_filter(signal, 399, 400)

correct1 = denoise_ecg(noisy)
correct2 = denoise_ecg_2(noisy)
correct3 = denoise_ecg(correct2)
correct4 = denoise_ecg_2(correct1)
print(f'Your mean square error is: {np.sum((correct1-clean)**2)/len(clean)}')
print(f'Your mean square error is: {np.sum((correct2-clean)**2)/len(clean)}')
print(f'Your mean square error is: {np.sum((correct3-clean)**2)/len(clean)}')
print(f'Your mean square error is: {np.sum((correct4-clean)**2)/len(clean)}')