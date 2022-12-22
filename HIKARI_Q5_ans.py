import numpy as np
import pandas as pd 
import sklearn # or its sub-package
from sklearn import datasets
import matplotlib.pyplot as plt

# We load a Covid-19 data as follows:

covid_df = pd.read_csv("https://raw.githubusercontent.com/datasets/covid-19/main/data/time-series-19-covid-combined.csv")
#covid_df = pd.read_csv("time-series-19-covid-combined.csv")

#print(covid_df.head(3))
# The first column is date, and the last three columns are the cumulative number of confirmed, recovered, and death case, respectively. Please compute the cumulative death rate on 2022-03-09. We define the cumulative death rate as follows:

# 𝑑𝑒𝑎𝑡ℎ_𝑟𝑎𝑡𝑒=𝐷𝑒𝑎𝑡ℎ𝑠/𝐶𝑜𝑛𝑓𝑖𝑟𝑚𝑒𝑑
 
# Next, sort the country according to the death rate and plot the top ten countries using plt.barh.


def covid_death_rate(covid_df):
    covid_df = covid_df[covid_df.Date=="2022-03-09"]
    #covid_df = covid_df.groupby(["Country/Region"])["Deaths"].transform('sum')
    covid_df = covid_df[covid_df.Confirmed != 0]
    covid_df["rate"] = covid_df["Deaths"] / covid_df["Confirmed"]
    #print(covid_df)
    countries = covid_df["Country/Region"].unique()
    rate_sum = pd.Series([0] * len(countries), index=countries)
    for i, row in covid_df.iterrows():
        rate_sum[row["Country/Region"]] += row["rate"]
    rate_sum = rate_sum.sort_values(ascending=False)
    country = rate_sum[:10].index.tolist()
    rate = rate_sum[:10].tolist()
    '''code here'''
    plt.figure(facecolor = 'w',edgecolor= 'w' ) # create an empty figure, the foreground and background are white
    plt.barh(np.arange(10), rate, color=['b']) 
    plt.yticks(np.arange(10), country, fontsize=15) # "name" is the name of those six players
    plt.xticks(fontsize=6)
    plt.title('Covid Death Rate', fontsize=12) # set the title of the figure
    plt.grid() # set the grid
    plt.xlabel('Death Rate (%)', fontsize=15)
    plt.tight_layout() # align the figure
    plt.savefig("./covid_bar.png") # save the figure
    
covid_death_rate(covid_df)
