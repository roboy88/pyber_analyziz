# pyber_analyziz
git clone
PyBer Analysis Analysis
This is the repository to store the PyBer (a ride-sharing app company) Analysis Challenge

Project Overview
V. Isualize is the CEO of PyBer V. Isualize has asked you to use your Python skills and knowledge of Pandas, to create a summary DataFrame of the ride-sharing data by city type. Then, using Pandas and Matplotlib, create a multiple-line graph that shows the total weekly fares for each city type. Finally, submit a written report that summarizes how the data differs by city type and how those differences can be used by decision-makers at PyBer.

Resources
Data source : city_data.csv, ride_data.csv
Anaconda 4.11.0, Python 3.9, jupyter notebook
Library Pandas, Matplotlib, Numpy, SciPy
Challenge Overview
Prerequisite:

Download the PyBer_Challenge_starter_code.ipynb file and rename it to PyBer_Challenge.ipynb file.
Deliverable 1: A ride-sharing summary DataFrame by city type
Use the step-by-step instructions below to add code where indicated by the numbered comments in the starter code file.

Step 1: Use the groupby() function to create a Series of data that has the type of city as the index, then apply the count() method to the "ride_id" column..

Step 2: Use the groupby() function to create a Series of data that has the type of city as the index, then apply the sum() method to the "driver_count" column.

Step 3: Use the groupby() function to create a Series of data that has the type of city as the index, then apply the sum() method to the "fare" column.

Step 4: Calculate the average fare per ride by city type by dividing the sum of all the fares by the total rides.

Step 5: Calculate the average fare per driver by city type by dividing the sum of all the fares by the total drivers.

Step 6: Create a PyBer summary DataFrame with all the data gathered from Steps 1-5.

Step 7: Use the provided code snippet to remove the index name ("type") from the PyBer summary DataFrame.

Step 8: Format the columns of the Pyber summary DataFrame.

Deliverable 2: A multiple-line chart of total fares for each city type
Use the step-by-step instructions below to add code where indicated by the numbered comments in the starter code file:

Step 1: Create a new DataFrame with multiple indices using the groupby() function on the "type" and "date" columns of the pyber_data_df DataFrame, then apply the sum() method on the "fare" column to show the total fare amount for each date.

Step 2: Use the provided code snippet to reset the index. This is needed to use the pivot() function in the next step (Step 3).

Step 3: Use the pivot() function to convert the DataFrame from the previous step so that the index is the "date," each column is a city "type," and the values are the "fare."

Step 4: Create a new DataFrame by using the loc method on the following date range: 2019-01-01 through 2019-04-28.

Step 5: Use the provided code snippet to reset the index of the DataFrame from the previous step (Step 4) to a datetime data type. This is necessary to use the resample() method in Step 7.

Step 6: Use the provided code snippet, df.info(), to check that the "date" is a datetime data type.

Step 7: Create a new DataFrame by applying the resample() function to the DataFrame you modified in Step 5. Resample the data in weekly bins, then apply the sum() method to get the total fares for each week. After creating the resampled DataFrame in Step 7, confirm that your DataFrame is with the date as the index and the different types of cities as the columns with the total fare for each week in each cell.

Step 8: Graph the resampled DataFrame from Step 7 using the object-oriented interface method and the df.plot() method, as well as the Matplotlib "fivethirtyeight" graph style code snippet provided in the starter code. Annotate the y-axis label and the title, then use the appropriate code to save the figure as PyBer_fare_summary.png in your "analysis" folder.

PyBer Analysis Results
PyBer ride-sharing summary DataFrame by city type image_name

PyBer - Multiple-line chart of total fares for each city type image_name

The total number of drivers in rural areas are much less.

The average fare per ride in rural areas are greater.

The average fare per driver in rural areas are greater too.

The total fare in urban areas are more.

PyBer Analysis Summary
Summarize three business recommendations to the CEO for addressing any disparities among the city types:

Add additional drivers in rural areas to bring down the average fare per ride/drivr and increase total revenue for PyBer.
Add additional drivers in suburban areas to bring down the average fare per ride/drivr and increase total revenue for PyBer.
In urban areas, the total drivers are more and we can move some of them to rural/suburban there by balancing the revenue from all three city types.
