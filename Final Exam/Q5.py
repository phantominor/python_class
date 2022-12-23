import numpy as np
import pandas as pd 
import sklearn # or its sub-package
from sklearn import datasets
import matplotlib.pyplot as plt

# We load a Covid-19 data as follows:

# covid_df = pd.read_csv("https://raw.githubusercontent.com/datasets/covid-19/main/data/time-series-19-covid-combined.csv")
# covid_df.head(3)
# The first column is date, and the last three columns are the cumulative number of confirmed, recovered, and death case, respectively. Please compute the cumulative death rate on 2022-03-09. We define the cumulative death rate as follows:

# 𝑑𝑒𝑎𝑡ℎ_𝑟𝑎𝑡𝑒=𝐷𝑒𝑎𝑡ℎ𝑠/𝐶𝑜𝑛𝑓𝑖𝑟𝑚𝑒𝑑
 
# Next, sort the country according to the death rate and plot the top ten countries using plt.barh.

covid_df = pd.read_csv("https://raw.githubusercontent.com/datasets/covid-19/main/data/time-series-19-covid-combined.csv")
# covid_df.head()

def covid_death_rate(covid_df):
    dic = {}
    for i,j in covid_df.iterrows():
        if j['Date'] == '2022-03-09':
            if j['Confirmed'] == 0:
                dic[j['Country/Region']] = 0
            else:
                dic[j['Country/Region']] = j['Deaths']/j['Confirmed']
    result = pd.Series(dic)
    result = result.sort_values(ascending = False)
    result = result[:10]

    plt.figure(facecolor = 'w',edgecolor= 'w' ) # create an empty figure, the foreground and background are white
    plt.barh(np.arange(10), result.values, color=['b']) 
    plt.yticks(np.arange(10), result.index, fontsize=15) # "name" is the name of those six players
    plt.xticks(fontsize=6)
    plt.title('Covid Death Rate', fontsize=12) # set the title of the figure
    plt.grid() # set the grid
    plt.xlabel('Death Rate (%)', fontsize=15)
    plt.tight_layout() # align the figure
    # plt.savefig("./covid_bar.png") # save the figure
    plt.show()
    
covid_death_rate(covid_df)