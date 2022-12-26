import numpy as np
import pandas as pd 
import sklearn # or its sub-package
from sklearn import datasets
import matplotlib.pyplot as plt
# 題目：Low-pass filter
# 試將有呼吸雜訊的ECG signal轉變為clean，越接近越好

clean = np.loadtxt('https://raw.githubusercontent.com/Kungbohan/final2022/main/101_original.csv')
noisy = np.loadtxt('https://raw.githubusercontent.com/Kungbohan/final2022/main/101_noisy.csv')

def denoise_ecg_2(signal):
    def low_pass_filter(data: np.ndarray, bandlimit, sampling_rate) -> np.ndarray:
        bandlimit_index = int(bandlimit*data.size/sampling_rate)
        fsig = np.fft.fft(data)
        for i in range(bandlimit_index+1, len(fsig)):
            fsig[i] = 0
        data_filtered = np.fft.ifft(fsig)
        return np.real(data_filtered)
    return low_pass_filter(signal, 399, 400)

correct = denoise_ecg_2(noisy)
print(f'Your mean square arror is: {np.sum((correct-clean)**2/len(clean))}')