import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters

register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv', index_col='date', parse_dates=True)

# Clean data
# Compute the 2.5th and 97.5th percentiles of the 'value' column
q_low, q_high = df['value'].quantile([0.025, 0.975])
# Filter the dataframe to exclude days with page views in the top or bottom 2.5%
data_filtered = df[(df['value'] > q_low) & (df['value'] < q_high)]


def draw_line_plot():
  # Draw line plot
  fig, ax = plt.subplots(figsize=(16, 6))
  # Set x and y data
  x = data_filtered.index
  y = data_filtered['value']

  # Create a line plot
  ax.plot(x, y, color='red', linewidth=1.5)

  # Add labels and title
  ax.set_xlabel('Date')
  ax.set_ylabel('Page Views')
  ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')

  # Save image and return fig (don't change this part)
  fig.savefig('line_plot.png')
  return fig


def draw_bar_plot():
  # Copy and modify data for monthly bar plot
  df_bar = data_filtered.copy()
  df_bar['year'] = df_bar.index.year
  df_bar['month'] = df_bar.index.strftime('%B')
  month_order = [
    'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August',
    'September', 'October', 'November', 'December'
  ]
  df_mean = df_bar.groupby(['year', 'month'
                            ])['value'].mean().unstack().reindex(month_order,
                                                                 axis=1)

  # Draw bar plot
  fig, ax = plt.subplots(figsize=(10, 6))
  ax.set_xlabel('Years')
  ax.set_ylabel('Average Page View')
  ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
 
  df_mean.plot(kind='bar', ax=ax)
  ax.legend(title='Months')

  # Save image and return fig (don't change this part)
  fig.savefig('bar_plot.png')
  return fig


def draw_box_plot():
  # Prepare data for box plots (this part is done!)
  df_box = data_filtered.copy()
  df_box.reset_index(inplace=True)
  df_box['year'] = [d.year for d in df_box.date]
  df_box['month'] = [d.strftime('%b') for d in df_box.date]

  # Draw box plots (using Seaborn)
  # Set up the plot
  fig, axs = plt.subplots(ncols=2, figsize=(15,5))
  # Plot the year-wise box plot
  sns.boxplot(x='year', y='value', data=df_box, ax=axs[0])
  axs[0].set_xlabel('Year')
  axs[0].set_ylabel('Page Views')
  axs[0].set_title('Year-wise Box Plot (Trend)')
  # Plot the month-wise box plot
  sns.boxplot(x='month', y='value', data=df_box, order=[
        'Jan','Feb','Mar','Apr','May','Jun',
        'Jul','Aug','Sep','Okt','Nov','Dec'], ax=axs[1])
  axs[1].set_xlabel('Month')
  axs[1].set_ylabel('Page Views')
  axs[1].set_title('Month-wise Box Plot (Seasonality)')
 

  # Save image and return fig (don't change this part)
  fig.savefig('box_plot.png')
  return fig

draw_line_plot()
draw_bar_plot()
draw_box_plot()
