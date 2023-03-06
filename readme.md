# Welcome to Data Analysis with Python!!!

- Author: Сретен Јокић / Sreten Jokic

 1. Task 01.
Create a function named calculate() in mean_var_std.py that uses Numpy to output the mean, variance, standard deviation, max, min, and sum of the rows, columns, and elements in a 3 x 3 matrix.
The input of the function should be a list containing 9 digits. The function should convert the list into a 3 x 3 Numpy array, and then return a dictionary containing the mean, variance, standard deviation, max, min, and sum along both axes and for the flattened matrix.

 2. Task 02.
Analyze demographic data using Pandas. You are given a dataset of demographic data that was extracted from the 1994 Census database.
Use Pandas to answer the following questions:
    - How many people of each race are represented in this dataset? This should be a Pandas series with race names as the index labels. (race column)
    - What is the average age of men?
    - What is the percentage of people who have a Bachelor's degree?
    - What percentage of people with advanced education (Bachelors, Masters, or Doctorate) make more than 50K?
    - What percentage of people without advanced education make more than 50K?
    - What is the minimum number of hours a person works per week?
    - What percentage of the people who work the minimum number of hours per week have a salary of more than 50K?
    - What country has the highest percentage of people that earn >50K and what is that percentage?
    - Identify the most popular occupation for those who earn >50K in India.

  3. Task 03.
We should visualize and make calculations from medical examination data using matplotlib, seaborn, and pandas. The dataset values were collected during medical examinations.

The rows in the dataset represent patients and the columns represent information like body measurements, results from various blood tests, and lifestyle choices. You will use the dataset to explore the relationship between cardiac disease, body measurements, blood markers, and lifestyle choices.
File name: medical_/examination.csv

Create a chart similar to examples/catplot.png, where we show the counts of good and bad outcomes for the cholesterol, gluc, alco, active, and smoke variables for patients with cardio=1 and cardio=0 in different panels.
     
- Add an overweight column to the data. To determine if a person is overweight, first calculate their BMI by dividing their weight in kilograms by the square of their height in meters. If that value is > 25 then the person is overweight. Use the value 0 for NOT overweight and the value 1 for overweight.
     
- Normalize the data by making 0 always good and 1 always bad. If the value of cholesterol or gluc is 1, make the value 0. If the value is more than 1, make the value 1.
     
- Convert the data into long format and create a chart that shows the value counts of the categorical features using seaborn's catplot(). The dataset should be split by 'Cardio' so there is one chart for each cardio value. The chart should look like examples/catplot.png.

![Catplot Image](/catplot.png)
     
- Clean the data. Filter out the following patient segments that represent incorrect data:
   -  diastolic pressure is higher than systolic (Keep the correct data with (df['ap_lo'] <= df['ap_hi']))
   - height is less than the 2.5th percentile (Keep the correct data with (df['height'] >= df['height'].quantile(0.025)))
   - height is more than the 97.5th percentile
   - weight is less than the 2.5th percentile
   - weight is more than the 97.5th percentile
      
- Create a correlation matrix using the dataset. Plot the correlation matrix using seaborn's heatmap(). Mask the upper triangle. The chart should look like examples/heatmap.png.

![Heatmap Image](/heatmap.png)

  4. Task 04.
You should visualize time series data using a line chart, bar chart, and box plots. You will use Pandas, Matplotlib, and Seaborn to visualize a dataset containing the number of page views each day from 2016-05-09 to 2019-12-03. The data visualizations can help us to understand the patterns in visits and identify yearly and monthly growth.
Use the data to complete the following tasks:

- Use Pandas to import the data from "fcc-forum-pageviews.csv". Set the index to the date column.

- Clean the data by filtering out days when the page views were in the top 2.5% of the dataset or bottom 2.5% of the dataset.

- Create a draw_line_plot function that uses Matplotlib to draw a line chart.
The title should be Daily freeCodeCamp Forum Page Views 5/2016-12/2019. The label on the x axis should be Date and the label on the y axis should be Page Views.
It should look like this:

![Draw_line_plot](/draw-line-plot.png)

- Create a draw_bar_plot function that draws a bar chart.
It should show average daily page views for each month grouped by year. The legend should show month labels and have a title of Months. On the chart, the label on the x axis should be Years and the label on the y axis should be Average Page Views.
It should look like this:

![Draw_Bar_plot](/draw-bar-plot.png)

- Create a draw_box_plot function that uses Seaborn to draw two adjacent box plots.
These box plots should show how the values are distributed within a given year or month and how it compares over time. The title of the first chart should be Year-wise Box Plot (Trend) and the title of the second chart should be Month-wise Box Plot (Seasonality). Make sure the month labels on bottom start at Jan and the x and y axis are labeled correctly. The boilerplate includes commands to prepare the data.
It should look like this:

![Draw_Box_plot](/draw-box-plot.png)
