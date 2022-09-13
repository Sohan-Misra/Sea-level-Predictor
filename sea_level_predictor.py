import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    # Read data from file
    data = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    y= data['CSIRO Adjusted Sea Level']
    x= data['Year']
    plt.scatter(x,y,label='Original data')

    # Create first line of best fit
    x_alt= np.arange(data['Year'].min(),2051,1)
    res= linregress(x,y)
    plt.plot(x_alt, res.slope*x_alt + res.intercept, 'r', label='Best Fit Line 1')
    plt.xlim(1850,2075)

    # Create second line of best fit
    x_new= np.arange(2000,data['Year'].max()+1,1)
    y_new= data[data['Year']>=2000]['CSIRO Adjusted Sea Level']
    res_new= linregress(x_new,y_new)
    x_alt_new=np.arange(2000,2051,1)
    plt.plot(x_alt_new, res_new.slope*x_alt_new + res_new.intercept, 'k', label='Best Fit Line 2')
    
    # Add labels and title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()