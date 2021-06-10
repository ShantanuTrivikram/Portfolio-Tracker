import matplotlib.pyplot as plt 
from portfolio import *
import seaborn as sns
import datetime as dt

def mf_data_plot(mf_data):  
    sns.set_theme()
    activity = []
    y_data = []
    for i in mf_data:
        y_data.append(float(i))
    print(y_data)
    for i in range(30):
        activity.append(i)
    print(activity)
    fig, ax = plt.subplots()
    ax.plot(activity, y_data, label="price")
    ax.legend()
    plt.show()


plot_data = plot_stockdata_mf(mf())
mf_data_plot(plot_data)