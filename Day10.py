import random
from itertools import count
import matplotlib.pyplot as plt 
from matplotlib.animation import FuncAnimation
import pandas as pd

def animate(i) : 
    df = pd.read_csv('CSV_Files/data6.csv')
    x = df['x_value']
    y1 = df['total_1']
    y2 = df['total_2']

    plt.cla()
    plt.plot(x,y1,label='Channel 1')
    plt.plot(x,y2,label='Channel 2')

    plt.legend(loc='upper left')
    plt.tight_layout()

anim = FuncAnimation(plt.gcf(),animate,interval=100)
plt.show()