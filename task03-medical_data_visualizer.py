import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv ( 'medical_examination.csv' )

# Add 'overweight' column
df['overweight'] = df['overweight'] = (df["weight"] / (df["height"] / 100) ** 2).apply ( lambda x: 1 if x > 25 else 0 )

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
df['cholesterol'] = df['cholesterol'].map ( lambda x: 0 if x == 1 else 1 )
df['gluc'] = df['gluc'].map ( lambda x: 0 if x == 1 else 1 )


# Draw Categorical Plot
def draw_cat_plot():
    # Set the style for the plots
    sns.set ( style='whitegrid' )

    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    df_cat = pd.melt ( df, id_vars=['cardio'], value_vars=['active', 'alco', 'cholesterol', 'gluc', 'smoke'] )

    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly.
    # Draw the catplot with 'sns.catplot()'
    df_cat_plot = sns.catplot ( x='variable', hue='value', col='cardio', data=df_cat, kind='count', height=6, aspect=1 )
    df_cat_plot.set_axis_labels ( "variable", "total" )
    plt.show ()
    # Get the figure for the output
    fig = df_cat_plot

    # Do not modify the next two lines
    fig.savefig ( 'catplot.png' )
    return fig


# Clean the data.
# Filter out the following patient segments that represent incorrect data:
# If diastolic pressure is higher than systolic (Keep the correct data with (df['ap_lo'] <= df['ap_hi'])) and in another way remove last 0 from ap_lo value
df.loc[df['ap_lo'] > df['ap_hi'], 'ap_lo'] = df.loc[df['ap_lo'] > df['ap_hi'], 'ap_lo'].astype ( str ).str[:-1]

# height is less than the 2.5th percentile (Keep the correct data with (df['height'] >= df['height'].quantile(0.025)))
df.loc[df['height'] <= df['height'].quantile ( 0.025 ), 'height'] = df['height'].quantile ( 0.025 )

# height is more than the 97.5th percentile
df.loc[df['height'] > df['height'].quantile ( 0.975 ), 'height'] = df['height'].quantile ( 0.975 )

# weight is less than the 2.5th percentile
df.loc[df['weight'] <= df['weight'].quantile ( 0.025 ), 'weight'] = df['weight'].quantile ( 0.025 )

# weight is more than the 97.5th percentile
df.loc[df['weight'] > df['weight'].quantile ( 0.975 ), 'weight'] = df['weight'].quantile ( 0.975 )


# Draw Heat Ma
def draw_heat_map():
    # Calculate the correlation matrix
    corr = df.corr ()

    # Generate a mask for the upper triangle
    mask = np.triu ( np.ones_like ( corr, dtype=bool ) )

    # Draw the heatmap with 'sns.heatmap()'
    df_heat_map_plot = sns.heatmap ( corr, mask=mask, annot=True, cmap='coolwarm' )
    plt.show()
    fig = df_heat_map_plot.figure
    # Do not modify the next two lines
    fig.savefig ( 'heatmap.png' )
    return fig


# Test your function by calling it here
draw_cat_plot ()
draw_heat_map ()
