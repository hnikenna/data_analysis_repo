import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress


def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    # df['Year'].at[0] = 2050
    x = df['Year']
    y = df['CSIRO Adjusted Sea Level']

    fig, ax = plt.subplots()
    ax.scatter(x, y)
    # Create first line of best fit
    slope = linregress(x, y).slope
    intercept = linregress(x, y).intercept

    def gradient(x):
        m = slope * x + intercept
        return m
    xo = x.tolist()
    xo.append(2050)
    yo = [gradient(i) for i in xo]
    xo = pd.Series(xo)
    yo = pd.Series(yo)
    ax.plot(xo, yo)
    # Create second line of best fit
    df2 = df[df['Year'] >= 2000]
    x2 = df2['Year']
    y2 = df2['CSIRO Adjusted Sea Level']
    slopew = linregress(x2, y2).slope
    interceptw = linregress(x2, y2).intercept

    def gradientw(x):
        m = slopew * x + interceptw
        return m
    xo = x2.tolist()
    xo.append(2050)
    yo = [gradientw(i) for i in xo]
    ax.plot(xo, yo)

    # Add labels and title
    ax.set(title='Rise in Sea Level', ylabel='Sea Level (inches)', xlabel='Year')

    # Save plot and return data for testing (DO NOT MODIFY)

    plt.show()
    plt.savefig('sea_level_plot.png')
    return plt.gca()


draw_plot()
