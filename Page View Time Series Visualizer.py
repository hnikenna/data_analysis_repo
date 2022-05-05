import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters

register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv')
df.set_index('date')

# Clean data
df = df[df['value'] > df['value'].quantile(0.025)]
df = df[df['value'] < df['value'].quantile(0.975)]
df = df.drop(df.index[1])
print(df.info)
# Create d/m/y
df['month'] = df['date'].str.split('-')
df['month'] = df['month'].to_list()
df[['year', 'month', 'day']] = df['month'].to_list()
# df['year_month'] = df['year'] + '-' + df['month']
df['month_number'] = df['month'].copy()
df['month'] = df['month'].replace({'01': 'January', '02': 'February',
                                   '03': 'March', '04': 'April',
                                   '05': 'May', '06': 'June',
                                   '07': 'July', '08': 'August',
                                   '09': 'September', '10': 'October',
                                   '11': 'November', '12': 'December'})


def draw_line_plot():
    # Draw line plot
    fig, ax = plt.subplots()
    line_plot = sns.lineplot(data=df, x='date', y='value', ax=ax)
    line_plot.set(title='Daily freeCodeCamp Forum Page Views 5/2016-12/2019', xlabel='Date', ylabel='Page Views')

    plt.show()

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig


def draw_bar_plot():
    # Copy and modify data for monthly bar plot

    df_bar = df.copy()

    # Draw bar plot
    fig, ax = plt.subplots()
    barplot = sns.barplot(data=df_bar, hue='month', x='year', ax=ax, y='value',
                          hue_order=['January', 'February', 'March', 'April', 'May', 'June', 'July',
                                     'August', 'September', 'October', 'November', 'December'])
    barplot.set(xlabel='Years', ylabel='Average Page Views')

    plt.show()

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig


def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['month'] = df_box['month'].replace({'January': 'Jan', 'February': 'Feb',
                                               'March': 'Mar', 'April': 'Apr',
                                               'May': 'May', 'June': 'Jun',
                                               'July': 'Jul', 'August': 'Aug',
                                               'September': 'Sep', 'October': 'Oct',
                                               'November': 'Nov', 'December': 'Dec'})

    # Draw box plots (using Seaborn)
    fig, ax = plt.subplots(ncols=2)
    boxplot1 = sns.boxplot(data=df_box, ax=ax[0], x='year', y='value')
    boxplot1.set(title='Year-wise Box Plot (Trend)', xlabel='Year', ylabel='Page Views')
    df_box.sort_values(by='month_number', inplace=True)
    boxplot2 = sns.boxplot(data=df_box, ax=ax[1], x='month', y='value', )
    boxplot2.set(title='Month-wise Box Plot (Seasonality)', xlabel='Month', ylabel='Page Views')
    plt.show()
    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig

draw_bar_plot()
