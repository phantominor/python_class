import numpy as np
import pandas as pd 
import sklearn # or its sub-package
from sklearn import datasets
import matplotlib.pyplot as plt
# Load a COVID-19 data as follows:
covid_df = pd.read_csv("https://raw.githubusercontent.com/datasets/covid-19/main/data/time-series-19-covid-combined.csv")

# 題目：define 'death rate' = 'deaths' / 'confirmed'
# sort the countries according to the 'death rate' and plot the top ten using plt.barh

def covid_death_rate(covid_df):
    co=pd.Series(dtype=int)
    D=pd.Series(dtype=int)
    for i in covid_df.index:
        if covid_df.loc[i]['Date']>'2022-03-19':
            pass
        elif covid_df.loc[i,'Country/Region'] in co.index:
            co[covid_df.loc[i,'Country/Region']]+=covid_df.loc[i]['Confirmed']
            D[covid_df.loc[i,'Country/Region']]+=covid_df.loc[i]['Deaths']
        else:
            co[covid_df.loc[i,'Country/Region']]=covid_df.loc[i]['Confirmed']
            D[covid_df.loc[i,'Country/Region']]=covid_df.loc[i]['Deaths']
    # print(co.head)
    
    DR=pd.Series(D.values/co.values,index=co.index)
    
    ans=DR.sort_values(ascending=False)
    ans=ans[:10]
    
    plt.figure(facecolor = 'w',edgecolor= 'w' ) # create an empty figure, the foreground and background are white
    plt.barh(np.arange(10), ans.values, color=['b']) 
    plt.yticks(np.arange(10), ans.index, fontsize=15) # "name" is the name of those six players
    plt.xticks(fontsize=6)
    plt.title('Covid Death Rate', fontsize=12) # set the title of the figure
    plt.grid() # set the grid
    plt.xlabel('Death Rate (%)', fontsize=15)
    plt.tight_layout() # align the figure
    # plt.savefig("./covid_bar.png") # save the figure
    plt.show()
    
covid_death_rate(covid_df)
