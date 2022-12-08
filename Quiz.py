# Tennis Big 3 Statistics (+3 pts)

# We use the same tennis dataset as HW3:
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

atp1 = pd.read_csv('https://query.data.world/s/5pftzxjpnopp6cbyp23eeehljoegx2') # AO
atp2 = pd.read_csv('https://query.data.world/s/u5b76rf4aqyq6op2ojpfgfwu7n376c') # LG
atp3 = pd.read_csv('https://query.data.world/s/kgdeqxaao7crmxw4uix4twly6euq4p') # Wimbledon
atp4 = pd.read_csv('https://query.data.world/s/t3ub55t6xxydoxdwtfpuo2if54fzfc') # US
mylist = [atp1, atp2, atp3, atp4,]

# Please count the number of times player A and player B have faced off (A v.s. B) in the championship match. Show the top eight frequent match pairs and use horizontal bar to visualize the result. Plot and save the figure.
# PS: the order of the names does not matter (A v.s. B equals B v.s.A).

def quiz(mylist):
    '''
    write your code here
    prepare two list: wins and name
    '''
    plt.figure(facecolor = 'w',edgecolor= 'w' ,figsize=(10,5)) 
    plt.barh(np.arange(8), wins, color=list('ccbbbgrr'))
    plt.yticks(np.arange(8), name, fontsize=15)
    plt.xticks(np.arange(10), fontsize=15)
    plt.title('match count', fontsize=15)
    plt.grid()
    plt.tight_layout()
    plt.savefig("./quiz.png")
    plt.close()
    